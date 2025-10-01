#!/bin/bash

# Simple script to add a new essay
# Usage: ./new-essay.sh "Essay Title" "category"

if [ $# -lt 2 ]; then
    echo "Usage: $0 \"Essay Title\" \"category\""
    echo "Example: $0 \"My New Essay\" \"personal favorites\""
    exit 1
fi

TITLE="$1"
CATEGORY="$2"
DATE=$(date "+%B %d, %Y")

# Create filename from title (lowercase, replace spaces with hyphens)
FILENAME=$(echo "$TITLE" | tr '[:upper:]' '[:lower:]' | sed 's/ /-/g' | sed 's/[^a-z0-9-]//g')

# Create markdown file
cat > "markdown-essays/$FILENAME.md" << EOF
---
title: "$TITLE"
date: "$DATE"
category: "$CATEGORY"
---

# $TITLE

Write your essay content here...

## Introduction

Start with an engaging introduction that hooks the reader.

## Main Points

Develop your main arguments or ideas here.

### Subheading

Use subheadings to organize your thoughts.

## Conclusion

Wrap up your essay with a strong conclusion.

EOF

echo "Created markdown-essays/$FILENAME.md"
echo "Edit the file and then run: python3 convert.py"
echo "Don't forget to add the link to your index.html!"
