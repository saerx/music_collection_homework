from models.artist import Artist
from models.album import Album
from db.run_sql import run_sql
import repositories.artist_repository as artist_repository


#CREATE 

def save(album):
    sql = "INSERT INTO albums (artist_id, title, genre) VALUES (%s, %s, %s) RETURNING id"
    values = [album.artist.id, album.title, album.genre]
    results = run_sql(sql, values)
    id = results[0]["id"]
    album.id = id
    return album

#READ
def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(artist, row['title'], row['genre'], row['id'])
        albums.append(album)
    return albums

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)
    if result is not None:
        artist_id = result['artist_id']
        artist = artist_repository.select(artist_id)
        album = Album(artist, result['title'], result['genre'])
    return album

#UPDATE
def update(album):
    sql = "UPDATE albums SET (artist_id, title, genre) = (%s, %s, %s) WHERE id = %s"
    values = [album.artist.id, album.title, album.genre]
    run_sql(sql, values)

#DELETE 

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)
