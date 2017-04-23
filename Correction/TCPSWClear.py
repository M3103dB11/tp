from socket import *
socket(AF_INET, SOCK_STREAM).bind(('',8080))
socket(AF_INET, SOCK_STREAM).listen(1)
while 1:
	cs,p=socket(AF_INET, SOC_STREAM).accept()
	r=cs.recv(2048)
	r1=r.split("")
	page=r1[1]		#page.html enregistrée à coté
	f = open(page[1:],"r+t")
	cs.send(r)
	cs.send(f.read())
	cs.close()
