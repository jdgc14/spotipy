from .post import Post


class Podcast(Post):
	def __init__(self, name, time, author, description):
		super().__init__(name, time, author)

		self.description = description