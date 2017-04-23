from socket import *
sP = 8081
sS = socket(AF_INET,SOCK_STREAM)
sS.bind(('',sP))
sS.listen(1)
print "ready receive"

while True:
	cS, addr = sS.accept()
	req = cS.recv(1024)
	url = req.split(" ")
	page = url[1]
	page = page[1:]
	f = open(page,"r+t")
	cS.send(req)
	cS.send(f.read())
	cS.close()