"""Cyberpunk styles generation module."""

def generate_cyberpunk_styles():
    return """
:root {
  --neon-blue: #00f3ff;
  --neon-purple: #9d00ff;
  --neon-pink: #ff00f7;
  --dark-bg: #0a0a0f;
  --grid-color: rgba(0, 243, 255, 0.1);
}

body {
  margin: 0;
  background-color: var(--dark-bg);
  color: #fff;
  font-family: 'Rajdhani', 'Orbitron', sans-serif;
  overflow-x: hidden;
}

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
  box-shadow: 0 0 10px var(--neon-blue),
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
  from { transform: translateY(-100%); }
  to { transform: translateY(100%); }
}

.hologram {
  position: relative;
  &::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(
      45deg,
      transparent 0%,
      rgba(0, 243, 255, 0.1) 50%,
      transparent 100%
    );
    animation: hologram 3s linear infinite;
  }
}

@keyframes hologram {
  from { transform: translateX(-100%); }
  to { transform: translateX(100%); }
}

.cyber-cursor {
  cursor: none;
  position: relative;
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
}""" 