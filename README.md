# Lydia Nottingham - Personal Website

A minimalist academic website for essays on AI, philosophy, and human flourishing.

## Features

- Clean, minimalist design inspired by academic blogs
- Essay categorization system
- Markdown-to-HTML converter for easy content management
- Responsive design
- Automatic deployment via Netlify

## Local Development

1. **Add new essays:** Create `.md` files in `markdown-essays/`
2. **Convert to HTML:** `python3 convert.py`
3. **Update homepage:** Edit `index.html` to add new essay links
4. **Commit changes:** `git add . && git commit -m "Add new essay"`
5. **Deploy:** `git push origin main`

## File Structure

```
lydia.ml/
├── index.html              # Main homepage
├── styles.css              # All styling
├── convert.py              # Markdown to HTML converter
├── substack-import.py      # Import essays from Substack
├── new-essay.sh           # Helper script for new essays
├── markdown-essays/        # Write essays here (.md files)
├── essays/                 # Generated HTML files
└── website-files/          # Deployment package
```

## Deployment

This site automatically deploys to Netlify when changes are pushed to the main branch.

## License

Personal website - all rights reserved.