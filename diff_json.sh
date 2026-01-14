#!/bin/bash

for file in recipes/*.json; do
    base=$(basename "$file")
    other="non-researched/$base"
    if [ -f "$other" ]; then
        if ! diff -q "$file" "$other" > /dev/null; then
            echo "$base is different"
        fi
    fi
done
