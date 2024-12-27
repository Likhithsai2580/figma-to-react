"""React code generation module."""

import os
import json
from typing import Dict, List, Any
from pathlib import Path
import shutil

def create_react_app(output_path: str):
    """Create a React app structure with cyberpunk theme"""
    try:
        # Clean up any existing files
        if os.path.exists(output_path):
            shutil.rmtree(output_path)
        
        # Create directory structure
        os.makedirs(output_path, exist_ok=True)
        os.makedirs(os.path.join(output_path, 'src'), exist_ok=True)
        os.makedirs(os.path.join(output_path, 'public'), exist_ok=True)
        os.makedirs(os.path.join(output_path, 'src', 'components'), exist_ok=True)
        os.makedirs(os.path.join(output_path, 'src', 'assets'), exist_ok=True)
        os.makedirs(os.path.join(output_path, 'src', 'styles'), exist_ok=True)
        
        # Create package.json
        package_json = {
            "name": "jarvis-interface",
            "version": "0.1.0",
            "private": True,
            "type": "module",
            "dependencies": {
                "react": "^18.2.0",
                "react-dom": "^18.2.0",
                "styled-components": "^6.0.7",
                "framer-motion": "^10.16.1",
                "@mui/material": "^5.14.5",
                "@emotion/react": "^11.11.1",
                "@emotion/styled": "^11.11.0"
            },
            "scripts": {
                "dev": "vite",
                "build": "tsc && vite build",
                "serve": "vite preview",
                "lint": "eslint src --ext ts,tsx",
                "format": "prettier --write 'src/**/*.{ts,tsx}'",
                "test": "vitest"
            },
            "devDependencies": {
                "@types/react": "^18.2.21",
                "@types/react-dom": "^18.2.7",
                "@types/styled-components": "^5.1.26",
                "@typescript-eslint/eslint-plugin": "^6.5.0",
                "@typescript-eslint/parser": "^6.5.0",
                "@vitejs/plugin-react": "^4.0.4",
                "eslint": "^8.48.0",
                "prettier": "^3.0.3",
                "typescript": "^5.2.2",
                "vite": "^4.4.9",
                "vitest": "^0.34.3"
            }
        }
        
        with open(os.path.join(output_path, 'package.json'), 'w') as f:
            json.dump(package_json, f, indent=2)
        
        # Create vite.config.ts
        vite_config = """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    open: true
  },
  build: {
    outDir: 'build',
    sourcemap: true
  }
})"""
        
        with open(os.path.join(output_path, 'vite.config.ts'), 'w') as f:
            f.write(vite_config)
        
        # Create tsconfig.json
        tsconfig = {
            "compilerOptions": {
                "target": "ES2020",
                "useDefineForClassFields": True,
                "lib": ["ES2020", "DOM", "DOM.Iterable"],
                "module": "ESNext",
                "skipLibCheck": True,
                "moduleResolution": "bundler",
                "allowImportingTsExtensions": True,
                "resolveJsonModule": True,
                "isolatedModules": True,
                "noEmit": True,
                "jsx": "react-jsx",
                "strict": True,
                "noUnusedLocals": True,
                "noUnusedParameters": True,
                "noFallthroughCasesInSwitch": True
            },
            "include": ["src"],
            "references": [{ "path": "./tsconfig.node.json" }]
        }
        
        with open(os.path.join(output_path, 'tsconfig.json'), 'w') as f:
            json.dump(tsconfig, f, indent=2)
        
        # Create tsconfig.node.json
        tsconfig_node = {
            "compilerOptions": {
                "composite": True,
                "skipLibCheck": True,
                "module": "ESNext",
                "moduleResolution": "bundler",
                "allowSyntheticDefaultImports": True
            },
            "include": ["vite.config.ts"]
        }
        
        with open(os.path.join(output_path, 'tsconfig.node.json'), 'w') as f:
            json.dump(tsconfig_node, f, indent=2)
        
        # Create index.html
        index_html = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>JARVIS Interface</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700&family=Rajdhani:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>"""
        
        with open(os.path.join(output_path, 'index.html'), 'w') as f:
            f.write(index_html)
        
        # Create main.tsx
        main_tsx = """import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './styles/index.css'
