#!/usr/bin/env python3
"""
Generate index.html from categories.yaml
Usage: python3 generate-index.py
"""

import yaml
import json
import os
from pathlib import Path

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

def generate_category_html(categories):
    """Generate HTML for essay categories section"""
    html = []
    
    for category, posts in categories.items():
        html.append(f'                    <h2>{category}</h2>')
        html.append('                    <ul class="essay-list">')
        
        for slug in posts:
            title = get_post_title(slug)
            html.append(f'                        <li><a href="essay.html?post={slug}">{title}</a></li>')
        
        html.append('                    </ul>')
        html.append('')  # blank line between categories
    
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

        <div class="main-content">
            <!-- Left Column - Main Content -->
            <div class="content-column">
                <!-- Introduction -->
                <section class="intro">
                    <p>I write about AI, philosophy, and human flourishing.</p>
                </section>

                <!-- Contact -->
                <section class="contact-info">
                    <p><a href="mailto:hello@lydia.ml">hello@lydia.ml</a> • <a href="https://lydianottingham.substack.com/">Substack</a></p>
                </section>

                <!-- Essay Categories -->
                <section class="essay-categories">
{category_html}
                </section>
            </div>

            <!-- Right Column - Sidebar -->
            <div class="sidebar">
                <!-- Recent Posts -->
                <div class="sidebar-box">
                    <h3>Recent</h3>
                    <ul class="recent-list">
                        <li><span class="date">Dec 15</span> <a href="essay.html?post=gpt-5-livestream-notes">GPT-5 Livestream Notes</a></li>
                        <li><span class="date">Dec 8</span> <a href="essay.html?post=astronomical-waste--conscientious-objection-">Astronomical Waste & Conscientious Objection</a></li>
                        <li><span class="date">Nov 28</span> <a href="essay.html?post=amusing-labels-in-the-jiminy-cricket-environments">Amusing Labels in the Jiminy Cricket Environments</a></li>
                        <li><span class="date">Nov 15</span> <a href="essay.html?post=how-to-be-a-human-starter-pack">How to be a Human Starter Pack</a></li>
                        <li><span class="date">Oct 30</span> <a href="essay.html?post=9030-ml-reading-group-retrospective">90/30 ML Reading Group: Retrospective</a></li>
                    </ul>
                </div>

                <!-- Newsletter Signup -->
                <div class="sidebar-box newsletter">
                    <h3>LYDIA ML</h3>
                    <p class="subscriber-count">Join 1,200+ readers</p>
                    <form class="newsletter-form">
                        <input type="email" placeholder="Type your email..." class="email-input">
                        <button type="submit" class="subscribe-btn">Subscribe</button>
                    </form>
                    <p class="disclaimer">Weekly essays on ideas that matter. No spam, ever.</p>
                </div>
            </div>
        </div>
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

