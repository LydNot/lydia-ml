#!/usr/bin/env python3
"""
Remove redundant header section from all essay HTML files.
This removes the duplicate title, subtitle, and empty share link that appears after the proper header.
"""

import os
import re
import glob

def remove_redundant_header(content):
    """Remove the redundant header section from HTML content."""
    
    # Pattern to match the redundant header section:
    # <h1>Title</h1>
    # <h3>Subtitle</h3>
    # (empty line)
    # <p><a href="..."></a></p>
    
    # Remove the redundant h1 title (duplicate of main title)
    content = re.sub(r'<h1>[^<]*</h1>\s*\n', '', content)
    
    # Remove the subtitle h3
    content = re.sub(r'<h3>[^<]*</h3>\s*\n', '', content)
    
    # Remove empty share link paragraphs
    content = re.sub(r'<p><a href="[^"]*"></a></p>\s*\n', '', content)
    
    # Clean up any extra blank lines
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
    
    return content

def process_essay_file(file_path):
    """Process a single essay HTML file."""
    print(f"Processing: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        content = remove_redundant_header(content)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✅ Updated: {file_path}")
        else:
            print(f"  ⏭️  No changes needed: {file_path}")
            
    except Exception as e:
        print(f"  ❌ Error processing {file_path}: {e}")

def main():
    """Main function to process all essay files."""
    print("🧹 Removing redundant header sections from essay files...")
    
    # Find all HTML files in essays directory
    essay_files = glob.glob("essays/*.html")
    
    if not essay_files:
        print("❌ No essay files found in essays/ directory")
        return
    
    print(f"Found {len(essay_files)} essay files to process")
    
    for file_path in essay_files:
        process_essay_file(file_path)
    
    print("\n🎉 Finished processing all essay files!")
    print("The redundant header sections (duplicate title, subtitle, empty share link) have been removed.")

if __name__ == "__main__":
    main()
