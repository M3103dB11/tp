from socket import *
s = socket(AF_INET,SOCK_STREAM)
s.bind(('',8080))
s.listen(1)
#s2 = socket(AF_INET,SOCK_STREAM)
#s2.bind(('',14000))
#s2.listen(1)

while True:
	(cs,(cip,cport)=s.accept()
	#print "connexion reçu"
	req = cs.recv(2048)
	mots = req.split(" ")
	f = open(mots[1],"rtt")
	cs.send(f.read())
	cs.close()