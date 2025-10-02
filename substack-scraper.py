#!/usr/bin/env python3
"""
Enhanced Substack scraper to get full content and images
Usage: python3 substack-scraper.py
"""

import requests
import xml.etree.ElementTree as ET
from datetime import datetime
import re
import html
from pathlib import Path
import os
from urllib.parse import urljoin, urlparse
import time

def download_image(url, filename, images_dir):
    """Download an image from URL"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        filepath = images_dir / filename
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        print(f"✓ Downloaded: {filename}")
        return filename
    except Exception as e:
        print(f"✗ Failed to download {url}: {e}")
        return None

def scrape_substack_post(url):
    """Scrape full content from a Substack post URL"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        
        # Extract content from HTML
        content = response.text
        
        # Find the main content area (Substack uses specific classes)
        content_match = re.search(r'<div[^>]*class="[^"]*post-content[^"]*"[^>]*>(.*?)</div>', content, re.DOTALL)
        if not content_match:
            # Try alternative selectors
            content_match = re.search(r'<article[^>]*>(.*?)</article>', content, re.DOTALL)
        
        if content_match:
            post_content = content_match.group(1)
            
            # Extract images
            img_pattern = r'<img[^>]*src="([^"]*)"[^>]*>'
            images = re.findall(img_pattern, post_content)
            
            # Clean up HTML and convert to markdown-like format
            # Remove script tags
            post_content = re.sub(r'<script[^>]*>.*?</script>', '', post_content, flags=re.DOTALL)
            
            # Convert images to markdown format
            for img_url in images:
                if img_url.startswith('//'):
                    img_url = 'https:' + img_url
                elif img_url.startswith('/'):
                    img_url = urljoin(url, img_url)
                
                # Generate filename
                parsed_url = urlparse(img_url)
                filename = os.path.basename(parsed_url.path)
                if not filename or '.' not in filename:
                    filename = f"image_{hash(img_url) % 10000}.jpg"
                
                # Replace img tag with markdown
                img_tag = f'<img[^>]*src="{re.escape(img_url)}"[^>]*>'
                markdown_img = f'![{filename}](images/{filename})'
                post_content = re.sub(img_tag, markdown_img, post_content)
            
            # Convert basic HTML to markdown
            post_content = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1\n', post_content)
            post_content = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1\n', post_content)
            post_content = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1\n', post_content)
            post_content = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', post_content)
            post_content = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', post_content)
            post_content = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', post_content)
            post_content = re.sub(r'<br[^>]*>', '\n', post_content)
            post_content = re.sub(r'<[^>]+>', '', post_content)  # Remove remaining HTML tags
            post_content = html.unescape(post_content)  # Convert HTML entities
            
            return post_content.strip(), images
        
        return None, []
        
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None, []

def main():
    print("Enhanced Substack scraper - fetching full content and images...")
    
    # Create images directory
    images_dir = Path('images')
    images_dir.mkdir(exist_ok=True)
    
    # Read existing markdown files to get URLs
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
        
        if full_content and len(full_content) > 50:  # Make sure we got substantial content
            # Download images
            downloaded_images = []
            for img_url in images:
                if img_url.startswith('//'):
                    img_url = 'https:' + img_url
                elif img_url.startswith('/'):
                    img_url = urljoin(source_url, img_url)
                
                parsed_url = urlparse(img_url)
                filename = os.path.basename(parsed_url.path)
                if not filename or '.' not in filename:
                    filename = f"image_{hash(img_url) % 10000}.jpg"
                
                downloaded_filename = download_image(img_url, filename, images_dir)
                if downloaded_filename:
                    downloaded_images.append(downloaded_filename)
            
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
        time.sleep(1)
    
    print(f"\n✓ Updated {updated_count} essays with full content and images!")
    print("Now run: python3 convert.py")

if __name__ == "__main__":
    main()
