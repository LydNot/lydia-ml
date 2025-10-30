#!/usr/bin/env python3
"""
Simple Markdown to HTML converter for Lydia ML essays
Usage: python3 convert.py
"""

import os
import re
import json
from datetime import datetime
import markdown
from pathlib import Path

def create_html_template(title, content, date=None, category=None, subtitle=None):
    """Create HTML template for essays"""
    if not date:
        date = datetime.now().strftime("%B %d, %Y")
    
    # Estimate reading time (roughly 200 words per minute)
    word_count = len(content.split())
    reading_time = max(1, word_count // 200)
    
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Lydia ML</title>
    <link rel="stylesheet" href="../styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Crimson+Text:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
    <style>
        .essay-content {{
            max-width: 700px;
            margin: 0 auto;
            padding: 40px 20px;
        }}
        
        .essay-header {{
            margin-bottom: 40px;
        }}
        
        .essay-title {{
            font-family: 'Inter', sans-serif;
            font-size: 2.2rem;
            font-weight: 600;
            color: #1a1a1a;
            margin-bottom: 15px;
            line-height: 1.2;
        }}
        
        .essay-meta {{
            color: #666;
            font-size: 0.9rem;
            margin-bottom: 15px;
        }}
        
        .essay-subtitle {{
            font-family: 'Inter', sans-serif;
            font-size: 1.2rem;
            font-weight: 500;
            color: #333;
            margin-bottom: 40px;
            font-style: italic;
            text-align: center;
        }}
        
        .essay-body {{
            font-family: 'Crimson Text', Georgia, serif;
            font-size: 1.1rem;
            line-height: 1.7;
            color: #333;
        }}
        
        .essay-body h2 {{
            font-family: 'Inter', sans-serif;
            font-size: 1.4rem;
            font-weight: 600;
            color: #1a1a1a;
            margin: 40px 0 20px 0;
        }}
        
        .essay-body h3 {{
            font-family: 'Inter', sans-serif;
            font-size: 1.2rem;
            font-weight: 500;
            color: #1a1a1a;
            margin: 30px 0 15px 0;
        }}
        
        .essay-body p {{
            margin-bottom: 20px;
        }}
        
        .essay-body ul, .essay-body ol {{
            margin: 20px 0;
            padding-left: 30px;
        }}
        
        .essay-body li {{
            margin-bottom: 8px;
        }}
        
        .essay-body blockquote {{
            border-left: 3px solid #e6e6e6;
            padding-left: 20px;
            margin: 20px 0;
            font-style: italic;
            color: #666;
        }}
        
        .essay-body code {{
            background-color: #f5f5f5;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Monaco', 'Consolas', monospace;
            font-size: 0.9em;
        }}
        
        .essay-body pre {{
            background-color: #f5f5f5;
            padding: 20px;
            border-radius: 5px;
            overflow-x: auto;
            margin: 20px 0;
        }}
        
        .essay-body pre code {{
            background: none;
            padding: 0;
        }}
        
        .back-link {{
            display: inline-block;
            margin-bottom: 30px;
            color: #666;
            text-decoration: none;
            font-size: 0.9rem;
        }}
        
        .back-link:hover {{
            color: #1a1a1a;
        }}
        
        @media (max-width: 768px) {{
            .essay-content {{
                padding: 20px 15px;
            }}
            
            .essay-title {{
                font-size: 1.8rem;
            }}
            
            .essay-body {{
                font-size: 1rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="essay-content">
        <a href="../index.html" class="back-link">← Back to home</a>
        
        <div class="essay-header">
            <h1 class="essay-title">{title}</h1>
            {f'<div class="essay-meta">{date}</div>' if date else ''}
            {f'<div class="essay-subtitle">{subtitle}</div>' if subtitle else ''}
        </div>
        
        <div class="essay-body">
            {content}
        </div>
    </div>
</body>
</html>"""
    
    return html_template

def parse_markdown_file(file_path):
    """Parse markdown file and extract metadata"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract frontmatter if present
    frontmatter = {}
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter_text = parts[1]
            content = parts[2].strip()
            
            # Parse frontmatter
            for line in frontmatter_text.strip().split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    frontmatter[key.strip()] = value.strip()
    
    # Extract title from first heading if not in frontmatter
    title = frontmatter.get('title', '')
    if not title:
        title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        if title_match:
            title = title_match.group(1)
        else:
            title = Path(file_path).stem.replace('-', ' ').title()
    
    # Extract subtitle from h3 heading
    subtitle = None
    subtitle_match = re.search(r'^### (.+)$', content, re.MULTILINE)
    if subtitle_match:
        subtitle = subtitle_match.group(1)
    
    # Clean up content by removing redundant elements
    # Remove the main title (h1) if it's duplicated
    content = re.sub(r'^# .+$\n', '', content, flags=re.MULTILINE)
    
    # Remove the subtitle (h3) from content since we'll add it to header
    content = re.sub(r'^### .+$\n', '', content, flags=re.MULTILINE)
    
    # Remove avatar image (first image that links to author profile)
    content = re.sub(r'^\[!\[.*?avatar.*?\]\(.*?\)\]\(.*?substack\.com/@.*?\)\s*$', '', content, flags=re.MULTILINE | re.IGNORECASE)
    
    # Remove author name links (just the link, not all links)
    content = re.sub(r'^\[.*?\]\(https://substack\.com/@.*?\)\s*$', '', content, flags=re.MULTILINE)
    
    # Convert linked images to simple images (unwrap from external links)
    # Pattern: [![alt](image-path)](external-link) -> ![alt](image-path)
    content = re.sub(r'\[!\[(.*?)\]\((images/[^)]+)\)\]\([^)]+\)', r'![\1](\2)', content)
    
    # Remove duplicate dates (more comprehensive patterns)
    content = re.sub(r'^[A-Za-z]{3,9} \d{1,2}, \d{4}\s*$', '', content, flags=re.MULTILINE)
    content = re.sub(r'^\w{3,9} \d{1,2}, \d{4}\s*$', '', content, flags=re.MULTILINE)
    
    # Remove standalone numbers on their own line (reading times, etc.)
    content = re.sub(r'^\s*\d+\s*$', '', content, flags=re.MULTILINE)
    
    # Remove comment count links like [2](url)
    content = re.sub(r'^\s*\[\d+\]\([^)]*comments[^)]*\)\s*$', '', content, flags=re.MULTILINE)
    content = re.sub(r'^\s*\[\d+\]\([^)]+\)\s*$', '', content, flags=re.MULTILINE)
    
    # Remove Share links and empty links (case insensitive, more thorough)
    content = re.sub(r'^\s*\[Share\]\([^)]*\)\s*$', '', content, flags=re.MULTILINE | re.IGNORECASE)
    content = re.sub(r'\[Share\]\([^)]*\)', '', content, flags=re.IGNORECASE)  # Also remove inline
    content = re.sub(r'^\s*\[\]\([^)]*\)\s*$', '', content, flags=re.MULTILINE)
    content = re.sub(r'\[\]\([^)]*\)', '', content)  # Also remove inline empty links
    
    # Remove any lines with just whitespace after previous removals
    content = re.sub(r'^\s*$\n', '\n', content, flags=re.MULTILINE)
    
    # Clean up extra blank lines
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
    content = content.strip()
    
    # Convert markdown to HTML
    md = markdown.Markdown(extensions=['extra', 'codehilite'])
    html_content = md.convert(content)
    
    return {
        'title': title,
        'content': html_content,
        'date': frontmatter.get('date', ''),
        'category': frontmatter.get('category', ''),
        'subtitle': subtitle,
        'filename': Path(file_path).stem
    }

def convert_all_essays():
    """Convert all markdown files to HTML and JSON"""
    markdown_dir = Path('markdown-essays')
    essays_dir = Path('essays')
    content_dir = Path('content')
    
    if not markdown_dir.exists():
        print("Creating markdown-essays directory...")
        markdown_dir.mkdir()
        return
    
    essays_dir.mkdir(exist_ok=True)
    content_dir.mkdir(exist_ok=True)
    
    converted_essays = []
    
    for md_file in markdown_dir.glob('*.md'):
        print(f"Converting {md_file.name}...")
        
        essay_data = parse_markdown_file(md_file)
        
        # Create standalone HTML file (backwards compatibility)
        html_content = create_html_template(
            essay_data['title'],
            essay_data['content'],
            essay_data['date'],
            essay_data['category'],
            essay_data['subtitle']
        )
        
        # Write HTML file
        html_file = essays_dir / f"{essay_data['filename']}.html"
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # Create JSON file for dynamic loading
        # Strip extra quotes from frontmatter values
        json_data = {
            'title': essay_data['title'].strip('"'),
            'date': essay_data['date'].strip('"'),
            'subtitle': essay_data['subtitle'] if essay_data['subtitle'] else None,
            'category': essay_data['category'].strip('"') if essay_data['category'] else None,
            'content': essay_data['content']
        }
        
        json_file = content_dir / f"{essay_data['filename']}.json"
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=2, ensure_ascii=False)
        
        converted_essays.append(essay_data)
    
    print(f"\nConverted {len(converted_essays)} essays!")
    print(f"  - Standalone HTML: essays/")
    print(f"  - Dynamic JSON: content/")
    return converted_essays

def update_index_page(essays):
    """Update the index page with essay links"""
    # This is a simple version - you could make it more sophisticated
    print("\nTo update your index.html with new essays, manually add them to the appropriate categories.")
    print("Here are your converted essays:")
    for essay in essays:
        print(f"- {essay['title']} ({essay['filename']}.html)")

if __name__ == "__main__":
    print("Converting Markdown essays to HTML...")
    essays = convert_all_essays()
    if essays:
        update_index_page(essays)
    else:
        print("No markdown files found in markdown-essays/ directory.")
        print("Create some .md files there and run this script again!")
