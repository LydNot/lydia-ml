#!/usr/bin/env python3
"""
Fix image markdown in essays
Usage: python3 fix-images.py
"""

import re
import os
from pathlib import Path
from urllib.parse import unquote

def fix_image_markdown(content):
    """Fix malformed image markdown"""
    # Fix broken image syntax like ![url](images/url)
    # Replace with proper ![alt text](images/filename)
    
    # Pattern to match broken image syntax
    pattern = r'!\[([^\]]*)\](images/[^)]+)'
    
    def replace_image(match):
        alt_text = match.group(1)
        image_path = match.group(2)
        
        # Extract filename from path
        filename = os.path.basename(image_path)
        
        # Decode URL encoding
        decoded_filename = unquote(filename)
        
        # Create proper alt text if it's a URL
        if alt_text.startswith('http'):
            alt_text = "Image"
        
        return f'![{alt_text}](images/{decoded_filename})'
    
    # Fix all image references
    content = re.sub(pattern, replace_image, content)
    
    # Fix concatenated text after images
    # Look for patterns like "![...](images/...)Text without space"
    content = re.sub(r'(!\[.*?\]\(images/[^)]+\))([A-Za-z])', r'\1\n\n\2', content)
    
    return content

def main():
    print("Fixing image markdown in essays...")
    
    markdown_dir = Path('markdown-essays')
    fixed_count = 0
    
    for md_file in markdown_dir.glob('*.md'):
        print(f"Processing {md_file.name}...")
        
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Fix image markdown
        fixed_content = fix_image_markdown(content)
        
        if fixed_content != content:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            print(f"  ✓ Fixed image markdown")
            fixed_count += 1
        else:
            print(f"  - No changes needed")
    
    print(f"\n✓ Fixed {fixed_count} essays!")
    print("Now run: python3 convert.py")

if __name__ == "__main__":
    main()
