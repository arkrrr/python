def suaraayam():
  print ("kukuruyuk!!!!"*3)
  
def hargaayam():
  suaraayam()
  print ("harga ayam per kilo adalah Rp.20.000")
 # fungsi dengan input argumen 
def hargatotal(kg):
  suaraayam()
  harga = 20000
  hargaTotal = harga*kg  
  print ("harga",kg,"kg ayam adalah",hargaTotal)
  
hargaayam()
hargatotal(2)
hargatotal(3)
hargatotal(0.5)
hargatotal(4)