"""
Hash calculation tool for MD5, SHA1, and SHA256.
"""

import argparse
import hashlib
import sys
from typing import Optional


def hash_calculate(args: argparse.Namespace) -> None:
    """
    Calculate hash of text or file content.
    
    Supports MD5, SHA1, and SHA256 algorithms.
    
    Args:
        args: Command-line arguments containing:
            - algorithm (str): Hash algorithm (md5, sha1, sha256)
            - text (str, optional): Text string to hash
            - file (str, optional): File path to read and hash
    
    Raises:
        SystemExit: If neither text nor file is provided, file not found, or invalid algorithm
    
    Example:
        >>> args = argparse.Namespace(algorithm='md5', text='hello', file=None)
        >>> hash_calculate(args)
        5d41402abc4b2a76b9719d911017c592
    """
    algorithm = args.algorithm.lower()
    
    if algorithm not in ['md5', 'sha1', 'sha256']:
        print(f"Error: Unsupported algorithm: {algorithm}", file=sys.stderr)
        print("Supported algorithms: md5, sha1, sha256", file=sys.stderr)
        sys.exit(1)
    
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
    
    # Calculate hash
    if algorithm == 'md5':
        hash_obj = hashlib.md5()
    elif algorithm == 'sha1':
        hash_obj = hashlib.sha1()
    else:  # sha256
        hash_obj = hashlib.sha256()
    
    hash_obj.update(content.encode('utf-8'))
    hash_value = hash_obj.hexdigest()
    
    print(hash_value)
