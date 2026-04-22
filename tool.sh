#!/bin/bash

# Unified CLI entry point for all tools

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TOOLS_DIR="$SCRIPT_DIR/tools"

# Display usage information
show_usage() {
    echo "Usage: tool.sh <tool-name> [arguments...]"
    echo ""
    echo "Available tools:"
    for tool in "$TOOLS_DIR"/*.sh; do
        if [ -f "$tool" ]; then
            tool_name=$(basename "$tool" .sh)
            echo "  $tool_name"
        fi
    done
    echo ""
    echo "Examples:"
    echo "  tool.sh escape filename.txt"
    echo "  tool.sh escape --help"
}

# Check if tools directory exists
if [ ! -d "$TOOLS_DIR" ]; then
    echo "Error: Tools directory not found: $TOOLS_DIR"
    exit 1
fi

# Check if tool name is provided
if [ -z "$1" ]; then
    show_usage
    exit 1
fi

TOOL_NAME="$1"
TOOL_PATH="$TOOLS_DIR/$TOOL_NAME.sh"

# Check if tool exists
if [ ! -f "$TOOL_PATH" ]; then
    echo "Error: Tool '$TOOL_NAME' not found"
    echo ""
    show_usage
    exit 1
fi

# Shift to remove tool name from arguments
shift

# Execute the tool with remaining arguments
bash "$TOOL_PATH" "$@"
