from socket import *
serverName = 'localhost'
clientSocket = socket(AF_INET, SOCK_STREAM)
#serverName2 = '10.98.2.90'
serverPort = 13000
while 1:
	
	clientSocket.connect((serverName,serverPort))
	sentence = raw_input('Input lowercase sentence:')
	clientSocket.send(sentence)
	modifiedSentence = clientSocket.recv(2048)
	#print 'From Server:', modifiedSentence
	clientSocket.close()
	



#clientSocket = socket(AF_INET, SOCK_STREAM)
#	clientSocket.connect((serverName2,serverPort))
#	sentence = raw_input('Input server aurelien:')
#	clientSocket.send(sentence)
#	modifiedSentence = clientSocket.recv(1024)
	#print 'From Server aurelien :', modifiedSentence
#	clientSocket.close()