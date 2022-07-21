from models.user_free import UserFree
from models.user_premium import UserPremium
from models.playlist import PlayList
from models.artist import Artist
from models.song import Song



print('user free create')
uf = UserFree('jose', '12345', 'email@email.com')
print(uf.username)
print(uf.subscription)
print()

print('user premium create')
up = UserPremium('viviana', '12345', 'vivi@gmail.com')
print(up.username)
print(up.subscription)
print()

# print('playlist create')
# pl = PlayList('primera playlist')
# print(pl.playlist_name)
# pl.add_song('nada')
# pl.add_song('hola')
# print(pl.songs_playlist)
# print(pl.enumerate_songs())

print('artist create')
artist1 = Artist(username='artista1', password='1234', email='artista1@mail.com', subscription=True, biography='soy la biografia')
print('name artist', artist1.username)
print(artist1.biography)
print('lista de canciones', artist1.albums)
print(artist1.get_followers())

print('\n\n')
print('song create')
song1 = Song.create(name='mi cancion', time=180, author=artist1, lyrics='letra de la cancion1', album='album1')
print(song1.name)
print(song1.lyrics)
print(song1.time)
print(song1.author)
print(artist1.albums)

print('\n\n')
print('song create')
song2 = Song.create(name='mi cancion2', time=100, author=artist1, lyrics='letra de la cancion2', album='album1')
print(song2.name)
print(song2.lyrics)
print(song2.time)
print(song2.author)
print(artist1.albums)

print('\n\n')
print('song create')
song3 = Song.create(name='mi cancion3', time=120, author=artist1, lyrics='letra de la cancion2', album='album2')
print(song3.name)
print(song3.lyrics)
print(song3.time)
print(song3.author)
print(artist1.albums)
print(artist1.numbers_songs())


print(uf.create_playlist('mi_playlist'))
print(uf.playlists)
print(uf.create_playlist('mi_playlist'))
print(uf.playlists['mi_playlist'].add_song(song1))
print(uf.playlists['mi_playlist'].songs_playlist)
print(uf.playlists['mi_playlist'].add_song(song2))
print(uf.playlists['mi_playlist'].songs_playlist)
print(uf.playlists['mi_playlist'].add_song(song3))
print(uf.playlists['mi_playlist'].songs_playlist)
print(uf.playlists['mi_playlist'].del_song())
print(uf.playlists['mi_playlist'].songs_playlist)
print('hola')