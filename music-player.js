// Welcome overlay with music player
(function() {
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
            src="https://open.spotify.com/embed/playlist/6Wa6TIXcEwMry13bjo54rb?utm_source=generator" 
            width="100%" 
            height="352" 
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

