from socket import *

serverName = 'localhost'
serverPort = 12345
clientSocket = socket(AF_INET,SOCK_DGRAM)
message = raw_input('input message to server')

clientSocket.sendto(message, (serverName,serverPort))
messageFromServer,serverAddress = clientSocket.recvfrom(2048)
print messageFromServer
clientSocket.close()
