# Tooling Set

A collection of utility tools with a unified Python CLI interface.


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

### base64

Encode and decode text or files to/from Base64 format.

**Usage:**
```bash
python tool.py base64 <command> [options]
```

**Commands:**
- `encode` - Encode text or file to Base64
- `decode` - Decode Base64 string or file

**Options:**
- `--text <string>` - Text string to encode/decode
- `--file <path>` - File path to read and encode/decode
- `--output, -o <path>` - Output file path (optional)

**Description:**
- Supports both text string and file input
- Outputs to stdout or file
- Handles UTF-8 encoding

**Examples:**
```bash
# Encode text to Base64
python tool.py base64 encode --text "hello world"
# Output: aGVsbG8gd29ybGQ=

# Decode Base64 string
python tool.py base64 decode --text "aGVsbG8gd29ybGQ="
# Output: hello world

# Encode file to Base64
python tool.py base64 encode --file input.txt

# Decode Base64 file
python tool.py base64 decode --file encoded.b64

# Encode and save to file
python tool.py base64 encode --text "secret" --output encoded.b64

### hash

Calculate hash of text or file using MD5, SHA1, or SHA256 algorithms.

**Usage:**
```bash
python tool.py hash <algorithm> [options]
```

**Algorithms:**
- `md5` - MD5 hash (128-bit)
- `sha1` - SHA1 hash (160-bit)
- `sha256` - SHA256 hash (256-bit)

**Options:**
- `--text <string>` - Text string to hash
- `--file <path>` - File path to read and hash

**Description:**
- Supports MD5, SHA1, and SHA256 algorithms
- Supports both text string and file input
- Outputs hash value as hexadecimal string

**Examples:**
```bash
# Calculate MD5 hash of text
python tool.py hash md5 --text "hello"
# Output: 5d41402abc4b2a76b9719d911017c592

# Calculate SHA1 hash
python tool.py hash sha1 --text "hello"
# Output: aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d

# Calculate SHA256 hash
python tool.py hash sha256 --text "hello"
# Output: 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824

# Calculate hash of file
python tool.py hash md5 --file input.txt
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

# Encode text to Base64
python tool.py base64 encode --text "hello world"

# Decode Base64 string
python tool.py base64 decode --text "aGVsbG8gd29ybGQ="
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
