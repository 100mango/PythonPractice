#coding=utf-8
from socket import *

serverName = 'localhost'
serverPort = 12345
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverName,serverPort))
serverSocket.listen(1)

while True:
	connectionSocket,addr = serverSocket.accept()
	receiveMessage = connectionSocket.recv(1024)
	if receiveMessage == 'close':
		connectionSocket.send('bye')
		connectionSocket.close()
		serverSocket.close()
		break
	else:
		connectionSocket.sned('hello')