"""
Timestamp conversion tool with timezone support.
"""

import argparse
import sys
from datetime import datetime, timezone
from typing import Optional
import zoneinfo


def get_timezone(tz_str: Optional[str]) -> timezone:
    """
    Get timezone object from string.
    
    Args:
        tz_str: Timezone string (e.g., 'UTC', 'Europe/Berlin', 'Asia/Shanghai')
                If None or 'UTC', returns UTC timezone.
    
    Returns:
        timezone: Python timezone object
    
    Raises:
        SystemExit: If timezone is unknown
    
    Example:
        >>> tz = get_timezone('Europe/Berlin')
        >>> str(tz)
        'Europe/Berlin'
    """
    if not tz_str or tz_str.upper() == 'UTC':
        return timezone.utc
    try:
        return zoneinfo.ZoneInfo(tz_str)
    except:
        print(f"Error: Unknown timezone: {tz_str}", file=sys.stderr)
        sys.exit(1)


def timestamp_to_human(args: argparse.Namespace) -> None:
    """
    Convert Unix timestamp to human-readable format.
    
    Args:
        args: Command-line arguments containing:
            - timestamp (str): Unix timestamp to convert
            - timezone (str): Target timezone (default: UTC)
    
    Raises:
        SystemExit: If timestamp is invalid
    
    Example:
        >>> args = argparse.Namespace(timestamp='1713792000', timezone='UTC')
        >>> timestamp_to_human(args)
        2024-04-22 12:00:00 UTC
        Unix timestamp: 1713792000.0
    """
    try:
        timestamp = float(args.timestamp)
    except ValueError:
        print("Error: Invalid timestamp", file=sys.stderr)
        sys.exit(1)
    
    tz = get_timezone(args.timezone)
    dt = datetime.fromtimestamp(timestamp, tz=tz)
    print(dt.strftime('%Y-%m-%d %H:%M:%S %Z'))
    print(f'Unix timestamp: {timestamp}')


def timestamp_to_unix(args: argparse.Namespace) -> None:
    """
    Convert datetime string to Unix timestamp.
    
    Supports common datetime formats:
    - YYYY-MM-DD HH:MM:SS
    - YYYY-MM-DD HH:MM
    - YYYY-MM-DD
    - YYYY/MM/DD HH:MM:SS
    - YYYY/MM/DD HH:MM
    - YYYY/MM/DD
    
    Args:
        args: Command-line arguments containing:
            - datetime (str): Datetime string to convert
            - timezone (str): Source timezone (default: UTC)
    
    Raises:
        SystemExit: If datetime string cannot be parsed
    
    Example:
        >>> args = argparse.Namespace(datetime='2024-04-22 12:00:00', timezone='UTC')
        >>> timestamp_to_unix(args)
        Unix timestamp: 1713792000.0
        2024-04-22 12:00:00 UTC
    """
    datetime_str = args.datetime
    tz = get_timezone(args.timezone)
    
    # Try common formats
    formats = [
        '%Y-%m-%d %H:%M:%S',
        '%Y-%m-%d %H:%M',
        '%Y-%m-%d',
        '%Y/%m/%d %H:%M:%S',
        '%Y/%m/%d %H:%M',
        '%Y/%m/%d',
    ]
    
    dt = None
    for fmt in formats:
        try:
            dt = datetime.strptime(datetime_str, fmt)
            break
        except ValueError:
            continue
    
    if not dt:
        print('Error: Unable to parse datetime. Try format: YYYY-MM-DD HH:MM:SS', file=sys.stderr)
        sys.exit(1)
    
    dt = dt.replace(tzinfo=tz)
    timestamp = dt.timestamp()
    print(f'Unix timestamp: {timestamp}')
    fmt = '%Y-%m-%d %H:%M:%S %Z'
    print(f'{dt.strftime(fmt)}')


def timestamp_now(args: argparse.Namespace) -> None:
    """
    Get current Unix timestamp and human-readable time.
    
    Args:
        args: Command-line arguments containing:
            - timezone (str): Target timezone (default: UTC)
    
    Example:
        >>> args = argparse.Namespace(timezone='UTC')
        >>> timestamp_now(args)
        Current time: 2024-04-22 13:00:00 UTC
        Unix timestamp: 1713795600.0
    """
    tz = get_timezone(args.timezone)
    now = datetime.now(tz=tz)
    timestamp = now.timestamp()
    fmt = '%Y-%m-%d %H:%M:%S %Z'
    print(f'Current time: {now.strftime(fmt)}')
    print(f'Unix timestamp: {timestamp}')
