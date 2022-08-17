from models.user_premium import UserPremium
from constant.dua_lipa import lipa
from constant.minaj import minaj
from constant.bieber import bieber


print('\n')

print('----------------------------------')
print('----------------------------------')

print('user_premium section')

user_viviana = UserPremium('viviana', '12345', 'vivi@gmail.com')

print(user_viviana, 'user premium created')

print()

print(user_viviana.create_playlist('pop'))

print()

print(user_viviana.follow(lipa))

print(user_viviana.follow(bieber))

print()

print(user_viviana.like_song(lipa.albums['dualipa_deluxe'].songs_playlist[5]))

print(user_viviana.like_song(lipa.albums['dualipa_deluxe'].songs_playlist[1]))

print()

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

print()

user_viviana.playlists['pop'].del_song()

print()

user_viviana.playlists['liked_songs'].show_songs()

print('----------------------------------')
print('----------------------------------')