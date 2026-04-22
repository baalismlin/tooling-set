"""
Base64 encoding and decoding tool.
"""

import argparse
import base64
import sys
from typing import Optional


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
    if args.text:
        content = args.text
    elif args.file:
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            print(f"Error: File not found: {args.file}", file=sys.stderr)
            sys.exit(1)
    else:
        print("Error: Either --text or --file must be provided", file=sys.stderr)
        sys.exit(1)
    
    # Encode to base64
    encoded = base64.b64encode(content.encode('utf-8')).decode('ascii')
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(encoded)
        print(f"Encoded content written to: {args.output}")
    else:
        print(encoded)


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
    if args.text:
        content = args.text
    elif args.file:
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            print(f"Error: File not found: {args.file}", file=sys.stderr)
            sys.exit(1)
    else:
        print("Error: Either --text or --file must be provided", file=sys.stderr)
        sys.exit(1)
    
    try:
        decoded = base64.b64decode(content.encode('ascii')).decode('utf-8')
    except Exception as e:
        print(f"Error: Invalid Base64 input - {e}", file=sys.stderr)
        sys.exit(1)
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(decoded)
        print(f"Decoded content written to: {args.output}")
    else:
        print(decoded)
