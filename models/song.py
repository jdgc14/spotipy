import time

from .post import Post



class Song(Post):
	def __init__(self, name, time, author, lyrics=None, album=None):
		super().__init__(name, time, author)
		if lyrics:
			self.lyrics = lyrics
		else: self.lyrics = f'lycrics {self.name}'
		if album:
			self.album = album
		else:
			self.album = 'none'

	def __str__(self):
		return f'{self.name}'

	def __repr__(self):
		return f'{self.name}'

	@classmethod
	def create(cls, name, time, author, lyrics=None, album=None):
		song = cls(name, time, author, lyrics, album)
		author.add_song(song, album)
		return song

	def play(self):
		time.sleep(0.7)
		print('{} by {}'.format(self.name, self.author.biography['name']))
		print()
		# print(self.lyrics)
		# print()