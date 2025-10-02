#!/usr/bin/env python3
"""
Create unique image names for each essay to avoid conflicts
Usage: python3 create-unique-images.py
"""

import re
import os
import shutil
from pathlib import Path

def main():
    print("Creating unique image names for each essay...")
    
    markdown_dir = Path('markdown-essays')
    images_dir = Path('images')
    new_images_dir = Path('images-unique')
    
    # Create new images directory
    new_images_dir.mkdir(exist_ok=True)
    
    essay_counter = 1
    
    for md_file in markdown_dir.glob('*.md'):
        essay_name = md_file.stem
        print(f"Processing {essay_name}...")
        
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all image references in this essay
        img_refs = re.findall(r'images/(img_\d+\.\w+)', content)
        
        if img_refs:
            print(f"  Found {len(img_refs)} images")
            
            # Create unique names for this essay's images
            new_content = content
            for i, img_ref in enumerate(img_refs):
                # Create unique name: essay_name_img_01.png
                base_name = img_ref.split('.')[0]  # img_01
                ext = img_ref.split('.')[1]        # png
                new_name = f"{essay_name}_img_{i+1:02d}.{ext}"
                
                # Copy the image file with new name
                old_path = images_dir / img_ref
                new_path = new_images_dir / new_name
                
                if old_path.exists():
                    shutil.copy2(old_path, new_path)
                    print(f"    {img_ref} -> {new_name}")
                    
                    # Update the markdown content
                    new_content = new_content.replace(f'images/{img_ref}', f'images/{new_name}')
                else:
                    print(f"    Warning: {img_ref} not found")
            
            # Write updated markdown
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"  ✓ Updated markdown with unique image names")
        else:
            print(f"  No images found")
    
    print(f"\n✓ Created unique images in {new_images_dir}")
    print("Now run: python3 convert.py")

if __name__ == "__main__":
    main()
