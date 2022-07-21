


class PlayList:
    def __init__(self, playlist_name):
        self.playlist_name = playlist_name
        self.songs_playlist = []

    @classmethod
    def create(cls, playlist_name):
        playlist = cls(playlist_name)
        return playlist

    def add_song(self, song):
        for melody in self.songs_playlist:
            if id(song) == id(melody):
                return 'this song has already been added'

        self.songs_playlist.append(song)
        return 'song added successfully'

    def del_song(self):
        for index, melody in enumerate(self.songs_playlist, start=1):
            print(f'{index}. {melody}')
        #TODO:
        #Exception
        delete = int(input('Select song to delete'))
        del self.songs_playlist[delete-1]


    def enumerate_songs(self):
        return len(self.songs_playlist)