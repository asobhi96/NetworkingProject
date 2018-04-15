import tkinter as tk
import select,queue
import client
class App(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidgets(master)
        self.setUpClient()


    def createWidgets(self,master):
        self.upperFrame = tk.Frame(master)
        self.upperFrame.pack()
        self.lowerFrame = tk.Frame(master)
        self.lowerFrame.pack()
        self.chatLog = tk.Text(self.upperFrame)
        self.chatLog.pack()
        self.messageBuffer = tk.Text(self.lowerFrame)
        self.messageBuffer.pack()
        self.sendButton = tk.Button(self.lowerFrame,text="Send",command=self.sendMessage)
        self.sendButton.pack(side=tk.LEFT)
        self.quitButton = tk.Button(self.lowerFrame,text="Close",command=root.destroy)
        self.quitButton.pack(side=tk.RIGHT)

    def setUpClient(self):
        self.connection = client.createClientSocket()
        self.message_queue= queue.Queue()
        self.readyToWrite = False

    def readMessage(self):
        socket = self.connection
        try:
            r,w,e = select.select([socket],[],[],.01)
            if socket in r:
                data = socket.recv(64).decode('ascii')
                if data:
                    self.chatLog.insert(tk.END,"Peer:" + data)
                else:
                    socket.close()
            if self.readyToWrite:
                try:
                    nextmsg = self.message_queue.get_nowait()
                except queue.Empty:
                    self.readyToWrite = False
                else:
                    socket.sendall(nextmsg.encode('ascii'))
            self.master.after(1,self.readMessage)
        except ValueError:
            socket.close()

    def sendMessage(self):
        buf = self.messageBuffer.get(1.0,tk.END)
        if len(buf) > 1:
            self.message_queue.put(buf)
            if self.readyToWrite == False:
                self.readyToWrite = True
            self.messageBuffer.delete(1.0,tk.END)
            self.chatLog.insert(tk.END,"You:" + buf)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(master=root)
    app.readMessage()
    app.mainloop()
