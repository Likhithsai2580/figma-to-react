"""File utility functions for React generator."""

import os
from pathlib import Path
from typing import Union

def create_directory(path: Union[str, Path]) -> bool:
    """Create a directory if it doesn't exist."""
    try:
        Path(path).mkdir(parents=True, exist_ok=True)
        return True
    except Exception as e:
        print(f"Error creating directory {path}: {str(e)}")
        return False

def write_file(path: Union[str, Path], content: str) -> bool:
    """Write content to a file."""
    try:
        # Ensure the directory exists
        directory = os.path.dirname(path)
        if directory:
            create_directory(directory)
        
        # Write the file
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Error writing file {path}: {str(e)}")
        return False

def read_file(path: Union[str, Path]) -> Union[str, None]:
    """Read content from a file."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading file {path}: {str(e)}")
        return None

def delete_file(path: Union[str, Path]) -> bool:
    """Delete a file if it exists."""
    try:
        if os.path.exists(path):
            os.remove(path)
        return True
    except Exception as e:
        print(f"Error deleting file {path}: {str(e)}")
        return False 