import './styles/cyberpunk.css'

// Create particles
const createParticles = () => {
  const particles = document.querySelector('.particles')
  for (let i = 0; i < 50; i++) {
    const particle = document.createElement('div')
    particle.className = 'particle'
    particle.style.left = `${Math.random() * 100}%`
    particle.style.top = `${Math.random() * 100}%`
    particle.style.animationDelay = `${Math.random() * 3}s`
    particles?.appendChild(particle)
  }
}

// Custom cursor
const updateCursor = (e: MouseEvent) => {
  const cursor = document.querySelector('.cursor')
  if (cursor) {
    cursor.setAttribute('style', `top: ${e.pageY - 10}px; left: ${e.pageX - 10}px;`)
  }
}

// Initialize effects
document.addEventListener('DOMContentLoaded', createParticles)
document.addEventListener('mousemove', updateCursor)

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)"""
        
        with open(os.path.join(output_path, 'src', 'main.tsx'), 'w') as f:
            f.write(main_tsx)
        
        # Create App.tsx
        app_tsx = """import React from 'react'
import styled from 'styled-components'
import './styles/index.css'
import './styles/cyberpunk.css'

const AppContainer = styled.div`
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: var(--dark-bg);
  color: var(--neon-blue);
  position: relative;
  overflow: hidden;
`

const App: React.FC = () => {
  return (
    <AppContainer>
      <div className="cyber-grid" />
      <div className="particles" />
      <div className="cursor" />
      <motion.h1
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8 }}
        className="glow"
      >
        JARVIS Interface
      </motion.h1>
      <div className="scan-line" />
    </AppContainer>
  )
}

export default App"""
        
        with open(os.path.join(output_path, 'src', 'App.tsx'), 'w') as f:
            f.write(app_tsx)
        
        # Create styles
        index_css = """
:root {
  --neon-blue: #00f3ff;
  --neon-purple: #9d00ff;
  --neon-pink: #ff00f7;
  --dark-bg: #0a0a0f;
  --grid-color: rgba(0, 243, 255, 0.1);
}

body {
  margin: 0;
  font-family: 'Rajdhani', 'Orbitron', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background-color: var(--dark-bg);
}"""
        
        with open(os.path.join(output_path, 'src', 'styles', 'index.css'), 'w') as f:
            f.write(index_css)
        
        # Create cyberpunk.css
        cyberpunk_css = """
.cyber-grid {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-image: 
    linear-gradient(var(--grid-color) 1px, transparent 1px),
    linear-gradient(90deg, var(--grid-color) 1px, transparent 1px);
  background-size: 30px 30px;
  z-index: -1;
  animation: gridMove 20s linear infinite;
}

@keyframes gridMove {
  from { transform: translateY(0); }
  to { transform: translateY(30px); }
}

.glow {
  text-shadow: 0 0 10px var(--neon-blue),
               0 0 20px var(--neon-blue),
               0 0 30px var(--neon-blue);
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% { opacity: 1; }
  50% { opacity: 0.7; }
  100% { opacity: 1; }
}

.scan-line {
  position: absolute;
  width: 100%;
  height: 2px;
  background: var(--neon-blue);
  opacity: 0.5;
  animation: scan 2s linear infinite;
}

@keyframes scan {
  from { transform: translateY(-100vh); }
  to { transform: translateY(100vh); }
}

.particles {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: -1;
}

.particle {
  position: absolute;
  background: var(--neon-blue);
  width: 2px;
  height: 2px;
  border-radius: 50%;
  animation: float 3s infinite;
}

