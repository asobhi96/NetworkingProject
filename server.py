#Server program
import socket

def createServerSocket():
	server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #creates a TCP socket
	server_socket.bind(("0.0.0.0",1024))
	server_socket.listen(1)
	print("Listening on {}\n".format(server_socket.getsockname()))
	conn,addr = server_socket.accept()
	conn.setblocking(False)
	print("Connection esablished with {} at {}\n".format(conn.getsockname(),addr))
	return conn
