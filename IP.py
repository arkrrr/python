import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Your computer Name is:" + hostname)
print("your computer ip address is " + IPAddr)