#Client Program
import socket,run

if __name__ == "__main__":
	client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #creates a TCP socket
	target = input("Enter the ip of the machine you wish to connect to")
	client.connect((target,1024))
	client.setblocking(False)
	print("Connected to machine")
	
	run.run(client)
	print("connection terminated")
	client.close()