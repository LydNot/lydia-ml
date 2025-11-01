#!/usr/bin/env python3
"""
Fetch images from Substack CDN URLs in markdown files and save them locally
"""

import os
import re
import requests
from pathlib import Path
from urllib.parse import unquote
import time

MARKDOWN_DIR = Path("markdown-essays")
IMAGES_DIR = Path("images")

def download_image(url, local_path):
    """Download an image from URL to local path"""
    try:
        # Handle URL-encoded URLs
        if 'substackcdn.com/image/fetch' in url:
            # Extract the actual image URL from the CDN URL
            match = re.search(r'https%3A%2F%2F[^&\s]+', url)
            if match:
                actual_url = unquote(match.group(0))
                url = actual_url
        
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Create directory if it doesn't exist
        local_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write image to file
        with open(local_path, 'wb') as f:
            f.write(response.content)
        
        return True
    except Exception as e:
        print(f"❌ Error downloading {url}: {e}")
        return False

def process_markdown_file(md_file):
    """Process a markdown file and download images"""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all image URLs that point to Substack CDN
    image_pattern = r'!\[([^\]]*)\]\((https://substackcdn\.com/[^)]+)\)'
    matches = re.findall(image_pattern, content)
    
    if not matches:
        return 0
    
    print(f"\n📄 Processing {md_file.name}...")
    downloaded = 0
    
    for i, (alt_text, url) in enumerate(matches, 1):
        # Skip avatar images
        if 'avatar' in alt_text.lower() or 'w_36' in url:
            continue
        
        # Generate local filename
        base_name = md_file.stem
        # Determine file extension from URL
        if '.png' in url or 'png' in url:
            ext = 'png'
        elif '.webp' in url or 'webp' in url:
            ext = 'webp'
        else:
            ext = 'jpeg'
        
        local_filename = f"{base_name}_img_{i:02d}.{ext}"
        local_path = IMAGES_DIR / local_filename
        
        # Download image if it doesn't exist
        if not local_path.exists():
            print(f"  ⬇️  Downloading image {i}...")
            if download_image(url, local_path):
                print(f"  ✅ Saved to {local_path}")
                downloaded += 1
                time.sleep(0.5)  # Be nice to the server
            else:
                continue
        else:
            print(f"  ⏭️  Image {i} already exists")
        
        # Update markdown content to use local path
        new_image_ref = f"![{alt_text}](images/{local_filename})"
        old_image_ref = f"![{alt_text}]({url})"
        content = content.replace(old_image_ref, new_image_ref)
    
    # Write updated content back to file if changes were made
    if downloaded > 0:
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  💾 Updated {md_file.name}")
    
    return downloaded

def main():
    """Main function"""
    print("🖼️  Fetching images from markdown files...")
    
    # Ensure directories exist
    IMAGES_DIR.mkdir(exist_ok=True)
    
    if not MARKDOWN_DIR.exists():
        print("❌ markdown-essays directory not found")
        return
    
    total_downloaded = 0
    
    # Process all markdown files
    for md_file in sorted(MARKDOWN_DIR.glob("*.md")):
        downloaded = process_markdown_file(md_file)
        total_downloaded += downloaded
    
    if total_downloaded > 0:
        print(f"\n🎉 Downloaded {total_downloaded} new image(s)!")
    else:
        print("\n✨ All images are already downloaded")

if __name__ == "__main__":
    main()
