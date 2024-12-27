import os
import sys
import threading
from core import parse_file
from react import react_code
from utils import extract_figma_id, has_update

def convert_figma_to_react(file_id: str, token: str, output_path: str = None) -> bool:
    """Convert a Figma design to a React website"""
    try:
        # Parse Figma file
        print("Fetching Figma design...")
        figma_data = parse_file(file_id, token, True, output_path)
        if not figma_data:
            print("Failed to fetch Figma design. Please check your file ID and token.")
            return False
        
        # Generate React code
        print("Generating React website...")
        app_path = os.path.join(output_path if output_path else '.', 'reactapp')
        return react_code(figma_data, app_path)
    except Exception as e:
        print(f"Error converting Figma to React: {str(e)}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python tkforge.py <figma_file_url_or_id> <figma_token> [output_path]")
        sys.exit(1)
    
    file_id = extract_figma_id(sys.argv[1])
    token = sys.argv[2]
    output_path = sys.argv[3] if len(sys.argv) > 3 else None
    
    print("\nFigma to React Converter")
    print("=======================")
    
    if convert_figma_to_react(file_id, token, output_path):
        print("\n✨ Successfully converted Figma design to React website!")
        app_path = os.path.join(output_path if output_path else '.', 'reactapp')
        print(f"📁 Output saved to: {os.path.abspath(app_path)}")
        print("\nTo run the website:")
        print(f"1. cd {app_path}")
        print("2. npm install")
        print("3. npm start")
    else:
        print("\n❌ Failed to convert Figma design to React website.")
