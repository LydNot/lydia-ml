# Easy Essay Management System

I've created a super simple system for you to write essays without touching HTML! Here's how it works:

## 🚀 **How to Add New Essays**

### Method 1: Use the helper script (easiest)
```bash
./new-essay.sh "My Essay Title" "personal favorites"
```
This creates a template file in `markdown-essays/` with the right format.

### Method 2: Create manually
1. Create a new `.md` file in `markdown-essays/` folder
2. Add frontmatter at the top:
```markdown
---
title: "Your Essay Title"
date: "December 15, 2024"
category: "personal favorites"
---

# Your Essay Title

Write your essay here using normal Markdown...
```

## 📝 **Writing Essays**

Just write in **Markdown** - it's super easy:
- `# Heading` for main headings
- `## Subheading` for subheadings  
- `**bold text**` for bold
- `- bullet points` for lists
- `1. numbered lists` for numbered lists
- `> quotes` for blockquotes

## 🔄 **Converting to Website**

After writing your essay:
```bash
python3 convert.py
```

This automatically:
- Converts your Markdown to HTML
- Creates a beautiful essay page
- Adds proper styling and navigation
- Calculates reading time

## 📁 **File Structure**

```
lydia.ml/
├── markdown-essays/     # ← Write your essays here (.md files)
├── essays/              # ← Generated HTML files (auto-created)
├── convert.py           # ← Converts Markdown to HTML
├── new-essay.sh         # ← Helper script to create new essays
└── index.html           # ← Your main page
```

## 🎯 **Example Workflow**

1. **Create new essay:**
   ```bash
   ./new-essay.sh "Why I Love Minimalism" "philosophy & ideas"
   ```

2. **Edit the essay:**
   ```bash
   # Edit markdown-essays/why-i-love-minimalism.md
   ```

3. **Convert to HTML:**
   ```bash
   python3 convert.py
   ```

4. **Add link to homepage:**
   Edit `index.html` and add your essay to the appropriate category

## ✨ **What You Get**

- Beautiful, responsive essay pages
- Automatic reading time calculation
- Clean typography (Crimson Text for body, Inter for headings)
- Mobile-friendly design
- Print-friendly styling
- Back-to-home navigation

## 🎨 **Categories Available**

- `personal favorites`
- `technology & society` 
- `philosophy & ideas`
- `one-pagers`

Just use these exact category names in your frontmatter!

---

**That's it!** No more HTML editing - just write in Markdown and run the converter. Much easier! 🎉
