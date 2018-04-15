import sys,queue,select, socket

def run(socket):
	message_queues = {}
	message_queues[socket] = queue.Queue()
	message_queues[sys.stdout] = queue.Queue()
	standard_input = sys.stdin
	inpt = [standard_input,socket]
	output = []
	error = []
	while socket in inpt:
		r,w,e = select.select(inpt,output,error)
		for file in r:
			if file == standard_input:
				#if file to be read from is stdin, need to readfrom stdin and tell socket to send data
				message_queues[socket].put(file.readline().strip())
				if socket not in output:
					output.append(socket)
			else:
				#file to be read from is a socket, need to store data in a buffer for stdout
				data = file.recv(64).decode('ascii')
				if data:
					if data == 'stop':
						print("Connection ending")
						inpt.remove(socket)
						break
					message_queues[sys.stdout].put(data)
					if sys.stdout not in output:
						output.append(sys.stdout)
				else:
					#connection termianted (recviecved 0 bytes)
					inpt.remove(socket)
					break
		for file in w:
			try:
				nextmsg = message_queues[file].get_nowait()
			except queue.Empty:
				output.remove(file)
			else:
				if file == sys.stdout:
					print(nextmsg)
				else:
					file.sendall(nextmsg.encode('ascii'))
