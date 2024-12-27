# TKForge - Figma to React Converter

A powerful Python tool that converts Figma designs into React components with high fidelity and pixel-perfect accuracy.

## Features

- 🎨 Direct Figma API integration
- ⚛️ Generates modern React components
- 📱 Responsive design support
- 🎯 Maintains design fidelity
- 🖼️ Automatic asset handling
- 🎭 Preserves styles and effects
- 🔄 Component mapping
- 📦 Easy-to-use CLI interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/tkforge.git
cd tkforge
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

4. Install Node.js dependencies:
```bash
npm install
```

## Usage

1. Get your Figma access token from your Figma account settings.

2. Run the converter:
```bash
python tkforge.py <figma_file_url_or_id> <figma_token> [output_path]
```

Example:
```bash
python tkforge.py https://www.figma.com/file/xxxxx/MyDesign your_figma_token ./output
```

3. After conversion, navigate to the generated React app:
```bash
cd reactapp
npm install
npm start
```

## Project Structure

```
tkforge/
├── core.py           # Core conversion logic
├── react.py         # React code generation
├── tk.py            # Tkinter GUI components
├── gui.py           # GUI implementation
├── utils.py         # Utility functions
├── tkforge.py       # CLI entry point
├── requirements.txt # Python dependencies
└── reactapp/        # Generated React application
```

## Requirements

- Python 3.8+
- Node.js 14+
- Figma access token
- Required Python packages (see requirements.txt)

## Development

This project uses several development tools:
- black for code formatting
- mypy for type checking
- pytest for testing
- flake8 for linting
- pre-commit hooks for code quality

To set up the development environment:
```bash
pip install -r requirements.txt
pre-commit install
```

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Figma API team for their excellent documentation
- React community for inspiration and best practices
- All contributors who have helped shape this project

## Support

If you encounter any issues or have questions, please:
1. Check the existing issues
2. Create a new issue with a detailed description
3. Include steps to reproduce the problem