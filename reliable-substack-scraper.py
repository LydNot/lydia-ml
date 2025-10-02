#!/usr/bin/env python3
"""
Simple, reliable Substack scraper with proper image mapping
Usage: python3 reliable-substack-scraper.py
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

def scrape_substack_post(url, essay_name):
    """Scrape full content from a Substack post URL with proper image mapping"""
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
        
        # Extract images with proper mapping
        images = []
        img_tags = content_div.find_all('img')
        
        for i, img in enumerate(img_tags):
            src = img.get('src')
            if src:
                if src.startswith('//'):
                    src = 'https:' + src
                elif src.startswith('/'):
                    src = urljoin(url, src)
                
                # Create unique filename for this essay
                parsed_url = urlparse(src)
                original_filename = os.path.basename(parsed_url.path)
                
                # Generate clean, unique filename
                if '.' in original_filename:
                    ext = original_filename.split('.')[-1]
                else:
                    ext = 'jpg'
                
                # Create unique name: essay_name_img_01.ext
                filename = f"{essay_name}_img_{i+1:02d}.{ext}"
                
                images.append({
                    'url': src,
                    'filename': filename,
                    'alt': img.get('alt', ''),
                    'original_src': src
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
    print("Reliable Substack scraper - fetching content with proper image mapping...")
    
    # Create directories
    images_dir = Path('images-clean')
    images_dir.mkdir(exist_ok=True)
    
    markdown_dir = Path('markdown-essays')
    
    # List of essays to scrape
    essays = [
        ('start-of-substack', 'https://lydianottingham.substack.com/p/start-of-substack'),
        ('against-one-way-streets', 'https://lydianottingham.substack.com/p/against-one-way-street-hypervigilance'),
        ('astronomical-waste--conscientious-objection-', 'https://lydianottingham.substack.com/p/astronomical-waste-and-conscientious'),
        ('9030-ml-reading-group-retrospective', 'https://lydianottingham.substack.com/p/9030-ml-reading-group-retrospective'),
        ('peripatetic-7-ludic-5-corollary-8', 'https://lydianottingham.substack.com/p/peripatetic-7-ludic-5-corollary-8'),
        ('beware-the-delmore-effect-', 'https://lydianottingham.substack.com/p/beware-the-delmore-effect'),
        ('not-buying-a-chinese-agibot', 'https://lydianottingham.substack.com/p/not-buying-a-chinese-agibot'),
        ('avocado-experiment', 'https://lydianottingham.substack.com/p/avocado-experiment'),
        ('the-box-shop', 'https://lydianottingham.substack.com/p/the-box-shop'),
        ('no-taxicab-fallacy-for-knowledge-workers', 'https://lydianottingham.substack.com/p/no-taxicab-fallacy-for-knowledge'),
        ('update-re-spontaneous-instantiation', 'https://lydianottingham.substack.com/p/update-re-spontaneous-instantiation'),
        ('sullivans-travels--throwing-it-all-away', 'https://lydianottingham.substack.com/p/sullivans-travels-and-throwing-it'),
        ('how-to-be-a-human-starter-pack', 'https://lydianottingham.substack.com/p/how-to-be-a-human-starter-pack'),
        ('on-patience', 'https://lydianottingham.substack.com/p/patience'),
        ('amusing-labels-in-the-jiminy-cricket-environments', 'https://lydianottingham.substack.com/p/amusing-labels-in-the-jiminy-cricket'),
        ('gpt-5-livestream-notes', 'https://lydianottingham.substack.com/p/gpt-5-livestream-notes')
    ]
    
    updated_count = 0
    
    for essay_name, url in essays:
        print(f"\nProcessing {essay_name}...")
        print(f"  URL: {url}")
        
        # Scrape the full content
        full_content, images = scrape_substack_post(url, essay_name)
        
        if full_content and len(full_content) > 100:  # Make sure we got substantial content
            print(f"  Found {len(images)} images")
            
            # Download images
            downloaded_images = []
            for img_info in images:
                success = download_image(img_info['url'], img_info['filename'], images_dir)
                if success:
                    downloaded_images.append(img_info)
            
            # Update markdown content with proper image references
            for img_info in downloaded_images:
                # Replace the original image reference with our local one
                old_pattern = rf'!\[.*?\]\({re.escape(img_info["original_src"])}\)'
                new_reference = f'![{img_info["alt"] or "Image"}](images/{img_info["filename"]})'
                full_content = re.sub(old_pattern, new_reference, full_content)
            
            # Create/update the markdown file
            md_file = markdown_dir / f"{essay_name}.md"
            
            # Read existing frontmatter if it exists
            frontmatter = ""
            if md_file.exists():
                with open(md_file, 'r', encoding='utf-8') as f:
                    existing_content = f.read()
                    frontmatter_match = re.search(r'(---.*?---)', existing_content, re.DOTALL)
                    if frontmatter_match:
                        frontmatter = frontmatter_match.group(1)
            
            # Write new content with frontmatter
            new_content = f"{frontmatter}\n\n{full_content}\n\n---\n\n*Originally published on [Substack]({url})*"
            
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"  ✓ Updated with full content ({len(full_content)} chars)")
            if downloaded_images:
                print(f"  ✓ Downloaded {len(downloaded_images)} images")
            
            updated_count += 1
        else:
            print(f"  ✗ Could not fetch full content")
        
        # Be respectful to the server
        time.sleep(2)
    
    print(f"\n✓ Updated {updated_count} essays with full content and properly mapped images!")
    print("Now run: python3 convert.py")

if __name__ == "__main__":
    main()
