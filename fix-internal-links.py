#!/usr/bin/env python3
"""
Fix internal links to point to local HTML files instead of Substack
Usage: python3 fix-internal-links.py
"""

import re
import os
from pathlib import Path

def main():
    print("Fixing internal links to point to local HTML files...")
    
    essays_dir = Path('essays')
    website_essays_dir = Path('website-files/essays')
    
    # Create mapping of Substack URLs to local HTML files
    url_mapping = {
        'https://lydianottingham.substack.com/p/9030-ml-reading-group-retrospective': '9030-ml-reading-group-retrospective.html',
        'https://lydianottingham.substack.com/p/against-one-way-street-hypervigilance': 'against-one-way-streets.html',
        'https://lydianottingham.substack.com/p/astronomical-waste-and-conscientious': 'astronomical-waste--conscientious-objection-.html',
        'https://lydianottingham.substack.com/p/beware-the-delmore-effect': 'beware-the-delmore-effect-.html',
        'https://lydianottingham.substack.com/p/not-buying-a-chinese-agibot': 'not-buying-a-chinese-agibot.html',
        'https://lydianottingham.substack.com/p/avocado-experiment': 'avocado-experiment.html',
        'https://lydianottingham.substack.com/p/the-box-shop': 'the-box-shop.html',
        'https://lydianottingham.substack.com/p/no-taxicab-fallacy-for-knowledge': 'no-taxicab-fallacy-for-knowledge-workers.html',
        'https://lydianottingham.substack.com/p/update-re-spontaneous-instantiation': 'update-re-spontaneous-instantiation.html',
        'https://lydianottingham.substack.com/p/sullivans-travels-and-throwing-it': 'sullivans-travels--throwing-it-all-away.html',
        'https://lydianottingham.substack.com/p/how-to-be-a-human-starter-pack': 'how-to-be-a-human-starter-pack.html',
        'https://lydianottingham.substack.com/p/patience': 'on-patience.html',
        'https://lydianottingham.substack.com/p/amusing-labels-in-the-jiminy-cricket': 'amusing-labels-in-the-jiminy-cricket-environments.html',
        'https://lydianottingham.substack.com/p/gpt-5-livestream-notes': 'gpt-5-livestream-notes.html',
        'https://lydianottingham.substack.com/p/start-of-substack': 'start-of-substack.html',
        'https://lydianottingham.substack.com/p/peripatetic-7-ludic-5-corollary-8': 'peripatetic-7-ludic-5-corollary-8.html',
    }
    
    updated_count = 0
    
    for essays_path in [essays_dir, website_essays_dir]:
        if not essays_path.exists():
            continue
            
        print(f"\nProcessing {essays_path}...")
        
        for html_file in essays_path.glob('*.html'):
            print(f"  Processing {html_file.name}...")
            
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace internal essay links
            original_content = content
            for substack_url, local_file in url_mapping.items():
                # Replace links to other essays
                pattern = f'href="{re.escape(substack_url)}"'
                replacement = f'href="{local_file}"'
                content = re.sub(pattern, replacement, content)
            
            # Remove Substack author links (keep the text but remove the link)
            content = re.sub(r'<a href="https://substack\.com/@lydianottingham">([^<]+)</a>', r'\1', content)
            
            # Remove Substack avatar links (keep the image but remove the link)
            content = re.sub(r'<a href="https://substack\.com/@lydianottingham">(<img[^>]+>)</a>', r'\1', content)
            
            # Remove comment links (keep the number but remove the link)
            content = re.sub(r'<a href="https://lydianottingham\.substack\.com/p/[^"]+/comments">(\d+)</a>', r'\1', content)
            
            if content != original_content:
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"    ✓ Updated internal links")
                updated_count += 1
            else:
                print(f"    - No internal links found")
    
    print(f"\n✓ Updated {updated_count} HTML files!")
    print("Internal links now point to local HTML files instead of Substack")

if __name__ == "__main__":
    main()
