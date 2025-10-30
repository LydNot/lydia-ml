#!/usr/bin/env python3
"""
Automatic Substack post importer for lydia.ml
Fetches new posts from Substack RSS and converts them to markdown
"""

import os
import re
import json
import feedparser
import requests
from pathlib import Path
from datetime import datetime
from bs4 import BeautifulSoup
import html2text

# Configuration
SUBSTACK_URL = "https://lydianottingham.substack.com"
RSS_FEED_URL = f"{SUBSTACK_URL}/feed"
MARKDOWN_DIR = Path("markdown-essays")

def get_existing_posts():
    """Get list of already imported post slugs"""
    existing = set()
    if MARKDOWN_DIR.exists():
        for md_file in MARKDOWN_DIR.glob("*.md"):
            existing.add(md_file.stem)
    return existing

def slugify(title):
    """Convert title to URL-friendly slug"""
    slug = title.lower()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[-\s]+', '-', slug)
    return slug.strip('-')

def fetch_post_content(url):
    """Fetch full post content from Substack URL"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the main article content
        article = soup.find('article') or soup.find('div', class_='post-content')
        
        if not article:
            print(f"⚠️  Could not find article content for {url}")
            return None
        
        # Convert HTML to markdown
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.ignore_images = False
        h.ignore_emphasis = False
        h.body_width = 0  # Don't wrap lines
        
        markdown_content = h.handle(str(article))
        
        return markdown_content
        
    except Exception as e:
        print(f"❌ Error fetching {url}: {e}")
        return None

def parse_date(date_str):
    """Parse date from RSS feed"""
    try:
        dt = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %Z")
        return dt.strftime("%B %d, %Y")
    except:
        return datetime.now().strftime("%B %d, %Y")

def create_markdown_file(entry, content):
    """Create markdown file with frontmatter"""
    title = entry.get('title', 'Untitled')
    slug = slugify(title)
    date = parse_date(entry.get('published', ''))
    link = entry.get('link', '')
    
    # Extract subtitle if present
    subtitle = None
    if hasattr(entry, 'subtitle') and entry.subtitle:
        subtitle = entry.subtitle
    
    # Create frontmatter
    frontmatter = f"""---
title: "{title}"
date: "{date}"
category: "writing"
source: "{link}"
---

# {title}
"""
    
    if subtitle:
        frontmatter += f"\n### {subtitle}\n"
    
    # Combine frontmatter and content
    full_content = frontmatter + "\n" + content
    
    # Add attribution at the end
    full_content += f"\n\n---\n\n*Originally published on [Substack]({link})*\n"
    
    # Save to file
    filepath = MARKDOWN_DIR / f"{slug}.md"
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(full_content)
    
    return slug

def import_new_posts():
    """Main function to import new Substack posts"""
    print("🔍 Checking for new Substack posts...")
    
    # Ensure markdown directory exists
    MARKDOWN_DIR.mkdir(exist_ok=True)
    
    # Get existing posts
    existing_posts = get_existing_posts()
    
    # Fetch RSS feed
    try:
        feed = feedparser.parse(RSS_FEED_URL)
    except Exception as e:
        print(f"❌ Error fetching RSS feed: {e}")
        return 0
    
    if not feed.entries:
        print("⚠️  No entries found in RSS feed")
        return 0
    
    new_count = 0
    
    # Process each entry
    for entry in feed.entries:
        title = entry.get('title', 'Untitled')
        slug = slugify(title)
        url = entry.get('link', '')
        
        # Skip if already imported
        if slug in existing_posts:
            continue
        
        print(f"📝 Importing: {title}")
        
        # Fetch full content
        content = fetch_post_content(url)
        
        if not content:
            continue
        
        # Create markdown file
        try:
            created_slug = create_markdown_file(entry, content)
            print(f"✅ Created: {created_slug}.md")
            new_count += 1
        except Exception as e:
            print(f"❌ Error creating file for {title}: {e}")
    
    if new_count > 0:
        print(f"\n🎉 Imported {new_count} new post(s)!")
    else:
        print("✨ No new posts to import")
    
    return new_count

if __name__ == "__main__":
    import_new_posts()


