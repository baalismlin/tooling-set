# Tooling Set

A collection of utility tools with a unified Python CLI interface.

## Project Structure

```
tooling-set/
├── tool.py                    # CLI entry point
├── tools/                     # Tool modules
│   ├── __init__.py
│   ├── escape.py            # ASCII character escape tool
│   └── timestamp.py         # Timestamp conversion tool
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

## Usage

### List Available Tools

```bash
python tool.py --help
```

### Run a Specific Tool

```bash
python tool.py <tool-name> [arguments...]
```

### Examples

```bash
# Escape non-ASCII characters in a file
python tool.py escape filename.txt

# Convert Unix timestamp to human-readable
python tool.py timestamp to-human 1713792000

# Get current time
python tool.py timestamp now
```

## Available Tools

### escape

Escapes non-ASCII characters in text files to Unicode escape sequences (`\uXXXX` format).

**Usage:**
```bash
python tool.py escape <filename>
```

**Description:**
- Detects non-ASCII characters in the input file
- Converts them to `\uXXXX` format (e.g., `ü` → `\u00fc`)
- Preserves ASCII characters unchanged
- Outputs to `<filename>.escaped`

**Example:**
```bash
python tool.py escape input.txt
# Creates input.txt.escaped
```

### timestamp

Converts between Unix timestamps and human-readable datetime formats with timezone support.

**Usage:**
```bash
python tool.py timestamp <command> [options]
```

**Commands:**
- `to-human <timestamp> [timezone]` - Convert Unix timestamp to human-readable format
- `to-unix <datetime> [timezone]` - Convert datetime string to Unix timestamp
- `now [timezone]` - Get current Unix timestamp and human-readable time

**Description:**
- Supports timezone specification (default: UTC)
- Handles common datetime formats
- Provides bidirectional conversion

**Examples:**
```bash
# Convert Unix timestamp to human-readable (UTC)
python tool.py timestamp to-human 1713792000

# Convert Unix timestamp to human-readable with timezone
python tool.py timestamp to-human 1713792000 Europe/Berlin

# Convert datetime to Unix timestamp
python tool.py timestamp to-unix '2024-04-22 12:00:00'

# Get current time
python tool.py timestamp now

# Get current time in specific timezone
python tool.py timestamp now Asia/Shanghai
```

## Adding New Tools

1. Create a new module in `tools/` (e.g., `mytool.py`)
2. Implement your tool function with type annotations and docstrings
3. Export the function in `tools/__init__.py`
4. Add the tool to the argparse subparsers in `tool.py`
5. Follow the existing pattern for command-line argument handling

**Example module structure:**
```python
# tools/mytool.py
import argparse
from typing import Any

def mytool_function(args: argparse.Namespace) -> None:
    """
    Tool description.
    
    Args:
        args: Command-line arguments
    """
    # Your implementation here
```

## Requirements

- Python 3.9+

## License

MIT
