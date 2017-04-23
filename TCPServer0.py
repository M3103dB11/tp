from socket import *
s = socket(AF_INET,SOCK_STREAM)
s.bind(('',13000))
s.listen(1)
s2 = socket(AF_INET,SOCK_STREAM)
s2.bind(('',14000))
s2.listen(1)

while 1:
	cs,addr =s.accept()#(cip,cport)
	print "connexion reçu"
	msg=cs.recv(2048)
	print "msg reçu"
	cs.send(msg)
	print "msg envoyé"
	#print addr [0],msg
	cs.close()
	print "connexionfermée"
	while True:
		(cs,(ip,port))=s2.accept()
		cs.send(msg)
		cs.close()