from .user import User
from .exceptions import PlaylistNotFound, InvalidOption
from random import shuffle
from copy import deepcopy



class UserPremium(User):
    def __init__(self, username, password, email, subscription=True, **kwargs):
        super().__init__(username, password, email, subscription, **kwargs)


    def play_playlist(self):
        
        for index, playlist_name in enumerate(self.playlists.keys(), start=1):
            print(f'{index}. {playlist_name}')

        try:
            playlist_to_play = input('What playlist name do you want to listening?')
            if playlist_to_play not in self.playlists.keys():
                raise PlaylistNotFound()

        except PlaylistNotFound:
            print(f'{playlist_to_play} does not exist')
            return self.play_playlist()


        mode_reproduction = 0
        
        playlist_copy = deepcopy(self.playlists[playlist_to_play])
        
        while True:
            try:
                print('1. Random Paylist\n2. Select Song\n3. Normal Reproduction')
                mode_reproduction = int(input('-> '))
                if (mode_reproduction < 1) or (mode_reproduction > 3):
                    raise InvalidOption
                break

            except (InvalidOption, ValueError):
                print('Invalid option, try')
                continue

        if mode_reproduction == 1:   
            shuffle(playlist_copy.songs_playlist)

        elif mode_reproduction == 2:
            playlist_copy.show_songs()
            song_start = int(input('Select number song: '))
            first_half = playlist_copy.songs_playlist[song_start:]
            second_half = playlist_copy.songs_playlist[:song_start]
            first_half.extend(second_half)
            playlist_copy.songs_playlist = first_half

        for song in playlist_copy.songs_playlist:
            print(song)




