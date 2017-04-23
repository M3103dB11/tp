from socket import *
serverPort = 12001
serverPort1 = 13000
serverPort2 = 14000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

serverSocket1 = socket(AF_INET,SOCK_STREAM)


while 1:
	print "The server TCP is ready to receive"
	connectionSocket, addr = serverSocket.accept()

	sentence = connectionSocket.recv(1024)
	capitalizedSentence = sentence.upper()
	connectionSocket.send(capitalizedSentence)
	print addr [0], capitalizedSentence
	print " "
	connectionSocket.close()

	serverSocket1.bind(('',serverPort1))
	serverSocket1.listen(1)
	connectionSocket1, addr = serverSocket1.accept()
	connectionSocket1.send(capitalizedSentence)
	print addr [0], capitalizedSentence
	print " "
	connectionSocket1.close()
	