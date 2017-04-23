from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print "The server TCP is ready to receive"
while 1:

	if((connectionSocket, addr = serverSocket.accept()) == 1)
		sentence = connectionSocket.recv(1024)
		capitalizedSentence = sentence.upper()
	
		connectionSocket.send(capitalizedSentence)
		print addr [0], sentence
		print " "
		connectionSocket.close()