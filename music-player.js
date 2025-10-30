// Welcome overlay with music player
(function() {
    // List of track IDs from your "site songs" playlist
    // To add more: open each song in Spotify, copy the track ID from the URL
    // URL format: https://open.spotify.com/track/TRACK_ID
    const trackIds = [
        '3n3Ppam7vgaVa1iaRUc9Lp',  // Example track
        // Add more track IDs here - I'll help you populate this!
    ];
    
    // Randomly select a track
    const randomTrack = trackIds[Math.floor(Math.random() * trackIds.length)];
    
    // Create welcome overlay
    const overlay = document.createElement('div');
    overlay.className = 'welcome-overlay';
    overlay.innerHTML = `
        <div class="welcome-content">
            <h2 class="welcome-title">welcome ✨</h2>
            <button class="welcome-button">enter 🎵</button>
        </div>
    `;
    document.body.appendChild(overlay);
    
    // Create floating music player (hidden initially)
    const musicPlayer = document.createElement('div');
    musicPlayer.className = 'music-player';
    musicPlayer.innerHTML = `
        <div class="music-player-header">
            <span>now playing 🎵</span>
            <button class="music-player-close">×</button>
        </div>
        <iframe 
            style="border-radius:12px" 
            src="https://open.spotify.com/embed/track/${randomTrack}?utm_source=generator" 
            width="100%" 
            height="152" 
            frameBorder="0" 
            allowfullscreen="" 
            allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" 
            loading="lazy">
        </iframe>
    `;
    musicPlayer.style.display = 'none';
    document.body.appendChild(musicPlayer);
    
    // Handle enter button click
    overlay.querySelector('.welcome-button').addEventListener('click', () => {
        // Fade out overlay
        overlay.style.opacity = '0';
        setTimeout(() => {
            overlay.style.display = 'none';
        }, 500);
        
        // Show music player after a brief delay
        setTimeout(() => {
            musicPlayer.style.display = 'block';
            setTimeout(() => {
                musicPlayer.style.opacity = '1';
                musicPlayer.style.transform = 'translateY(0)';
            }, 10);
        }, 600);
    });
    
    // Handle close button
    musicPlayer.querySelector('.music-player-close').addEventListener('click', () => {
        musicPlayer.style.opacity = '0';
        musicPlayer.style.transform = 'translateY(20px)';
        setTimeout(() => {
            musicPlayer.style.display = 'none';
        }, 300);
    });
    
    // Prevent scrolling when overlay is visible
    document.body.style.overflow = 'hidden';
    overlay.addEventListener('transitionend', (e) => {
        if (e.target === overlay && overlay.style.opacity === '0') {
            document.body.style.overflow = '';
        }
    });
})();

