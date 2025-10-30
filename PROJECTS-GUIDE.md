# Projects Management Guide

## How to Add/Edit Projects

Edit `projects.yaml` to manage your projects. The system automatically generates project cards on your homepage.

### Basic Structure

```yaml
projects:
  - title: "Project Name"
    description: "A brief description of your project"
    image: "images/project-name.png"  # Optional: image path
    link: "https://external-link.com"  # Optional: external link
    webpage: "project-page.html"  # Optional: internal page
```

### Fields Explained

- **title**: The name of your project (required)
- **description**: A short description (optional, but recommended)
- **image**: Path to an image in the `images/` folder (optional)
  - Just drop images in the `images/` folder and reference them
  - Example: `"images/orchard-logo.png"`
- **link**: External link (GitHub, website, etc.) - opens in new tab (optional)
- **webpage**: Internal page for more details (optional)
  - Example: `"orchard.html"` - you can create custom HTML pages

### Examples

#### Simple Project (no image, external link only)
```yaml
- title: "90/30 ML Reading Group"
  description: "Weekly deep dives into machine learning papers"
  link: "https://github.com/yourname/90-30-ml"
```

#### Full Project (with image and internal page)
```yaml
- title: "[orchard]"
  description: "AI alignment research platform"
  image: "images/orchard-preview.png"
  link: "https://github.com/orchard-ai"
  webpage: "orchard.html"
```

#### Minimal Project
```yaml
- title: "FHI Paper Working Group"
  description: "Collaborative research on AI safety"
```

## Workflow

1. **Edit** `projects.yaml` with your project details
2. **Add images** (if any) to the `images/` folder
3. **Run** `python3 generate-index.py` (or let auto-deploy do it)
4. **Deploy** automatically via fswatch, or manually copy to `website-files/`

## Tips

- Keep descriptions concise (1-2 sentences)
- Images will be displayed full-width within the project card
- You can have 0-10+ projects, the layout adapts automatically
- Projects appear in the order you list them in `projects.yaml`

