#!/usr/bin/env python3
"""
Remove buggy author section from all essay HTML files.
This removes the duplicate date, numbers, and share button section.
"""

import os
import re
import glob

def remove_author_section(content):
    """Remove the buggy author section from HTML content."""
    
    # Pattern to match the buggy section:
    # <p>Jun 01, 2025</p> (or similar date)
    # <p>4</p> (or similar number)
    # <p><a href="...">1</a></p> (or similar share link)
    
    # Remove duplicate date line (like <p>Jun 01, 2025</p>)
    content = re.sub(r'<p>\w{3} \d{2}, \d{4}</p>\s*\n', '', content)
    
    # Remove standalone number lines (like <p>4</p>)
    content = re.sub(r'<p>\d+</p>\s*\n', '', content)
    
    # Remove share link lines (like <p><a href="...">1</a></p>)
    content = re.sub(r'<p><a href="[^"]*">\d+</a></p>\s*\n', '', content)
    
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
        content = remove_author_section(content)
        
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
    print("🧹 Removing buggy author sections from essay files...")
    
    # Find all HTML files in essays directory
    essay_files = glob.glob("essays/*.html")
    
    if not essay_files:
        print("❌ No essay files found in essays/ directory")
        return
    
    print(f"Found {len(essay_files)} essay files to process")
    
    for file_path in essay_files:
        process_essay_file(file_path)
    
    print("\n🎉 Finished processing all essay files!")
    print("The buggy author sections (avatar, name, numbers, share button) have been removed.")

if __name__ == "__main__":
    main()