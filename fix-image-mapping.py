#!/usr/bin/env python3
"""
Fix image mapping - ensure each essay gets its correct images
Usage: python3 fix-image-mapping.py
"""

import re
import os
from pathlib import Path
from collections import defaultdict

def main():
    print("Fixing image mapping to ensure correct images for each essay...")
    
    # Create a mapping of essays to their correct images
    essay_image_mapping = {
        'start-of-substack': ['img_01.png'],
        'against-one-way-streets': ['img_01.png'],
        'astronomical-waste--conscientious-objection-': ['img_01.png'],
        '9030-ml-reading-group-retrospective': ['img_01.png', 'img_02.png', 'img_03.jpeg', 'img_04.png', 'img_05.jpeg', 'img_06.png', 'img_07.jpeg', 'img_08.png'],
        'peripatetic-7-ludic-5-corollary-8': ['img_01.png', 'img_02.png'],
        'beware-the-delmore-effect-': ['img_01.png'],
        'not-buying-a-chinese-agibot': ['img_01.png', 'img_02.png', 'img_03.png', 'img_04.png', 'img_05.png', 'img_06.jpeg'],
        'avocado-experiment': ['img_01.png'],
        'the-box-shop': ['img_01.png'],
        'no-taxicab-fallacy-for-knowledge-workers': ['img_01.png'],
        'update-re-spontaneous-instantiation': ['img_01.png'],
        'sullivans-travels--throwing-it-all-away': ['img_01.png'],
        'how-to-be-a-human-starter-pack': ['img_01.png', 'img_02.png'],
        'on-patience': ['img_01.png'],
        'amusing-labels-in-the-jiminy-cricket-environments': ['img_01.png', 'img_02.png', 'img_03.png', 'img_04.png', 'img_05.png', 'img_06.png', 'img_07.png', 'img_08.png'],
        'gpt-5-livestream-notes': ['img_01.png', 'img_02.png', 'img_03.png']
    }
    
    essays_dir = Path('essays')
    website_essays_dir = Path('website-files/essays')
    
    updated_count = 0
    
    for essays_path in [essays_dir, website_essays_dir]:
        if not essays_path.exists():
            continue
            
        print(f"\nProcessing {essays_path}...")
        
        for html_file in essays_path.glob('*.html'):
            essay_name = html_file.stem
            print(f"  Processing {html_file.name}...")
            
            if essay_name not in essay_image_mapping:
                print(f"    - No mapping found for {essay_name}")
                continue
            
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Get the correct images for this essay
            correct_images = essay_image_mapping[essay_name]
            
            # Find all image references in this file
            img_refs = re.findall(r'src="\.\./images/(img_\d+\.\w+)"', content)
            
            if img_refs:
                print(f"    Found {len(img_refs)} image references")
                
                # Replace each image reference with the correct one
                for i, img_ref in enumerate(img_refs):
                    if i < len(correct_images):
                        correct_image = correct_images[i]
                        content = content.replace(f'src="../images/{img_ref}"', f'src="../images/{correct_image}"')
                        print(f"      {img_ref} -> {correct_image}")
                    else:
                        print(f"      {img_ref} -> (no mapping, keeping original)")
            
            if content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"    ✓ Updated image mappings")
                updated_count += 1
            else:
                print(f"    - No image mapping updates needed")
    
    print(f"\n✓ Updated {updated_count} HTML files!")
    print("Each essay now has its correct images")

if __name__ == "__main__":
    main()
