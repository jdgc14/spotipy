from .playlist import PlayList


class User:
    def __init__(self, username, password, email, subscription=False, **kwargs):
        self.username = username
        self.password = password
        self.email = email
        self.subscription = subscription
        self.playlists = {'liked_songs':PlayList.create('Liked Songs')}
        self.following = []

        for key, value in kwargs.items():
            setattr(self, key, value)

    def create_playlist(self, playlist_name):
        if playlist_name in self.playlists.keys():
            return f'{playlist_name} already exists'

        playlist = PlayList.create(playlist_name)
        self.playlists[playlist_name] = playlist
        return f'{playlist_name} has been created'


    def like_song(self, song):
        if song in self.playlists['liked_songs'].songs_playlist:
            return self.dislike_song(song)
        return self.playlists['liked_songs'].add_song(song)

    def dislike_song(self, song):
        self.playlists['liked_songs'].songs_playlist.remove(song)
        return 'dislike'

    def follow(self, author):
        if author in self.following:
            return self.unfollow(author)
        author.followers += 1
        self.following.append(author)

    def unfollow(self, author):
        author.followers -= 1
        self.following.remove(author)
        return 'unfollow'

    def show_playlists(self):
        for playlist_name in self.playlists.keys():
            print(f'• {playlist_name}')

    @staticmethod
    def default_playlist(playlist):
        for song in playlist.songs_playlist:
            song.play()