#Server program
import socket

def createServerSocket():
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #creates a TCP socket
    server_socket.bind(("0.0.0.0",1024))
    server_socket.listen(1)
    print("Listening")
    conn,addr = server_socket.accept()
    print("Accepted connection")
    conn.setblocking(False)
    return conn
