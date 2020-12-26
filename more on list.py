barang = ["kunci","jaket","mobil","motor","baju"]
print (barang)

#  menambah data list
barang.append("sepeda")
print(barang)

barang.extend("tas")
print (barang)

barang.insert(3,"dompet")
print (barang)

 #  meethod umtuk menghitung anggota
jumlahSepeda = barang.count("sepeda")
print ("jumlah sepeda adalah",jumlahSepeda)

#  meremove list
barang.remove("sepeda")
print (barang)

#  membalikkan list
barang.reverse()
print(barang)

stuff = barang.copy()
stuff.append("gelas")
print (stuff)
print (barang)