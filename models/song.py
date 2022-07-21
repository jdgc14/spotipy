from .post import Post


class Song(Post):
	def __init__(self, name, time, author, lyrics, album=None):
		super().__init__(name, time, author)
		self.lyrics = lyrics
		if album:
			self.album = album
		else:
			self.album = 'none'

	def __str__(self):
		return f'{self.name}'

	def __repr__(self):
		return f'{self.name}'

	@classmethod
	def create(cls, name, time, author, lyrics, album=None):
		song = cls(name, time, author, lyrics, album)
		author.add_song(song, album)
		return song