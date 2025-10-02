#!/usr/bin/env python3
"""
Better Substack scraper with proper image handling
Usage: python3 better-substack-scraper.py
"""

import requests
import re
import os
from pathlib import Path
from urllib.parse import urljoin, urlparse
import time
from bs4 import BeautifulSoup
import html2text

def download_image(url, filename, images_dir):
    """Download an image from URL with proper error handling"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, timeout=15, headers=headers)
        response.raise_for_status()
        
        filepath = images_dir / filename
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        print(f"✓ Downloaded: {filename}")
        return True
    except Exception as e:
        print(f"✗ Failed to download {url}: {e}")
        return False

def scrape_substack_post(url):
    """Scrape full content from a Substack post URL"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the main content area
        content_div = soup.find('div', class_=re.compile(r'post-content|entry-content'))
        if not content_div:
            # Try alternative selectors
            content_div = soup.find('article')
        
        if not content_div:
            print(f"Could not find content area for {url}")
            return None, []
        
        # Extract images
        images = []
        img_tags = content_div.find_all('img')
        
        for i, img in enumerate(img_tags):
            src = img.get('src')
            if src:
                if src.startswith('//'):
                    src = 'https:' + src
                elif src.startswith('/'):
                    src = urljoin(url, src)
                
                # Generate clean filename
                parsed_url = urlparse(src)
                filename = os.path.basename(parsed_url.path)
                if not filename or '.' not in filename:
                    filename = f"image_{i+1:02d}.jpg"
                
                # Clean filename
                filename = re.sub(r'[^a-zA-Z0-9._-]', '_', filename)
                
                images.append({
                    'url': src,
                    'filename': filename,
                    'alt': img.get('alt', '')
                })
        
        # Convert to markdown using html2text
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.ignore_images = False
        h.ignore_tables = False
        h.body_width = 0  # Don't wrap lines
        
        markdown_content = h.handle(str(content_div))
        
        # Clean up the markdown
        markdown_content = re.sub(r'\n\s*\n\s*\n', '\n\n', markdown_content)  # Remove excessive newlines
        markdown_content = markdown_content.strip()
        
        return markdown_content, images
        
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None, []

def main():
    print("Better Substack scraper - fetching full content and images...")
    
    # Create directories
    images_dir = Path('images')
    images_dir.mkdir(exist_ok=True)
    
    markdown_dir = Path('markdown-essays')
    updated_count = 0
    
    for md_file in markdown_dir.glob('*.md'):
        print(f"\nProcessing {md_file.name}...")
        
        # Read the file to get the source URL
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract source URL
        source_match = re.search(r'source: "([^"]*)"', content)
        if not source_match:
            print(f"  No source URL found")
            continue
        
        source_url = source_match.group(1)
        print(f"  Fetching from: {source_url}")
        
        # Scrape the full content
        full_content, images = scrape_substack_post(source_url)
        
        if full_content and len(full_content) > 100:  # Make sure we got substantial content
            # Download images
            downloaded_images = []
            for img_info in images:
                success = download_image(img_info['url'], img_info['filename'], images_dir)
                if success:
                    downloaded_images.append(img_info)
            
            # Update markdown content with proper image references
            for img_info in downloaded_images:
                # Replace any existing image references with the new ones
                old_pattern = rf'!\[.*?\]\([^)]*{re.escape(img_info["filename"])}[^)]*\)'
                new_reference = f'![{img_info["alt"] or "Image"}](images/{img_info["filename"]})'
                full_content = re.sub(old_pattern, new_reference, full_content)
            
            # Update the markdown file with full content
            frontmatter_match = re.search(r'(---.*?---)', content, re.DOTALL)
            if frontmatter_match:
                frontmatter = frontmatter_match.group(1)
                new_content = f"{frontmatter}\n\n{full_content}\n\n---\n\n*Originally published on [Substack]({source_url})*"
                
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print(f"  ✓ Updated with full content ({len(full_content)} chars)")
                if downloaded_images:
                    print(f"  ✓ Downloaded {len(downloaded_images)} images")
                
                updated_count += 1
            else:
                print(f"  ✗ Could not find frontmatter")
        else:
            print(f"  ✗ Could not fetch full content")
        
        # Be respectful to the server
        time.sleep(2)
    
    print(f"\n✓ Updated {updated_count} essays with full content and images!")
    print("Now run: python3 convert.py")

if __name__ == "__main__":
    main()
