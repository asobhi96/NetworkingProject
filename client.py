#Client Program
import socket

def createClientSocket(ip='localhost'):
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #creates a TCP socket
    print("attempting to connect")
    client.connect((ip,1024))
    print("connected")
    client.setblocking(False)
    return client
