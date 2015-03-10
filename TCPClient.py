#coding=utf-8
from socket import *

serverName = 'localhost'
serverPort = 12345
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

message = raw_input('input a message')
clientSocket.send(message)

receiveMessage = clientSocket.recv(1024)
print receiveMessage
clientSocket.close()