@keyframes float {
  0% { transform: translateY(0) translateX(0); }
  50% { transform: translateY(-20px) translateX(10px); }
  100% { transform: translateY(0) translateX(0); }
}

.cursor {
  width: 20px;
  height: 20px;
  border: 2px solid var(--neon-blue);
  border-radius: 50%;
  position: fixed;
  pointer-events: none;
  z-index: 9999;
  mix-blend-mode: screen;
  animation: cursorPulse 2s infinite;
}

@keyframes cursorPulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.5); }
  100% { transform: scale(1); }
}"""
        
        with open(os.path.join(output_path, 'src', 'styles', 'cyberpunk.css'), 'w') as f:
            f.write(cyberpunk_css)
        
        return True
    except Exception as e:
        print(f"Error creating React app: {str(e)}")
        return False

def react_code(figma_data: List[Dict[str, Any]], output_path: str = None) -> bool:
    """Generate React components from Figma data"""
    try:
        base_path = output_path if output_path else '.'
        
        # Create React app structure
        if not create_react_app(base_path):
            return False
            
        # Generate components from figma_data
        components_dir = os.path.join(base_path, 'src', 'components')
        os.makedirs(components_dir, exist_ok=True)
        
        for frame_data in figma_data:
            frame_name = frame_data['frame']['name'].replace(' ', '')
            frame_bg = frame_data['frame'].get('backgroundColor', '#ffffff')
            
            # Create frame component
            frame_component = f"""import React from 'react'
import styled from 'styled-components'

const Frame = styled.div`
  position: relative;
  width: 100%;
  height: 100vh;
  background-color: {frame_bg};
  overflow: hidden;
`

const {frame_name}: React.FC = () => {{
  return (
    <Frame>
      {{components.map((comp, index) => (
        <Component key={{{{index}}}} {{...comp}} />
      ))}}
    </Frame>
  )
}}

export default {frame_name}"""
            
            with open(os.path.join(components_dir, f'{frame_name}.tsx'), 'w') as f:
                f.write(frame_component)
            
            # Create components for each element in the frame
            for component in frame_data['components']:
                comp_name = component['name'].replace(' ', '')
                styles = component['style']
                style_string = '\n  '.join([f'{k}: {v};' for k, v in styles.items()])
                
                component_code = f"""import React from 'react'
import styled from 'styled-components'

const Styled{comp_name} = styled.{component['type']}`
  {style_string}
`

const {comp_name}: React.FC = () => {{
  return (
    <Styled{comp_name}>
      {component.get('text', '')}
    </Styled{comp_name}>
  )
}}

export default {comp_name}"""
                
                with open(os.path.join(components_dir, f'{comp_name}.tsx'), 'w') as f:
                    f.write(component_code)
        
        # Update App.tsx to use the generated components
        app_code = """import React from 'react'
import styled from 'styled-components'
import './styles/index.css'
import './styles/cyberpunk.css'
"""

        # Import all frame components
        for frame_data in figma_data:
            frame_name = frame_data['frame']['name'].replace(' ', '')
            app_code += f"import {frame_name} from './components/{frame_name}'\n"

        app_code += """
const AppContainer = styled.div`
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: var(--dark-bg);
  color: var(--neon-blue);
  position: relative;
  overflow: hidden;
`

const App: React.FC = () => {
  return (
    <AppContainer>
      <div className="cyber-grid" />
      <div className="particles" />
      <div className="cursor" />
"""

        # Add all frame components
        for frame_data in figma_data:
            frame_name = frame_data['frame']['name'].replace(' ', '')
            app_code += f"      <{frame_name} />\n"

        app_code += """      <div className="scan-line" />
    </AppContainer>
  )
}

export default App"""

        with open(os.path.join(base_path, 'src', 'App.tsx'), 'w') as f:
            f.write(app_code)
        
        return True
    except Exception as e:
        print(f"Error generating React code: {str(e)}")
        return False 