#!/usr/bin/env python3
"""
Fetch preview images for existing markdown posts that have Substack source URLs
"""

import re
import requests
from pathlib import Path
from bs4 import BeautifulSoup

MARKDOWN_DIR = Path("markdown-essays")

def extract_preview_image(url):
    """Fetch preview image from a Substack URL"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Try og:image meta tag first (most reliable)
        og_image = soup.find('meta', property='og:image')
        if og_image and og_image.get('content'):
            return og_image['content']
        
        # Try twitter:image as fallback
        twitter_image = soup.find('meta', attrs={'name': 'twitter:image'})
        if twitter_image and twitter_image.get('content'):
            return twitter_image['content']
        
        return None
        
    except Exception as e:
        print(f"❌ Error fetching {url}: {e}")
        return None

def update_markdown_file(filepath):
    """Update a markdown file to include preview_image in frontmatter"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if it already has a preview_image
    if 'preview_image:' in content:
        return False, "Already has preview image"
    
    # Extract frontmatter
    if not content.startswith('---'):
        return False, "No frontmatter found"
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False, "Invalid frontmatter"
    
    frontmatter_text = parts[1]
    rest_of_content = parts[2]
    
    # Extract source URL
    source_match = re.search(r'source:\s*"([^"]+)"', frontmatter_text)
    if not source_match:
        return False, "No source URL found"
    
    source_url = source_match.group(1)
    
    # Fetch preview image
    print(f"  Fetching preview image from {source_url[:50]}...")
    preview_image = extract_preview_image(source_url)
    
    if not preview_image:
        return False, "No preview image found"
    
    # Add preview_image to frontmatter (before the closing ---)
    new_frontmatter = frontmatter_text.rstrip() + f'\npreview_image: "{preview_image}"\n'
    new_content = f"---{new_frontmatter}---{rest_of_content}"
    
    # Write back to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True, preview_image

def main():
    """Main function to update all markdown files"""
    print("🖼️  Fetching preview images for existing posts...\n")
    
    updated_count = 0
    skipped_count = 0
    
    for md_file in sorted(MARKDOWN_DIR.glob('*.md')):
        print(f"📝 Processing: {md_file.name}")
        success, result = update_markdown_file(md_file)
        
        if success:
            print(f"   ✅ Added preview image")
            updated_count += 1
        else:
            print(f"   ⏭️  Skipped: {result}")
            skipped_count += 1
        print()
    
    print(f"\n{'='*50}")
    print(f"✅ Updated: {updated_count} files")
    print(f"⏭️  Skipped: {skipped_count} files")
    
    if updated_count > 0:
        print(f"\n💡 Run 'python3 convert.py' to regenerate JSON files with the new images")

if __name__ == "__main__":
    main()

