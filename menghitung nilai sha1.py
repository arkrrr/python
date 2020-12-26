import hashlib
plaintext=input("Nilai string:")
sha = hashlib.sha1()
sha.update(plaintext.encode("ascii"))
print("Nilai hash sha1:", sha.hexdigest())