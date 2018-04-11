def sendmessage(peer):
	msg = ''
	while msg != "stop":
		msg = input("Enter a message to send:\n")
		sent = peer.sendall(msg.encode('ascii'))
		if sent is not None:
			print("Connection ended")
			break
		else:
			print("Sent {} \n".format(msg))
			sel.register(peer,selectors.EVENT_READ,readmessage)
	print("Sending stopping")


def readmessage(connection):
	msg = ''
	while msg != "stop":
		msg = connection.recv(64).decode('ascii')
		if msg == '':
			print("Connection termianted")
			break
		else:
			print(msg)
		