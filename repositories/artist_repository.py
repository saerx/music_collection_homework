from models.artist import Artist
from models.album import Album
from db.run_sql import run_sql

# CREATE
def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING id
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
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        artist = Artist(result['name'], result['id'])
    return artist


#DELETE

def delete_all():
    sql = "DELETE * FROM users"
    run_sql(sql)

def delete(id):
    sql = "DELETE * FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)





