from socket import *
while 1:
	socket(AF_INET, SOCK_STREAM).connect(('localhost',13000))
	s=raw_input('LOL : ')
	socket(AF_INET, SOCK_STREAM).send(s)
	m=socket(AF_INET, SOCK_STREAM).recv(2048)
	socket(AF_INET, SOCK_STREAM).close()
