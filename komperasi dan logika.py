# episode latihan logika dan kompersi
# membuat angka atau rentang angka
# +++++++3-------10++++++++

inputUser = float(input("Masukkan angka yang kurang\n dari 3 atau \nlebih besar dari 10:"))
# ++++++3---------------
# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print ("Kurang dari 3 = ",isKurangDari)

# -------10+++++++++++=
# memriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print ("Lebih dari 10 = ",isLebihDari)

# +++++++3-------10++++++++
isCorrect = isKurangDari or isKurangDari
print ("angka yang anda masukkan",isCorrect)

print ("\n",20*"=","\n")
# ---------3+++++++++10---------
# kasus irisaan
inputUser = float(input("Masukkan angka yang\n lebih dari 3 dan \nkurang dari 10:"))

# ----3++++++++++++
# lebih dari 3
isLebihDari = inputUser > 3
print ("Lebih dari 3 = ",isLebihDari)

# +++++++++++10----
# kurang dari 10
isKurangDari = inputUser < 10
print ("Kurang dari 10 = ", isKurangDari)

#  ---------3+++++++++10---------
isCorrect = isKurangDari and isKurangDari
print ("angka yang anda masukkan",isCorrect)
