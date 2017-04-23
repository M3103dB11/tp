from socket import *
socket(AF_INET, SOCK_STREAM).connect(("www.meteofrance.com",80)
socket(AF_INET, SOCK_STREAM).send("GET / HTTPS/1.1 \n\n")
print socket(AF_INET, SOCK_STREAM).recv(1024)
socket(AF_INET, SOCK_STREAM).close()
