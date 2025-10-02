#!/usr/bin/env python3
"""
Remove buggy author section from HTML files
Usage: python3 remove-author-section.py
"""

import re
import os
from pathlib import Path

def main():
    print("Removing buggy author section from HTML files...")
    
    essays_dir = Path('essays')
    website_essays_dir = Path('website-files/essays')
    
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
            
            # Remove the buggy author section
            # This pattern matches the section with avatar, name, date, and share button
            author_pattern = r'<p><a href="https://substack\.com/@lydianottingham"><img alt="[^"]*" src="/images/[^"]*" /></a></p>\s*<p><a href="https://substack\.com/@lydianottingham">Lydia Nottingham</a></p>\s*<p>[^<]*</p>\s*<p>\d+</p>\s*<p>\d+</p>\s*<p><a href="[^"]*">Share</a></p>'
            
            content = re.sub(author_pattern, '', content, flags=re.MULTILINE | re.DOTALL)
            
            # Also remove any standalone avatar images
            avatar_pattern = r'<p><a href="https://substack\.com/@lydianottingham"><img alt="[^"]*" src="/images/[^"]*" /></a></p>'
            content = re.sub(avatar_pattern, '', content)
            
            # Remove any standalone "Lydia Nottingham" links
            name_pattern = r'<p><a href="https://substack\.com/@lydianottingham">Lydia Nottingham</a></p>'
            content = re.sub(name_pattern, '', content)
            
            # Remove any standalone share links
            share_pattern = r'<p><a href="[^"]*">Share</a></p>'
            content = re.sub(share_pattern, '', content)
            
            # Clean up any extra whitespace
            content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
            
            if content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"    ✓ Removed author section")
                updated_count += 1
            else:
                print(f"    - No author section found")
    
    print(f"\n✓ Updated {updated_count} HTML files!")
    print("Buggy author sections removed")

if __name__ == "__main__":
    main()
