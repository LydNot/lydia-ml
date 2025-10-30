#!/bin/bash

# Auto-deploy script for lydia.ml
# Watches for file changes and automatically commits/pushes to GitHub

REPO_DIR="/Users/mox/lydia.ml"
cd "$REPO_DIR"

echo "🚀 Auto-deploy started for lydia.ml"
echo "📁 Watching: $REPO_DIR"
echo "🔄 Changes will be automatically committed and pushed to GitHub"
echo "📰 Checking Substack for new posts every hour"
echo "⚠️  Press Ctrl+C to stop"
echo ""

# Track last Substack check time
LAST_SUBSTACK_CHECK=$(date +%s)

# Function to check for new Substack posts
check_substack() {
    cd "$REPO_DIR"
    
    CURRENT_TIME=$(date +%s)
    TIME_DIFF=$((CURRENT_TIME - LAST_SUBSTACK_CHECK))
    
    # Check every hour (3600 seconds)
    if [ $TIME_DIFF -ge 3600 ]; then
        echo "📰 Checking Substack for new posts..."
        python3 substack-import.py 2>&1 | grep -E "(Importing|Created|Imported|new posts)" || true
        LAST_SUBSTACK_CHECK=$CURRENT_TIME
        echo ""
    fi
}

# Function to commit and push changes
commit_and_push() {
    cd "$REPO_DIR"
    
    # Check for new Substack posts periodically
    check_substack
    
    # Check if markdown files have changed
    if git status -s | grep -q "markdown-essays/.*\.md"; then
        echo "📝 Markdown files changed - running convert.py..."
        python3 convert.py > /dev/null 2>&1
        
        # Copy generated JSON to website-files
        cp -r content/*.json website-files/content/ 2>/dev/null
        
        echo "✅ Converted markdown to JSON"
    fi
    
    # Check if there are any changes to commit
    if [[ -n $(git status -s) ]]; then
        echo "📝 Changes detected..."
        
        # Stage all changes
        git add -A
        
        # Create commit with timestamp
        TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
        git commit -m "Auto-deploy: $TIMESTAMP"
        
        # Push to GitHub
        echo "⬆️  Pushing to GitHub..."
        git push origin main
        
        echo "✅ Deployed at $TIMESTAMP"
        echo ""
    fi
}

# Watch for changes using fswatch (install with: brew install fswatch)
if command -v fswatch &> /dev/null; then
    # Use fswatch for real-time monitoring
    fswatch -o \
        --exclude='\.git/' \
        --exclude='node_modules/' \
        --exclude='\.DS_Store' \
        --exclude='__pycache__/' \
        "$REPO_DIR" | while read f; do
        sleep 2  # Wait 2 seconds to batch rapid changes
        commit_and_push
    done
else
    # Fallback: poll every 30 seconds if fswatch is not installed
    echo "⚠️  fswatch not found. Using polling mode (checks every 30s)"
    echo "💡 For better performance, install fswatch: brew install fswatch"
    echo ""
    
    while true; do
        commit_and_push
        sleep 30
    done
fi

