from .playlist import PlayList


class User:
    def __init__(self, username, password, email, subscription=False, **kwargs):
        self.username = username
        self.password = password
        self.email = email
        self.subscription = subscription
        self.like_songs = []
        self.playlists = {}

        for key, value in kwargs.items():
            setattr(self, key, value)

    def create_playlist(self, playlist_name):
        if playlist_name in self.playlists.keys():
            return f'{playlist_name} already exists'

        playlist = PlayList.create(playlist_name)
        self.playlists[playlist_name] = playlist
        return f'{playlist_name} has been created'