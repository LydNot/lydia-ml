#!/usr/bin/env python3
"""
Update markdown files to reference renamed images
Usage: python3 update-new-images.py
"""

import re
import os
from pathlib import Path

def main():
    print("Updating image references in markdown files...")
    
    # Get list of images
    images_dir = Path('images')
    image_files = list(images_dir.glob('*'))
    
    markdown_dir = Path('markdown-essays')
    updated_count = 0
    
    for md_file in markdown_dir.glob('*.md'):
        print(f"Processing {md_file.name}...")
        
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all image references in this file
        image_refs = re.findall(r'!\[.*?\]\(images/[^)]+\)', content)
        
        if image_refs:
            print(f"  Found {len(image_refs)} image references")
            
            # Replace each reference with a simple name
            for i, ref in enumerate(image_refs):
                # Extract the filename from the reference
                old_path = re.search(r'images/([^)]+)', ref).group(1)
                
                # Determine file extension
                if '.' in old_path:
                    ext = old_path.split('.')[-1]
                else:
                    ext = 'jpg'
                
                # Create new simple name
                new_name = f"img_{i+1:02d}.{ext}"
                new_ref = ref.replace(old_path, new_name)
                
                # Update the content
                content = content.replace(ref, new_ref)
                print(f"    {old_path} -> {new_name}")
            
            # Write updated content
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"  ✓ Updated {len(image_refs)} references")
            updated_count += 1
        else:
            print(f"  - No image references found")
    
    print(f"\n✓ Updated {updated_count} markdown files!")
    print("Now run: python3 convert.py")

if __name__ == "__main__":
    main()
