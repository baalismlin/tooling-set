# Tooling Set

A collection of utility scripts with a unified CLI interface.

## Project Structure

```
tooling-set/
├── tool.sh           # Unified CLI entry point
├── tools/            # Individual tool scripts
│   └── escape.sh     # ASCII character escape tool
└── README.md         # This file
```

## Usage

### List Available Tools

```bash
./tool.sh
```

### Run a Specific Tool

```bash
./tool.sh <tool-name> [arguments...]
```

### Examples

```bash
# Escape non-ASCII characters in a file
./tool.sh escape filename.txt

# The tool will create filename.txt.escaped with Unicode escape sequences
```

## Available Tools

### escape

Escapes non-ASCII characters in text files to Unicode escape sequences (`\uXXXX` format).

**Usage:**
```bash
./tool.sh escape <filename>
```

**Description:**
- Detects non-ASCII characters in the input file
- Converts them to `\uXXXX` format (e.g., `ü` → `\u00fc`)
- Preserves ASCII characters unchanged
- Outputs to `<filename>.escaped`

**Example:**
```bash
./tool.sh escape input.txt
# Creates input.txt.escaped
```

## Adding New Tools

1. Create a new bash script in the `tools/` directory
2. Name it `<tool-name>.sh`
3. Make it executable: `chmod +x tools/<tool-name>.sh`
4. The tool will be automatically available via the CLI

## Requirements

- Bash (Git Bash, WSL, or similar on Windows)
- Python 3 (required by some tools)

## License

MIT
