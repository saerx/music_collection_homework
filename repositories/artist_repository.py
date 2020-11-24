from models.artist import Artist
from models.album import Album
from db.run_sql import run_sql

# CREATE
def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING id"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]["id"]
    artist.id = id
    return artist

#READ

def select_all():
    artists = []
    sql = "SELECT * FROM artists"
    results = run_sql(sql)
    for row in results:
        artist = Artist(row['name'], row['id'])
        artists.append(artist)
    return artists

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        artist = Artist(result['name'], result['id'])
    return artist

#UPDATE

def update(artist):
    sql = "UPDATE artists SET ('name') = (%s) WHERE id = %s"
    values = [artist.title, artist.id]
    run_sql(sql, values)


#DELETE

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)


#OTHER

def get_albums_by_artist(artist):
    sql = "SELECT * FROM artists WHERE artist_id = %s"
    values = [artist.id]
    results = run_sql(sql, values)

    artists_albums = []

    for row_data in results:
        album = Album(
            artist,
            row_data["title"],
            row_data["genre"],
            row_data["id"]        
            )
        artists_albums.append(album)

    return artists_albums


