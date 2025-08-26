
document.addEventListener('DOMContentLoaded', () => {
    const songListContainer = document.getElementById('song-list');
    const playlistListContainer = document.getElementById('playlist-list');
    const addSongForm = document.getElementById('add-song-form');


    function fetchPlaylists() {
        fetch('/api/playlists')
            .then(response => response.json())
            .then(data => {
                playlistListContainer.innerHTML = '';
                data.playlists.forEach(playlist => {
                    const li = document.createElement('li');
                    li.className = 'list-item';
                    li.innerHTML = `<h3>${playlist.name}</h3><p>${playlist.description}</p>`;
                    li.addEventListener('click', () => fetchSongsForPlaylist(playlist.id));
                    playlistListContainer.appendChild(li);
                });
            })
            .catch(error => console.error('Error fetching playlists:', error));
    }


    function fetchSongsForPlaylist(playlistId) {
        fetch(`/api/playlists/${playlistId}/songs`)
            .then(response => response.json())
            .then(data => {
                renderSongs(data.songs);
            })
            .catch(error => console.error('Error fetching songs for playlist:', error));
    }


    function fetchAllSongs() {
        fetch('/api/songs')
            .then(response => response.json())
            .then(data => {
                renderSongs(data.songs);
            })
            .catch(error => console.error('Error fetching all songs:', error));
    }


    function renderSongs(songs) {
        songListContainer.innerHTML = '';
        if (songs.length === 0) {
            songListContainer.innerHTML = '<li>No songs found.</li>';
        } else {
            songs.forEach(song => {
                const li = document.createElement('li');
                li.className = 'list-item';
                li.innerHTML = `
                    <h3>${song.title}</h3>
                    <p>by ${song.artist_name} | Album: ${song.album || 'N/A'}</p>
                `;
                songListContainer.appendChild(li);
            });
        }
    }


    addSongForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const form = event.target;
        const data = {
            title: form.title.value,
            artist_name: form.artist_name.value,
            album: form.album.value || null
        };

        fetch('/api/songs', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        })
        .then(response => {
            if (!response.ok) {
                return response.json().then(err => { throw new Error(err.error || 'Unknown error'); });
            }
            return response.json();
        })
        .then(data => {
            alert(data.message);
            form.reset();
            fetchAllSongs(); 
        })
        .catch(error => {
            console.error('Error adding song:', error);
            alert('Error: ' + error.message);
        });
    });

    fetchPlaylists();
    fetchAllSongs();
});