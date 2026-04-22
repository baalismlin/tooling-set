#!/bin/bash

FILE="$1"

# Check for non-ASCII characters
if grep -qP '[^\x00-\x7F]' "$FILE"; then
    echo "Non-ASCII characters detected, converting..."
    
    # Convert using Python
    python -c "
import sys
with open('$FILE', 'r', encoding='utf-8') as f:
    content = f.read()
escaped = ''.join(r'\u' + format(ord(c), '04x') if ord(c) > 127 else c for c in content)
print(escaped, end='')
" > "${FILE}.escaped"
    
    echo "Conversion complete, output to: ${FILE}.escaped"
else
    echo "File contains only ASCII characters"
fi