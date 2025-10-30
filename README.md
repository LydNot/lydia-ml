# Lydia Nottingham - Personal Website

A minimalist academic website for essays on AI, philosophy, and human flourishing.

## Features

- 🎨 Clean, minimalist design inspired by academic blogs
- 📝 Dynamic template system - edit once, update all posts
- 🔄 Markdown-to-JSON converter for easy content management
- 📱 Responsive design
- 🚀 Automatic deployment via Netlify (auto-deploy on file save!)

## Architecture

This site uses a **dynamic template system**:
- One template (`essay.html`) for all posts
- Content stored as JSON files loaded dynamically via JavaScript
- Edit the template → all posts update instantly
- Edit content → that post updates instantly

## Quick Start

### Adding/Editing Essays

1. **Write/edit essay:** Edit `.md` files in `markdown-essays/`
2. **Convert to JSON:** `python3 convert.py` (or let auto-deploy do it!)
3. **Organize in categories:** Edit `categories.yaml` to add to homepage
4. **Auto-deploy:** Changes push to GitHub automatically via `auto-deploy.sh`

### Organizing Categories

**The easiest way to manage your homepage!**

1. **Edit `categories.yaml`:** Simply add/remove post slugs under category names
   ```yaml
   personal favorites:
     - astronomical-waste--conscientious-objection-
     - not-buying-a-chinese-agibot
   
   ai & machine learning:
     - field-notes-from-eag-nyc
     - gpt-5-livestream-notes
   ```
2. **Regenerate index:** `python3 generate-index.py` (or let auto-deploy do it!)
3. **Result:** Homepage updates with new organization!

### Changing Styling

1. **Edit template:** Modify `essay.html` or `website-files/essay.html`
2. **Auto-deploy:** Changes push automatically
3. **Result:** All posts get the new styling instantly!

## File Structure

```
lydia.ml/
├── markdown-essays/        # 📝 Source files (edit these!)
│   ├── essay-1.md
│   └── essay-2.md
│
├── content/                # 🔄 Generated JSON (via convert.py)
│   ├── essay-1.json
│   └── essay-2.json
│
├── essay.html              # 🎨 Single template for all posts
├── index.html              # 🏠 Homepage
├── images/                 # 🖼️  Essay images
│
├── convert.py              # ⚙️  Markdown → JSON converter
├── auto-deploy.sh          # 🚀 Auto-push to GitHub on changes
│
└── website-files/          # 📦 Deployed to Netlify
    ├── content/            # JSON files
    ├── images/             # Images
    ├── essay.html          # Template
    └── index.html          # Homepage
```

## How It Works

1. **Write in Markdown:** Essays are written in `markdown-essays/` with frontmatter:
   ```markdown
   ---
   title: "My Essay"
   date: "October 29, 2025"
   category: "ai"
   ---
   
   ### Subtitle
   
   Content here...
   ```

2. **Convert to JSON:** Run `python3 convert.py` to generate JSON files in `content/`

3. **Dynamic Loading:** When someone visits `essay.html?post=my-essay`, JavaScript:
   - Reads the `?post=` parameter
   - Fetches `content/my-essay.json`
   - Injects content into the template

4. **Auto-Deploy:** The `auto-deploy.sh` script watches for file changes and automatically pushes to GitHub, which triggers Netlify deployment

## Deployment

- **Platform:** Netlify
- **Branch:** `main`
- **Build:** No build step needed (static files)
- **Deploy directory:** `website-files/`
- **Auto-deploy:** Enabled via `auto-deploy.sh` (runs in background)

## License

Personal website - all rights reserved.