nilai = 60

if 88 <= nilai <= 100:
  print ("Nilai anda A") 
elif 70 <= nilai < 80:
  print ("Nilai anda B") 
elif 60 <= nilai < 70:
  print ("Nilai anda C")
elif 50 <= nilai < 60:
  print ("Nilai anda D, lakukan perbaikan")
else:
  print ("Maaf anda tidak lulus")
 
print (100*"+")
print ("Operator untuk list dan string")
print (" ")
gorengan = ["bakwan","pisang goreng","pukis","tahu","bala-bala","cireng","ubi"]
beli = "bakwan"
if beli in gorengan:
  print ('Mamang bilang "Ya saya jual"',beli )
if not beli in gorengan:
  print ('Saya ga jual',beli) 
karakter = "z"
if karakter in beli:
  print ("ada",karakter,"di",beli)
else:
  print ("tidak ada",karakter,"di",beli)