from .playlist import PlayList



class Album(PlayList):
    
    def __repr__(self):
        return f'{self.playlist_name}'