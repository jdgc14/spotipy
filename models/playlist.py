from .exceptions import MusicNotFound


class PlayList:
    def __init__(self, playlist_name):
        self.playlist_name = playlist_name
        self.songs_playlist = []

    def __str__(self):
        return f'{self.playlist_name}'

    @classmethod
    def create(cls, playlist_name):
        playlist = cls(playlist_name)
        return playlist

    def add_song(self, song):
        for melody in self.songs_playlist:
            if id(song) == id(melody):
                return 'this song has already been added\n'

        self.songs_playlist.append(song)
        return f'{song} added successfully to {self}\n'

    def del_song(self):
        self.show_songs()

        try:
            delete = int(input('Select song to delete\n'))
            if (delete > len(self.songs_playlist)) or (delete <=0):
                raise MusicNotFound()
            del self.songs_playlist[delete-1]
            print('the song has been deleted')
            self.show_songs()
            print()
            # return 

        except (MusicNotFound, ValueError):
            print()
            print('Invalid option try again.')
            print()
            return self.del_song()

    def enumerate_songs(self):
        return len(self.songs_playlist)


    def show_songs(self):
        print(f'{self}')
        for index, song in enumerate(self.songs_playlist, start=1):
            print(f'{index}. {song}')