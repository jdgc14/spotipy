from .user_premium import UserPremium
from .album import Album

from .song import Song


class Artist(UserPremium):
	def __init__(self, username, password, email, biography, subscription=True, **kwargs):
		super().__init__(username, password, email, subscription, **kwargs)
		self.biography = biography
		self.albums = {'singles' : Album.create('singles')}
		self.followers = 0

	def __str__(self):
		return f'{self.username}'

	def add_song(self, song, album=None):
		if album:
			self.add_album(album)
			return self.albums[album].add_song(song)
		return self.albums['singles'].add_song(song)
	
	def add_album_songs(self, album_name, list_music):
		self.add_album(album_name)
		for song in list_music:
			Song.create(song[0], song[1], self, album=album_name)

	def add_album(self, album_name):
		if album_name in self.albums.keys():
			return 'The album already exists'
		self.albums[album_name] = Album.create(album_name)
		return f'{album_name} has been created'

	def get_followers(self):
		return f'numbers of followers: {self.followers}'

	def numbers_songs(self):
		numbers_songs = 0
		for album in self.albums:
			numbers_songs += self.albums[album].enumerate_songs()
		return numbers_songs