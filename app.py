
from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Akshat9091' 
app.config['MYSQL_DB'] = 'music_system'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/songs', methods=['GET'])
def get_songs():
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT 
            s.id, 
            s.title, 
            a.name AS artist_name, 
            s.album, 
            s.duration_seconds
        FROM songs s
        JOIN artists a ON s.artist_id = a.id
    """)
    songs = cur.fetchall()
    cur.close()
    
    song_list = []
    for song in songs:
        song_list.append({
            "id": song[0],
            "title": song[1],
            "artist_name": song[2],
            "album": song[3],
            "duration_seconds": song[4]
        })
    return jsonify({"songs": song_list})
@app.route('/api/playlists', methods=['GET'])
def get_playlists():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, name, description FROM playlists")
    playlists_data = cur.fetchall()
    cur.close()

    playlists_list = []
    for playlist in playlists_data:
        playlists_list.append({
            "id": playlist[0],
            "name": playlist[1],
            "description": playlist[2]
        })
    return jsonify({"playlists": playlists_list})


@app.route('/api/playlists/<int:playlist_id>/songs', methods=['GET'])
def get_playlist_songs(playlist_id):
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT 
            s.id, 
            s.title, 
            a.name AS artist_name, 
            s.album, 
            s.duration_seconds
        FROM playlist_songs ps
        JOIN songs s ON ps.song_id = s.id
        JOIN artists a ON s.artist_id = a.id
        WHERE ps.playlist_id = %s
    """, (playlist_id,))
    songs = cur.fetchall()
    cur.close()

    song_list = []
    for song in songs:
        song_list.append({
            "id": song[0],
            "title": song[1],
            "artist_name": song[2],
            "album": song[3],
            "duration_seconds": song[4]
        })
    return jsonify({"songs": song_list})

@app.route('/api/songs', methods=['POST'])
def add_song():
    data = request.get_json()
    title = data.get('title')
    artist_name = data.get('artist_name')
    album = data.get('album')
    duration_seconds = data.get('duration_seconds')

    if not title or not artist_name:
        return jsonify({"error": "Title and artist name are required"}), 400

    cur = mysql.connection.cursor()
    

    cur.execute("SELECT id FROM artists WHERE name = %s", (artist_name,))
    artist_result = cur.fetchone()
    if artist_result:
        artist_id = artist_result[0]
    else:
        cur.execute("INSERT INTO artists (name) VALUES (%s)", (artist_name,))
        mysql.connection.commit()
        artist_id = cur.lastrowid
        
    cur.execute("""
        INSERT INTO songs (title, artist_id, album, duration_seconds) 
        VALUES (%s, %s, %s, %s)
    """, (title, artist_id, album, duration_seconds))
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "Song added successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)