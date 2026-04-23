"""
Hash calculation tool for MD5, SHA1, and SHA256.
"""

import argparse
import hashlib
from typing import Optional

from .utils import read_input, handle_error


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
        handle_error(f"Unsupported algorithm: {algorithm}. Supported: md5, sha1, sha256")
    
    content = read_input(args)
    
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
