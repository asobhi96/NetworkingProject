#Server program
import socket, run

if __name__ == "__main__":
	server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #creates a TCP socket
	server_socket.bind(("0.0.0.0",1024))
	server_socket.listen(1)
	print("Listening on {}\n".format(server_socket.getsockname()))

	client,addr = server_socket.accept()
	client.setblocking(False)
	print("Connection esablished with {} at {}\n".format(client.getsockname(),addr))
	
	run.run(client)
	
	print("Connection terminated")
	client.close()
	server_socket.close()
