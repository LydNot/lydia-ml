#!/usr/bin/env python3
"""
Create proper image mapping by analyzing original markdown files
Usage: python3 create-proper-image-mapping.py
"""

import re
import os
from pathlib import Path
from collections import defaultdict

def main():
    print("Creating proper image mapping from original markdown files...")
    
    markdown_dir = Path('markdown-essays')
    
    # First, let's see what images each essay actually references
    essay_images = {}
    
    for md_file in markdown_dir.glob('*.md'):
        essay_name = md_file.stem
        print(f"Analyzing {essay_name}...")
        
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all image references in the markdown
        # Look for both the new format and any remaining old format
        img_refs = re.findall(r'images/(img_\d+\.\w+)', content)
        
        if img_refs:
            essay_images[essay_name] = img_refs
            print(f"  Found images: {img_refs}")
        else:
            print(f"  No images found")
    
    print(f"\nEssay image mapping:")
    for essay, images in essay_images.items():
        print(f"  {essay}: {images}")
    
    # Now let's create a mapping file for reference
    with open('image-mapping.txt', 'w') as f:
        f.write("Essay Image Mapping\n")
        f.write("==================\n\n")
        for essay, images in essay_images.items():
            f.write(f"{essay}:\n")
            for img in images:
                f.write(f"  - {img}\n")
            f.write("\n")
    
    print(f"\n✓ Created image-mapping.txt for reference")
    print("This shows which images each essay should have")

if __name__ == "__main__":
    main()
