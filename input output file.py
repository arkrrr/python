# input output file 
# membuat file text

"""
w = write mode / mode menulis dan menghapus file lama, jika file lama tidak ada akan di buat file baru
r = read mode / hanya bisa membaca
a = appending mode / menambahkan data di akhir teks
r+ = read and write mode
"""

file = open("data.txt",'w')
file.write("ini adalah file teks yang di buat dengan python")
file.write("\nini baris kedua")
file.write("\nini baris ketiga")
file.write("\nini baris keempat")
file.write("\nini baris kelima")
file.close()

file2 = open("data.txt",'r')
#print (file.read(9))
print (file2.readline())

print (file2.readline())
file2.close()

# menambahkan data dengan appending
file4 = open("data.txt",'a')
file4.write("\nbaris ini di buat dengan appending")
file4.close()