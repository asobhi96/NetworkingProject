#Client Program
import socket

def createClientSocket():
	client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #creates a TCP socket
	client.connect(('127.0.0.1',1024))
	client.setblocking(False)
	print("Connected to machine")
	return client
