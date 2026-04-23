"""
Base64 encoding and decoding tool.
"""

import argparse
import base64
from typing import Optional

from .utils import read_input, write_output, handle_error


def base64_encode(args: argparse.Namespace) -> None:
    """
    Encode text or file content to Base64.
    
    Args:
        args: Command-line arguments containing:
            - text (str, optional): Text string to encode
            - file (str, optional): File path to read and encode
            - output (str, optional): Output file path
    
    Raises:
        SystemExit: If neither text nor file is provided, or file not found
    
    Example:
        >>> args = argparse.Namespace(text='hello', file=None, output=None)
        >>> base64_encode(args)
        aGVsbG8=
    """
    content = read_input(args)
    
    # Encode to base64
    encoded = base64.b64encode(content.encode('utf-8')).decode('ascii')
    
    write_output(encoded, args)


def base64_decode(args: argparse.Namespace) -> None:
    """
    Decode Base64 string or file content.
    
    Args:
        args: Command-line arguments containing:
            - text (str, optional): Base64 string to decode
            - file (str, optional): File path to read and decode
            - output (str, optional): Output file path
    
    Raises:
        SystemExit: If neither text nor file is provided, file not found, or invalid base64
    
    Example:
        >>> args = argparse.Namespace(text='aGVsbG8=', file=None, output=None)
        >>> base64_decode(args)
        hello
    """
    content = read_input(args)
    
    try:
        decoded = base64.b64decode(content.encode('ascii')).decode('utf-8')
    except Exception as e:
        handle_error(f"Invalid Base64 input - {e}")
    
    write_output(decoded, args)
