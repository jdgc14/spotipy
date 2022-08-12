from models.user_premium import UserPremium

from constant.dua_lipa import lipa
from constant.minaj import minaj
from constant.bieber import bieber


print('\n\n\n')
print('user premium')

user_viviana = UserPremium('viviana', '12345', 'vivi@gmail.com')

user_viviana.create_playlist('pop')

user_viviana.follow(lipa)
user_viviana.follow(bieber)


user_viviana.like_song(lipa.albums['dualipa_deluxe'].songs_playlist[5])

user_viviana.like_song(lipa.albums['dualipa_deluxe'].songs_playlist[1])

print(user_viviana.playlists['pop'].add_song(bieber.albums['changes'].songs_playlist[3]))
print(user_viviana.playlists['pop'].add_song(bieber.albums['changes'].songs_playlist[6]))
print(user_viviana.playlists['pop'].add_song(bieber.albums['changes'].songs_playlist[6]))
print(user_viviana.playlists['pop'].add_song(bieber.albums['changes'].songs_playlist[8]))
print(user_viviana.playlists['pop'].add_song(bieber.albums['changes'].songs_playlist[1]))
print(user_viviana.playlists['pop'].add_song(bieber.albums['changes'].songs_playlist[9]))
print(user_viviana.playlists['pop'].add_song(lipa.albums['dualipa_deluxe'].songs_playlist[9]))
print(user_viviana.playlists['pop'].add_song(lipa.albums['dualipa_deluxe'].songs_playlist[6]))
print(user_viviana.playlists['pop'].add_song(lipa.albums['dualipa_deluxe'].songs_playlist[2]))
print(user_viviana.playlists['pop'].add_song(lipa.albums['future_nostalgia'].songs_playlist[6]))
print(user_viviana.playlists['pop'].add_song(lipa.albums['future_nostalgia'].songs_playlist[2]))
print(user_viviana.playlists['pop'].add_song(lipa.albums['future_nostalgia'].songs_playlist[6]))
print(user_viviana.playlists['pop'].add_song(lipa.albums['future_nostalgia'].songs_playlist[9]))

# user_viviana.playlists['pop'].del_song()

user_viviana.playlists['pop'].show_songs()

user_viviana.play_playlist()