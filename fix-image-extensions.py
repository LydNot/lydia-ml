#!/usr/bin/env python3
"""
Fix image file extensions in HTML files to match actual files
Usage: python3 fix-image-extensions.py
"""

import re
import os
from pathlib import Path

def main():
    print("Fixing image file extensions in HTML files...")
    
    essays_dir = Path('essays')
    website_essays_dir = Path('website-files/essays')
    
    # Get actual image files
    images_dir = Path('website-files/images')
    actual_files = set()
    if images_dir.exists():
        for file in images_dir.glob('img_*'):
            actual_files.add(file.name)
    
    print(f"Found {len(actual_files)} actual image files")
    
    updated_count = 0
    
    for essays_path in [essays_dir, website_essays_dir]:
        if not essays_path.exists():
            continue
            
        print(f"\nProcessing {essays_path}...")
        
        for html_file in essays_path.glob('*.html'):
            print(f"  Processing {html_file.name}...")
            
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Find all image references
            img_refs = re.findall(r'src="\.\./images/(img_\d+\.\w+)"', content)
            
            for img_ref in img_refs:
                # Extract base name and extension
                base_name = img_ref.split('.')[0]
                current_ext = img_ref.split('.')[1]
                
                # Find the actual file with this base name
                actual_file = None
                for actual in actual_files:
                    if actual.startswith(base_name + '.'):
                        actual_file = actual
                        break
                
                if actual_file and actual_file != img_ref:
                    # Replace the reference with the correct file
                    content = content.replace(f'src="../images/{img_ref}"', f'src="../images/{actual_file}"')
                    print(f"    {img_ref} -> {actual_file}")
            
            if content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"    ✓ Updated image references")
                updated_count += 1
            else:
                print(f"    - No image reference updates needed")
    
    print(f"\n✓ Updated {updated_count} HTML files!")
    print("Image file extensions now match actual files")

if __name__ == "__main__":
    main()
