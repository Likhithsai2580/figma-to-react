import os
import requests
import threading
from typing import Dict, Any, List
from utils import rgb_to_hex, get_foreground_color

def get_file(file: str, token: str) -> Dict[str, Any]:
    """Fetch Figma file data with enhanced error handling"""
    try:
        response = requests.get(
            f"https://api.figma.com/v1/files/{file}",
            headers={'X-FIGMA-TOKEN': token},
            timeout=30
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Figma file: {str(e)}")
        return None

def download_image(file: str, id: str, name: str, token: str, out: str = None, frame: int = None) -> str:
    """Download image assets with enhanced error handling and retries"""
    max_retries = 3
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            response = requests.get(
                f"https://api.figma.com/v1/images/{file}",
                headers={'X-FIGMA-TOKEN': token},
                params={'ids': id, 'format': 'png', 'scale': 2},
                timeout=30
            )
            response.raise_for_status()
            json_data = response.json()
            image_url = json_data.get('images', {}).get(id)

            if image_url:
                if frame is not None:
                    folder_path = os.path.join(out, 'ReactApp/src/assets', f'frame_{frame}') if out else os.path.join('ReactApp/src/assets', f'frame_{frame}')
                else:
                    folder_path = os.path.join(out, 'ReactApp/src/assets') if out else 'ReactApp/src/assets'
                    
                os.makedirs(folder_path, exist_ok=True)
                
                file_name = f'{name}.png'
                file_path = os.path.join(folder_path, file_name)
                
                image_response = requests.get(image_url, timeout=30)
                image_response.raise_for_status()

                with open(file_path, 'wb') as f:
                    f.write(image_response.content)

                return os.path.join(f'frame_{frame}' if frame is not None else '', file_name).replace('\\', '/')
            
            return None
        
        except requests.exceptions.RequestException as e:
            print(f"Error downloading image (attempt {retry_count + 1}/{max_retries}): {str(e)}")
            retry_count += 1
            if retry_count == max_retries:
                return None

def parse_effects(effects: List[Dict[str, Any]]) -> Dict[str, str]:
    """Parse Figma effects into CSS styles"""
    styles = {}
    
    for effect in effects:
        if effect['type'] == 'DROP_SHADOW':
            color = rgb_to_hex(effect['color']['r'], effect['color']['g'], effect['color']['b'], effect['color']['a'])
            styles['boxShadow'] = f"{effect['offset']['x']}px {effect['offset']['y']}px {effect['radius']}px {color}"
        elif effect['type'] == 'INNER_SHADOW':
            color = rgb_to_hex(effect['color']['r'], effect['color']['g'], effect['color']['b'], effect['color']['a'])
            styles['boxShadow'] = f"inset {effect['offset']['x']}px {effect['offset']['y']}px {effect['radius']}px {color}"
        elif effect['type'] == 'LAYER_BLUR':
            styles['filter'] = f"blur({effect['radius']}px)"
        elif effect['type'] == 'BACKGROUND_BLUR':
            styles['backdropFilter'] = f"blur({effect['radius']}px)"
    
    return styles

def parse_constraints(constraints: Dict[str, str]) -> Dict[str, str]:
    """Parse Figma constraints into CSS styles"""
    styles = {}
    
    if constraints['horizontal'] == 'CENTER':
        styles['left'] = '50%'
        styles['transform'] = 'translateX(-50%)'
    elif constraints['horizontal'] == 'RIGHT':
        styles['right'] = '0'
    elif constraints['horizontal'] == 'SCALE':
        styles['width'] = '100%'
    
    if constraints['vertical'] == 'CENTER':
        styles['top'] = '50%'
        styles['transform'] = styles.get('transform', '') + ' translateY(-50%)'
    elif constraints['vertical'] == 'BOTTOM':
        styles['bottom'] = '0'
    elif constraints['vertical'] == 'SCALE':
        styles['height'] = '100%'
    
    return styles

def parse_file(file: str, token: str, download_images: bool = True, out: str = None) -> List[Dict[str, Any]]:
    """Parse Figma file with enhanced component mapping and responsive design"""
    output = []
    result = get_file(file, token)
    
    if not result:
        return []
    
    try:
        frames = result['document']['children'][0]['children']
        frame_count = 1 if len(frames) > 1 else 0

        def parse_frame(frame: Dict[str, Any], frame_count: int):
            nonlocal output
            parsed = []
            image_count = 0

            for i in frame['children']:
                if 'absoluteBoundingBox' in i:
                    bounds = i['absoluteBoundingBox']
                else:
                    bounds = i['absoluteRenderBounds']
                
                # Enhanced component mapping
                react_components = {
                    "image": "img",
                    "button": "button",
                    "label": "label",
                    "text": "p",
                    "heading": "h1",
                    "subheading": "h2",
                    "paragraph": "p",
                    "rectangle": "div",
                    "circle": "div",
                    "oval": "div",
                    "line": "hr",
                    "textbox": "input",
                    "textarea": "textarea",
                    "listbox": "select",
                    "checkbox": "input",
                    "radio": "input",
                    "slider": "input",
                    "dropdown": "select",
                    "link": "a",
                    "icon": "span",
                    "video": "video",
                    "audio": "audio",
                    "iframe": "iframe",
                    "svg": "svg",
                    "canvas": "canvas"
                }
                
                name_parts = i['name'].lower().split(' ')
                type = name_parts[0]
                react_type = react_components.get(type, "div")
                
                # Initialize style with positioning
                i['style'] = {
                    'position': 'absolute',
                    'left': f"{abs(int(frame['absoluteBoundingBox']['x']) - int(bounds['x']))}px",
                    'top': f"{abs(int(frame['absoluteBoundingBox']['y']) - int(bounds['y']))}px",
                    'width': f"{int(bounds['width'])}px",
                    'height': f"{int(bounds['height'])}px"
                }
                
                # Add constraints-based styles
                if 'constraints' in i:
                    i['style'].update(parse_constraints(i['constraints']))
                
                # Add effects
                if 'effects' in i:
                    i['style'].update(parse_effects(i['effects']))
                
                # Process background color
                bg_color = i.get('backgroundColor') or \
                        (i.get('background', [{}])[0].get('color') if i.get('background') else None) or \
                        (i.get('fills', [{}])[0].get('color') if i.get('fills') else None)
                
                if bg_color:
                    i['style']['backgroundColor'] = rgb_to_hex(bg_color['r'], bg_color['g'], bg_color['b'])
                    fg = get_foreground_color(bg_color['r'], bg_color['g'], bg_color['b'])
                    i['style']['color'] = fg
                
                # Process borders
                if i.get('strokes'):
                    stroke = i['strokes'][0]
                    stroke_color = rgb_to_hex(stroke['color']['r'], stroke['color']['g'], stroke['color']['b'])
                    i['style']['border'] = f"{stroke.get('weight', 1)}px {stroke.get('type', 'solid')} {stroke_color}"
                
                # Process special components
                if react_type == 'input':
                    input_type = name_parts[1] if len(name_parts) > 1 else 'text'
                    i['type'] = input_type
                    if input_type in ['checkbox', 'radio']:
                        i['checked'] = False
                
                elif react_type in ['h1', 'h2', 'p']:
                    i['text'] = i.get('characters', '')
                    style = i.get('style', {})
                    i['style'].update({
                        'fontFamily': style.get('fontFamily', 'inherit'),
                        'fontSize': f"{int(style.get('fontSize', 16))}px",
                        'fontWeight': style.get('fontWeight', 'normal'),
                        'letterSpacing': f"{style.get('letterSpacing', 0)}px",
                        'lineHeight': style.get('lineHeight', 1.5)
                    })
                
                elif react_type == 'img':
                    if download_images:
                        parts = i['name'].split(' ')
                        name = " ".join(parts[1:])
                        if not name.replace(' ', '') == '':
                            download(name)
                        else:
                            image_count += 1
                            download(str(image_count))
                
                # Add border radius for rounded components
                if type in ['circle', 'oval']:
                    i['style']['borderRadius'] = '50%'
                elif 'cornerRadius' in i:
                    i['style']['borderRadius'] = f"{i['cornerRadius']}px"
                
                # Add responsive design attributes
                i['style']['maxWidth'] = '100%'
                i['style']['boxSizing'] = 'border-box'
                
                if 'layoutMode' in i:
                    i['style']['display'] = 'flex'
                    i['style']['flexDirection'] = 'column' if i['layoutMode'] == 'VERTICAL' else 'row'
                
                parsed.append(i)
            
            # Process frame background
            frame_bg = frame.get('backgroundColor') or \
                            (frame.get('background', [{}])[0].get('color') if frame.get('background') else None) or \
                            (frame.get('fills', [{}])[0].get('color') if frame.get('fills') else None)

            if frame_bg:
                frame_bg = rgb_to_hex(frame_bg['r'], frame_bg['g'], frame_bg['b'])
            else:
                frame_bg = "#ffffff"
            
            output.append({
                'components': parsed,
                'frame': {
                    'width': int(frame['absoluteBoundingBox']['width']),
                    'height': int(frame['absoluteBoundingBox']['height']),
                    'backgroundColor': frame_bg,
                    'name': result['name'],
                    'frameIndex': frame_count,
                    'description': frame.get('description', ''),
                    'effects': parse_effects(frame.get('effects', [])),
                    'constraints': parse_constraints(frame.get('constraints', {'horizontal': 'LEFT', 'vertical': 'TOP'}))
                }
            })

        threads = []
        for frame in frames:
            if frame["type"] == "FRAME":
                thread = threading.Thread(target=parse_frame, args=(frame, frame_count,))
                threads.append(thread)
                thread.start()
                frame_count += 1

        for thread in threads:
            thread.join()

    except KeyError as e:
        print(f"KeyError: {str(e)} - likely due to missing keys in JSON response")
    except Exception as e:
        print(f"Error parsing Figma file: {str(e)}")
    
    return output
