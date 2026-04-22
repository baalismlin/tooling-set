#!/usr/bin/env python3
"""
Tooling Set - Unified CLI entry point for utility tools.

This module provides the main command-line interface for the tooling set package,
routing commands to appropriate tool modules.
"""

import argparse
import sys
from typing import Optional

from tools import (
    escape_tool,
    timestamp_to_human,
    timestamp_to_unix,
    timestamp_now,
    base64_encode,
    base64_decode,
    hash_calculate,
)


def main() -> None:
    """
    Main entry point for the CLI.
    
    Parses command-line arguments and routes to the appropriate tool function.
    """
    parser = argparse.ArgumentParser(
        description='Tooling set - unified CLI for utility tools',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest='command', help='Available tools')
    
    # Escape tool
    escape_parser = subparsers.add_parser(
        'escape',
        help='Escape non-ASCII characters to Unicode escape sequences',
        description='Escape non-ASCII characters in text files to \\uXXXX format'
    )
    escape_parser.add_argument('file', help='Input file path')
    escape_parser.set_defaults(func=escape_tool)
    
    # Timestamp tool
    timestamp_parser = subparsers.add_parser(
        'timestamp',
        help='Timestamp conversion with timezone support',
        description='Convert between Unix timestamps and human-readable datetime formats'
    )
    timestamp_subparsers = timestamp_parser.add_subparsers(
        dest='timestamp_command',
        help='Timestamp commands'
    )
    
    # to-human
    to_human_parser = timestamp_subparsers.add_parser(
        'to-human',
        help='Convert Unix timestamp to human-readable format'
    )
    to_human_parser.add_argument('timestamp', help='Unix timestamp to convert')
    to_human_parser.add_argument(
        'timezone',
        nargs='?',
        default='UTC',
        help='Target timezone (default: UTC)'
    )
    to_human_parser.set_defaults(func=timestamp_to_human)
    
    # to-unix
    to_unix_parser = timestamp_subparsers.add_parser(
        'to-unix',
        help='Convert datetime string to Unix timestamp'
    )
    to_unix_parser.add_argument('datetime', help='Datetime string (e.g., 2024-04-22 12:00:00)')
    to_unix_parser.add_argument(
        'timezone',
        nargs='?',
        default='UTC',
        help='Source timezone (default: UTC)'
    )
    to_unix_parser.set_defaults(func=timestamp_to_unix)
    
    # now
    now_parser = timestamp_subparsers.add_parser(
        'now',
        help='Get current Unix timestamp and human-readable time'
    )
    now_parser.add_argument(
        'timezone',
        nargs='?',
        default='UTC',
        help='Target timezone (default: UTC)'
    )
    now_parser.set_defaults(func=timestamp_now)
    
    # Base64 tool
    base64_parser = subparsers.add_parser(
        'base64',
        help='Base64 encoding and decoding',
        description='Encode or decode text/files to/from Base64 format'
    )
    base64_subparsers = base64_parser.add_subparsers(
        dest='base64_command',
        help='Base64 commands'
    )
    
    # encode
    encode_parser = base64_subparsers.add_parser(
        'encode',
        help='Encode text or file to Base64'
    )
    encode_parser.add_argument('--text', help='Text string to encode')
    encode_parser.add_argument('--file', help='File path to read and encode')
    encode_parser.add_argument('--output', '-o', help='Output file path')
    encode_parser.set_defaults(func=base64_encode)
    
    # decode
    decode_parser = base64_subparsers.add_parser(
        'decode',
        help='Decode Base64 string or file'
    )
    decode_parser.add_argument('--text', help='Base64 string to decode')
    decode_parser.add_argument('--file', help='File path to read and decode')
    decode_parser.add_argument('--output', '-o', help='Output file path')
    decode_parser.set_defaults(func=base64_decode)
    
    # Hash tool
    hash_parser = subparsers.add_parser(
        'hash',
        help='Hash calculation (MD5, SHA1, SHA256)',
        description='Calculate hash of text or file using MD5, SHA1, or SHA256'
    )
    hash_parser.add_argument('algorithm', choices=['md5', 'sha1', 'sha256'], help='Hash algorithm')
    hash_parser.add_argument('--text', help='Text string to hash')
    hash_parser.add_argument('--file', help='File path to read and hash')
    hash_parser.set_defaults(func=hash_calculate)
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    if args.command == 'timestamp' and not args.timestamp_command:
        timestamp_parser.print_help()
        sys.exit(1)
    
    if args.command == 'base64' and not args.base64_command:
        base64_parser.print_help()
        sys.exit(1)
    
    args.func(args)


if __name__ == '__main__':
    main()
