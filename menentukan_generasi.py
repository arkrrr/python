nama = input('Masukkan nama anda: ')
tahun = int(input('Tahun berapa anda lahir: '))




if tahun <= 1964:
    print (f'{nama} berdasarkan tanggal lahir anda, anda termasuk generasi Baby boomer')
elif tahun <= 1979:
    print (f'{nama} berdasarkan tanggal lahir anda, anda termasuk generasi X')
elif tahun <= 1994:
    print (f'{nama} berdasarkan  tanggal lahir anda, anda termasuk generasi Y (milenials)')
elif tahun <= 2015:
    print (f'{nama} berdasarkan tanggal lahir anda, anda termasuk generasi Z')
else:
    print ('salah pilih')
