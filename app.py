from constant.dua_lipa import lipa, this_is_dualipa
from constant.minaj import minaj, this_is_minaj
from constant.bieber import bieber
from constant.user_jose import jose_user
from constant.user_viviana import user_viviana


print()

print('reproduction default_playlist by user free')

print()

jose_user.default_playlist(this_is_dualipa)

print('----------------------------------')
print('----------------------------------')

print()

print('reproduction default_playlist by user premium')

print()

user_viviana.default_playlist(this_is_minaj)

print('----------------------------------')
print('----------------------------------')

print(lipa)
print(lipa.get_followers())
lipa.get_albums()
print(lipa.numbers_songs())

print('----------------------------------')
print('----------------------------------')

print(minaj)
print(minaj.get_followers())
minaj.get_albums()
print(minaj.numbers_songs())

print('----------------------------------')
print('----------------------------------')

print(bieber)
print(bieber.get_followers())
bieber.get_albums()
print(bieber.numbers_songs())

print('----------------------------------')
print('----------------------------------')