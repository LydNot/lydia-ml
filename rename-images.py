#!/usr/bin/env python3
"""
Rename images to simple names and update markdown references
Usage: python3 rename-images.py
"""

import os
import re
from pathlib import Path
from urllib.parse import unquote

def main():
    print("Renaming images to simple names...")
    
    # Create images directory
    images_dir = Path('images')
    images_dir.mkdir(exist_ok=True)
    
    # Get all image files
    image_files = [f for f in os.listdir('.') if f.startswith('https%3A')]
    
    # Rename images to simple names
    image_mapping = {}
    for i, old_name in enumerate(image_files):
        # Extract extension
        if '.' in old_name:
            ext = old_name.split('.')[-1]
        else:
            ext = 'jpg'  # default
        
        new_name = f"image_{i+1:02d}.{ext}"
        
        # Move to images directory
        os.rename(old_name, images_dir / new_name)
        image_mapping[old_name] = new_name
        print(f"  {old_name} -> images/{new_name}")
    
    # Update markdown files
    print("\nUpdating markdown files...")
    markdown_dir = Path('markdown-essays')
    
    for md_file in markdown_dir.glob('*.md'):
        print(f"Processing {md_file.name}...")
        
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace image references
        updated = False
        for old_name, new_name in image_mapping.items():
            old_pattern = f'images/{old_name}'
            new_pattern = f'images/{new_name}'
            
            if old_pattern in content:
                content = content.replace(old_pattern, new_pattern)
                updated = True
        
        if updated:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ Updated image references")
        else:
            print(f"  - No image references found")
    
    print(f"\n✓ Renamed {len(image_files)} images!")
    print("Now run: python3 convert.py")

if __name__ == "__main__":
    main()
