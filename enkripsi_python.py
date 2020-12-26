import os 
import marshal

class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
def main():
# untuk meng clear text di terminal
  os.system("clear")

# input file
  file = input("\033[94mfile python >\033[95m")

# baca isi file
  baca = open(file, "r").read()

# compile file yang sudah di baca
  com = compile(baca, "","exec")

# encrypt file yang sudah di compile dengan marshal
  encrypt = marshal.dumps(com)

# membuat file yg sudah di complie dengan marshal
  baru = open("enc_"+str(file),"w")

# print kode marshal untuk bisa di gunakan
  baru.write("import marshal\n")
  baru.write("exec(marshal.loads("+repr(encrypt)+"))")

# jika berhasil
  print (bcolors.OKGREEN,"berhasil di encrypt | file sava as enc_"+str(file))
main()