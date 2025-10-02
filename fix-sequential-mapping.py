#!/usr/bin/env python3
"""
Fix image mapping by creating a proper sequential mapping
Usage: python3 fix-sequential-mapping.py
"""

import re
import os
import shutil
from pathlib import Path

def main():
    print("Creating proper sequential image mapping...")
    
    markdown_dir = Path('markdown-essays')
    images_dir = Path('images')
    new_images_dir = Path('images-sequential')
    
    # Create new images directory
    new_images_dir.mkdir(exist_ok=True)
    
    # Get all image files and sort them
    all_images = sorted(images_dir.glob('img_*'))
    print(f"Found {len(all_images)} total images")
    
    # Create a global counter for unique naming
    global_counter = 1
    
    for md_file in markdown_dir.glob('*.md'):
        essay_name = md_file.stem
        print(f"Processing {essay_name}...")
        
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all image references in this essay
        img_refs = re.findall(r'images/(img_\d+\.\w+)', content)
        
        if img_refs:
            print(f"  Found {len(img_refs)} image references")
            
            # Create unique names for this essay's images
            new_content = content
            for i, img_ref in enumerate(img_refs):
                # Find the actual file (handle extension mismatches)
                base_name = img_ref.split('.')[0]  # img_01
                ext = img_ref.split('.')[1]        # jpeg
                
                # Look for the actual file (might have different extension)
                actual_file = None
                for img_file in all_images:
                    if img_file.stem == base_name:
                        actual_file = img_file
                        break
                
                if actual_file:
                    # Create unique name: essay_name_img_01.png
                    new_name = f"{essay_name}_img_{i+1:02d}{actual_file.suffix}"
                    new_path = new_images_dir / new_name
                    
                    # Copy the image file with new name
                    shutil.copy2(actual_file, new_path)
                    print(f"    {actual_file.name} -> {new_name}")
                    
                    # Update the markdown content
                    new_content = new_content.replace(f'images/{img_ref}', f'images/{new_name}')
                    global_counter += 1
                else:
                    print(f"    Warning: {img_ref} not found")
            
            # Write updated markdown
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"  ✓ Updated markdown with unique image names")
        else:
            print(f"  No images found")
    
    print(f"\n✓ Created {global_counter-1} unique images in {new_images_dir}")
    print("Now run: python3 convert.py")

if __name__ == "__main__":
    main()
