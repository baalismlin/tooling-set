"""
Common utility functions for tool modules.
"""

import sys
from typing import Optional


def read_input(args) -> str:
    """
    Read input from either --text or --file argument.
    
    Args:
        args: Command-line arguments containing:
            - text (str, optional): Text string to read
            - file (str, optional): File path to read
    
    Returns:
        str: The content from text or file
    
    Raises:
        SystemExit: If neither text nor file is provided, or file not found
    """
    if hasattr(args, 'text') and args.text:
        return args.text
    elif hasattr(args, 'file') and args.file:
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: File not found: {args.file}", file=sys.stderr)
            sys.exit(1)
    else:
        print("Error: Either --text or --file must be provided", file=sys.stderr)
        sys.exit(1)


def write_output(content: str, args) -> None:
    """
    Write content to either --output file or stdout.
    
    Args:
        content: Content to write
        args: Command-line arguments containing:
            - output (str, optional): Output file path
    """
    if hasattr(args, 'output') and args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Output written to: {args.output}")
    else:
        print(content)


def handle_error(message: str) -> None:
    """
    Print error message and exit with status 1.
    
    Args:
        message: Error message to print
    """
    print(f"Error: {message}", file=sys.stderr)
    sys.exit(1)
