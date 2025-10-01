#!/usr/bin/env python3
"""
Substack RSS to Markdown converter
Usage: python3 substack-import.py https://lydianottingham.substack.com/feed
"""

import requests
import xml.etree.ElementTree as ET
from datetime import datetime
import re
from pathlib import Path
import html

def clean_html_to_markdown(html_content):
    """Basic HTML to Markdown conversion"""
    # Remove HTML tags and convert basic formatting
    text = re.sub(r'<h[1-6][^>]*>(.*?)</h[1-6]>', r'# \1\n', html_content)
    text = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', text)
    text = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', text)
    text = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', text)
    text = re.sub(r'<br[^>]*>', '\n', text)
    text = re.sub(r'<[^>]+>', '', text)  # Remove remaining HTML tags
    text = html.unescape(text)  # Convert HTML entities
    return text.strip()

def parse_substack_rss(rss_url):
    """Parse Substack RSS feed"""
    try:
        response = requests.get(rss_url)
        response.raise_for_status()
        
        root = ET.fromstring(response.content)
        posts = []
        
        for item in root.findall('.//item'):
            title = item.find('title').text if item.find('title') is not None else "Untitled"
            link = item.find('link').text if item.find('link') is not None else ""
            pub_date = item.find('pubDate').text if item.find('pubDate') is not None else ""
            description = item.find('description').text if item.find('description') is not None else ""
            
            # Try to get full content
            content_elem = item.find('.//{http://purl.org/rss/1.0/modules/content/}encoded')
            if content_elem is not None:
                content = content_elem.text
            else:
                content = description
            
            posts.append({
                'title': title,
                'link': link,
                'date': pub_date,
                'content': content
            })
        
        return posts
    
    except Exception as e:
        print(f"Error parsing RSS feed: {e}")
        return []

def convert_to_markdown(post):
    """Convert a post to markdown format"""
    # Parse date
    try:
        date_obj = datetime.strptime(post['date'], '%a, %d %b %Y %H:%M:%S %Z')
        formatted_date = date_obj.strftime('%B %d, %Y')
    except:
        formatted_date = datetime.now().strftime('%B %d, %Y')
    
    # Clean content
    content = clean_html_to_markdown(post['content'])
    
    # Create filename from title
    filename = re.sub(r'[^a-zA-Z0-9\s-]', '', post['title'])
    filename = filename.lower().replace(' ', '-')
    filename = filename[:50]  # Limit length
    
    # Create markdown content
    markdown_content = f"""---
title: "{post['title']}"
date: "{formatted_date}"
category: "technology & society"
source: "{post['link']}"
---

{content}

---

*Originally published on [Substack]({post['link']})*
"""
    
    return filename, markdown_content

def main():
    import sys
    
    if len(sys.argv) > 1:
        substack_url = sys.argv[1]
    else:
        substack_url = input("Enter your Substack RSS URL (e.g., https://lydianottingham.substack.com/feed): ").strip()
    
    if not substack_url:
        print("No URL provided. Exiting.")
        return
    
    print(f"Fetching posts from {substack_url}...")
    posts = parse_substack_rss(substack_url)
    
    if not posts:
        print("No posts found or error occurred.")
        return
    
    print(f"Found {len(posts)} posts. Converting to Markdown...")
    
    # Create markdown-essays directory if it doesn't exist
    Path('markdown-essays').mkdir(exist_ok=True)
    
    converted_count = 0
    for post in posts:
        try:
            filename, markdown_content = convert_to_markdown(post)
            
            # Write to file
            file_path = f"markdown-essays/{filename}.md"
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            
            print(f"✓ Converted: {post['title']}")
            converted_count += 1
            
        except Exception as e:
            print(f"✗ Error converting '{post['title']}': {e}")
    
    print(f"\nSuccessfully converted {converted_count} posts!")
    print("Now run: python3 convert.py")
    print("Then update your index.html with the new essays.")

if __name__ == "__main__":
    main()
