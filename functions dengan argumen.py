def siswa(nama):
   print ("nama siswa ini adalah :",nama)
   
siswa('arka')

# fungsi dengan menggunakan keywords argument
def guru(nama,pelajaran):
  print ("guru ini bernama :",nama)
  print ("mengaar pelajaran :",pelajaran)
  
guru(nama='nanang',pelajaran='matematika')

def penjagasekolah(nama,shift='siang',galak='tidak'):
  print ("penjaga sekolah ini adalah :",nama)
  print ("shiftnya ; ",shift)
  print ("galak? :",galak)
  
penjagasekolah('ipul')
penjagasekolah('ipul',shift='malam')
penjagasekolah('ipul',shift='malam',galak='iya')