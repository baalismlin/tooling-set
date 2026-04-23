"""
Escape tool for converting non-ASCII characters to Unicode escape sequences.
"""

import argparse
from typing import Any

from .utils import handle_error


def escape_tool(args: argparse.Namespace) -> None:
    """
    Escape non-ASCII characters in a text file to Unicode escape sequences.
    
    This tool reads a text file, detects non-ASCII characters, and converts them
    to \\uXXXX format (e.g., 'ü' → '\\u00fc') while preserving ASCII characters unchanged.
    The output is written to a new file with the '.escaped' suffix.
    
    Args:
        args: Command-line arguments containing:
            - file (str): Path to the input file to process
    
    Raises:
        FileNotFoundError: If the input file does not exist
        Exception: For other file processing errors
    
    Example:
        >>> args = argparse.Namespace(file='input.txt')
        >>> escape_tool(args)
        Non-ASCII characters detected, converting...
        Conversion complete, output to: input.txt.escaped
    """
    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for non-ASCII characters
        if any(ord(c) > 127 for c in content):
            print("Non-ASCII characters detected, converting...")
            
            # Convert to \uXXXX format
            escaped = ''.join(
                r'\u' + format(ord(c), '04x') if ord(c) > 127 else c 
                for c in content
            )
            
            output_file = args.file + '.escaped'
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(escaped)
            
            print(f"Conversion complete, output to: {output_file}")
        else:
            print("File contains only ASCII characters")
    
    except FileNotFoundError:
        handle_error(f"File not found: {args.file}")
    except Exception as e:
        handle_error(str(e))
