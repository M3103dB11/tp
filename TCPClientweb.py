from socket import *
sN = "www.meteofrance.com"
sP = 80
cS = socket(AF_INET, SOCK_STREAM)
cS.connect((sN,sP))
msg = "GET / HTTPS/1.1 \n\n"
cS.send(msg)
answer = cS.recv(1024)
print "From Sever:  ", answer
cS.close()