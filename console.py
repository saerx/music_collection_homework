import pdb
from models.album import Album 
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.delete_all()
artist_repository.delete_all()

CSS = Artist("CSS")
artist_repository.save(CSS)

eponymous_css = Album(CSS, "Cansei de Ser Sexy", "electroclash")
album_repository.save(eponymous_css)

pdb.set_trace()
