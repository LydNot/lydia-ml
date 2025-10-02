#!/usr/bin/env python3
"""
Replace Substack image URLs with local image references
Usage: python3 fix-substack-images.py
"""

import re
import os
from pathlib import Path

def main():
    print("Replacing Substack image URLs with local references...")
    
    markdown_dir = Path('markdown-essays')
    updated_count = 0
    
    for md_file in markdown_dir.glob('*.md'):
        print(f"Processing {md_file.name}...")
        
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all Substack image URLs
        substack_images = re.findall(r'https://substack-post-media\.s3\.amazonaws\.com/public/images/[^)]+', content)
        
        if substack_images:
            print(f"  Found {len(substack_images)} Substack image URLs")
            
            # Replace each URL with a local reference
            for i, url in enumerate(substack_images):
                # Extract filename from URL
                filename = url.split('/')[-1]
                
                # Determine file extension
                if '.' in filename:
                    ext = filename.split('.')[-1]
                else:
                    ext = 'jpg'
                
                # Create new simple name
                new_name = f"img_{i+1:02d}.{ext}"
                new_ref = f"images/{new_name}"
                
                # Replace the URL in the content
                content = content.replace(url, new_ref)
                print(f"    {filename} -> {new_name}")
            
            # Write updated content
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"  ✓ Updated {len(substack_images)} image references")
            updated_count += 1
        else:
            print(f"  - No Substack image URLs found")
    
    print(f"\n✓ Updated {updated_count} markdown files!")
    print("Now run: python3 convert.py")

if __name__ == "__main__":
    main()
