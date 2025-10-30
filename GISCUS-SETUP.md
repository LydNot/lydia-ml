# Giscus Comments Setup

Giscus has been added to your essay pages! Here's how to complete the setup:

## Step 1: Enable GitHub Discussions

1. Go to your GitHub repository: `https://github.com/YOUR_USERNAME/lydia.ml`
2. Click **Settings** → **Features**
3. Check the box for **Discussions**
4. Click the **Set up discussions** button if prompted

## Step 2: Install Giscus App

1. Go to [https://github.com/apps/giscus](https://github.com/apps/giscus)
2. Click **Install**
3. Select your repository (`lydia.ml`)
4. Grant the permissions

## Step 3: Get Your Configuration

1. Go to [https://giscus.app](https://giscus.app)
2. Enter your repository name: `YOUR_USERNAME/lydia.ml`
3. Select **Discussions Category**: Create a new category called "Comments" or use "General"
4. The page will generate configuration values for you

## Step 4: Update essay.html

Open `essay.html` and replace these TODO values (around line 269-272):

```javascript
script.setAttribute('data-repo', 'YOUR_USERNAME/lydia.ml'); // Replace YOUR_USERNAME
script.setAttribute('data-repo-id', 'YOUR_REPO_ID'); // Get from giscus.app
script.setAttribute('data-category-id', 'YOUR_CATEGORY_ID'); // Get from giscus.app
```

With the actual values from giscus.app.

## Step 5: Deploy

Once you've updated the values:

```bash
python3 convert.py  # If you have any updated essays
git add essay.html
git commit -m "Add Giscus comments"
git push
```

## What You Get

✅ Comments powered by GitHub Discussions
✅ Markdown support
✅ Reactions & voting
✅ No ads or tracking
✅ Free forever
✅ Matches your dark theme
✅ Anonymous commenting (if they have GitHub accounts)

Comments will appear at the bottom of each essay page. Each essay gets its own discussion thread based on the URL path.

## Testing

After setup, visit any essay page like:
`https://yourdomain.com/essay.html?post=your-essay-slug`

The comments section should appear at the bottom!

