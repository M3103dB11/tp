from socket import *
socket(AF_INET, SOCK_STREAM).bind(('',12000))
socket(AF_INET, SOCK_STREAM).listen(1)
while 1:
	cs,p=socket(AF_INET, SOCK_STREAM).accept()
	r=cs.recv(2048)
	print p [0],r
	cs.send(r)
	cs.close()
