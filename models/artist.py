from .user import User


class Artist(User):
	def __init__(self, biography, username, password, email, subscription, **kwargs):
		super().__init__(username, password, email, subscription, **kwargs)
		self.biography = biography
		self.albums = {'none':[]}
		self.followers = 0

	def __str__(self):
		return f'{self.username}'

	def add_song(self, song, album=None):
		if album:
			self.add_album(album)
			return self.albums[album].append(song) 
		return self.albums['none'].append(song)

	def add_album(self, album_name):
		if album_name in self.albums.keys():
			return ('El album ya existe')
		self.albums[album_name] = []

	def get_followers(self):
		return self.followers

	def numbers_songs(self):
		numbers_songs = 0
		for album in self.albums.values():
			numbers_songs += len(album)
		return numbers_songs