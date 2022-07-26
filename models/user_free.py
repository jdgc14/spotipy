from .user import User
from .exceptions import PlaylistNotFound

from random import shuffle
from copy import deepcopy

class UserFree(User):
    

    def play_music(self):
        pass

    def play_playlist(self):
        for index, playlist_name in enumerate(self.playlists.keys(), start=1):
            print(f'{index}. {playlist_name}')

        
        try:
            playlist_to_play = input('What playlist name do you want to listening?')
            if playlist_to_play not in self.playlists.keys():
                raise PlaylistNotFound()

            playlist_copy = deepcopy(self.playlists[playlist_to_play].songs_playlist)
            shuffle(playlist_copy)
            
            for song in playlist_copy:
                print(song)

        except PlaylistNotFound:
            print(f'{playlist_to_play} does not exist')
            return self.play_playlist()


