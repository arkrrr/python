from getpass import getpass
# meminta input dari user
user1 = getpass('Pilih (gunting/batu/kertas): ')
user2 = getpass('pilih (gunting/batu/kertas):')

# melakukan perbandingan
if user1 == 'gunting' and user2 == 'batu':
    print ('user1 kalah')
    print ('user2 menang')
elif user1 == 'batu' and user2 == 'gunting':
    print ('user1 menang')
    print ('user2 kalah')
elif user1 == 'gunting'  and user2 == 'gunting':
    print ('seri')
elif user1 == 'kertas' and user2 == 'gunting':
    print ('user1 kalah')
    print ('user2 menang')
elif user1 == 'gunting' and user2 == 'kertas':
    print ('user1 menang')
    print ('user2 kalah')
elif user1 == 'kertas' and user2 == 'kertas':
    print ('seri')
elif user1 == 'kertas' and user2 == 'batu':
    print ('user1 menang')
    print ('user2 kalah')
elif user1 == 'batu' and user2 == 'kertas':
    print ('user1 kalah')
    print ('user2 menang')
elif user1 == 'batu' and user2 == 'batu':
    print ('seri')

else:
    print ('salah pilih')
