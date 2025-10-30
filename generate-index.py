#!/usr/bin/env python3
"""
Generate index.html from categories.yaml
Usage: python3 generate-index.py
"""

import pyyaml
import json
import os
from pathlib import Path
from datetime import datetime

def load_categories():
    """Load category configuration from YAML file"""
    with open('categories.yaml', 'r') as f:
        return yaml.safe_load(f)

def get_post_title(slug):
    """Get post title from JSON file"""
    json_path = f'content/{slug}.json'
    if os.path.exists(json_path):
        with open(json_path, 'r') as f:
            data = json.load(f)
            return data.get('title', slug)
    return slug

def get_all_posts_with_dates():
    """Get all posts from content directory with their dates"""
    posts = []
    content_dir = Path('content')
    
    for json_file in content_dir.glob('*.json'):
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
                slug = json_file.stem
                title = data.get('title', slug)
                date_str = data.get('date', '')
                
                if date_str:
                    # Parse date like "October 14, 2025"
                    try:
                        date_obj = datetime.strptime(date_str, '%B %d, %Y')
                        posts.append({
                            'slug': slug,
                            'title': title,
                            'date': date_obj,
                            'date_str': date_str
                        })
                    except ValueError:
                        # If date parsing fails, skip this post
                        pass
        except (json.JSONDecodeError, FileNotFoundError):
            continue
    
    # Sort by date, most recent first
    posts.sort(key=lambda x: x['date'], reverse=True)
    return posts

def format_date_for_sidebar(date_obj):
    """Format date as 'Dec 15' for sidebar"""
    return date_obj.strftime('%b %d')

def generate_category_html(categories):
    """Generate HTML for essay categories section with three columns (alternating)"""
    category_items = list(categories.items())
    
    # Distribute across 3 columns: 0,3,6... → col1, 1,4,7... → col2, 2,5,8... → col3
    col1_categories = [cat for i, cat in enumerate(category_items) if i % 3 == 0]
    col2_categories = [cat for i, cat in enumerate(category_items) if i % 3 == 1]
    col3_categories = [cat for i, cat in enumerate(category_items) if i % 3 == 2]
    
    def generate_column(category_list):
        html = []
        for category, posts in category_list:
            html.append(f'                        <h2>{category}</h2>')
            html.append('                        <ul class="essay-list">')
            
            for slug in posts:
                title = get_post_title(slug)
                html.append(f'                            <li><a href="essay.html?post={slug}">{title}</a></li>')
            
            html.append('                        </ul>')
            html.append('')  # blank line between categories
        return '\n'.join(html)
    
    # Build three-column layout
    html = ['                    <div class="essay-categories-grid">']
    
    # Column 1
    html.append('                        <div class="category-column">')
    html.append(generate_column(col1_categories))
    html.append('                        </div>')
    
    # Column 2
    html.append('                        <div class="category-column">')
    html.append(generate_column(col2_categories))
    html.append('                        </div>')
    
    # Column 3
    html.append('                        <div class="category-column">')
    html.append(generate_column(col3_categories))
    html.append('                        </div>')
    
    html.append('                    </div>')
    
    return '\n'.join(html)

def generate_recent_html(num_posts=5):
    """Generate HTML for recent posts sidebar"""
    posts = get_all_posts_with_dates()[:num_posts]
    
    html = []
    for post in posts:
        date_formatted = format_date_for_sidebar(post['date'])
        html.append(f'                        <li><span class="date">{date_formatted}</span> <a href="essay.html?post={post["slug"]}">{post["title"]}</a></li>')
    
    return '\n'.join(html)

def generate_index():
    """Generate complete index.html"""
    categories = load_categories()
    category_html = generate_category_html(categories)
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LYDIA</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Crimson+Text:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
</head>
<body>
    <div class="container">
        <!-- Header -->
        <header class="header">
            <h1 class="site-title">LYDIA</h1>
            <nav class="nav">
                <a href="#about">About</a>
                <a href="#essays">Essays</a>
                <a href="#contact">Contact</a>
                <a href="#archive">Archive</a>
            </nav>
        </header>

        <!-- Introduction -->
        <section class="intro">
            <p>hello! welcome to my site :D i like:
America
The phenomenon of grokking / phase transitions
People / things with Markovian property
Proactivity
Have I mentioned I like America? I really like America.
Musicals
Mathematical modelling, particularly phase plane analysis and Markov chains
Bridging artificial intelligence with the physical world
Unpretentiousness
Nondogmatism, thinking for oneself
Unrigorously dissolving philosophical problems
The anti-inductive & open-ended
Precision </p>
        </section>

        <!-- Contact -->
        <section class="contact-info">
            <p><a href="mailto:hello@lydia.ml">hello@lydia.ml</a> • <a href="https://lydianottingham.substack.com/">Substack</a></p>
        </section>

        <!-- Essay Categories -->
        <section class="essay-categories">
{category_html}
        </section>

        <!-- Newsletter Signup at Bottom -->
        <section class="newsletter-bottom">
            <iframe src="https://lydianottingham.substack.com/embed" width="100%" height="320" style="border:1px solid #2d4a6e; background:#0a1628; border-radius: 8px;" frameborder="0" scrolling="no"></iframe>
        </section>
    </div>
</body>
</html>'''
    
    # Write to index.html
    with open('index.html', 'w') as f:
        f.write(html)
    
    # Also copy to website-files
    with open('website-files/index.html', 'w') as f:
        f.write(html)
    
    print("✅ Generated index.html from categories.yaml")

if __name__ == '__main__':
    generate_index()

