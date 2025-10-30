#!/usr/bin/env python3
"""
Helper script to fetch track IDs from a Spotify playlist.
This will help populate the music-player.js file with your songs.
"""

import requests
import json

# Your playlist ID
PLAYLIST_ID = "6Wa6TIXcEwMry13bjo54rb"

# Note: Spotify's public API requires authentication
# For a simpler approach, we'll provide instructions to get track IDs manually

print("=" * 60)
print("SPOTIFY TRACK ID EXTRACTOR")
print("=" * 60)
print()
print("To get track IDs from your 'site songs' playlist:")
print()
print("Option 1: Use Spotify Web Player")
print("-" * 60)
print("1. Open your playlist in the Spotify web player:")
print(f"   https://open.spotify.com/playlist/{PLAYLIST_ID}")
print()
print("2. Right-click each song → 'Share' → 'Copy Song Link'")
print("   Example link: https://open.spotify.com/track/3n3Ppam7vgaVa1iaRUc9Lp")
print()
print("3. Extract the track ID (the part after '/track/')")
print("   From the example: 3n3Ppam7vgaVa1iaRUc9Lp")
print()
print("Option 2: Use Spotify API (Requires Developer Account)")
print("-" * 60)
print("If you want me to help automate this, we'll need:")
print("1. Spotify Client ID and Client Secret")
print("2. Run an OAuth flow")
print()
print("=" * 60)
print()

# Alternative: Try to fetch without auth (only works for some playlists)
print("Attempting to fetch tracks (may require authentication)...")
print()

try:
    # Try the public embed API endpoint
    url = f"https://open.spotify.com/oembed?url=https://open.spotify.com/playlist/{PLAYLIST_ID}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print("✅ Found playlist:")
        print(f"   Title: {data.get('title', 'Unknown')}")
        print()
    else:
        print("ℹ️  Note: Full track list requires Spotify API authentication")
        print()
except Exception as e:
    print(f"⚠️  Could not fetch playlist data: {e}")
    print()

print("=" * 60)
print("EASIEST METHOD:")
print("=" * 60)
print("1. Open: https://open.spotify.com/playlist/" + PLAYLIST_ID)
print("2. Copy each track's 'Share → Copy Song Link'")
print("3. Send me the list of links")
print("4. I'll extract the IDs and update music-player.js!")
print("=" * 60)

