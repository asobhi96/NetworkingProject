import tkinter as tk
import select,queue
import server,client

class App(tk.Frame):
    def __init__(self,is_host,master=None):
        self.master=master
        self.set_up_socket(is_host)
        self.create_widgets(master)

    def create_widgets(self,master):
        self.upper_frame = tk.Frame(master)
        self.upper_frame.pack()
        self.lower_frame = tk.Frame(master)
        self.lower_frame.pack()
        self.chat_log = tk.Text(self.upper_frame)
        self.chat_log.config(state=tk.DISABLED)
        self.chat_log.pack()
        self.message_buffer = tk.Text(self.lower_frame)
        self.message_buffer.pack()
        self.send_button = tk.Button(self.lower_frame,text="Send",command=self.send_message)
        self.send_button.pack(side=tk.LEFT)
        self.quit_button = tk.Button(self.lower_frame,text="Close",command=self.close_connection)
        self.quit_button.pack(side=tk.RIGHT)

    def set_up_socket(self,is_host):
        if is_host:
            self.connection = server.createServerSocket()
        else:
            target_ip = input("Enter the IP address of the machine you wish to connect to\n")
            self.connection = client.createClientSocket(target_ip)
        self.message_queue= queue.Queue()

    def close_connection(self):
        self.connection.close()
        self.master.destroy()


    def read_message(self):
        socket = self.connection
        r,_,_ = select.select([socket],[],[],.01)
        if socket in r:
            data = socket.recv(64).decode('ascii')
            if data:
                self.insert_to_chat_log(data,"Peer")
            else:
                socket.close()
                self.master.destroy()
        try:
            next_message = self.message_queue.get_nowait()
        except queue.Empty:
            pass
        else:
            socket.sendall(next_message.encode('ascii'))
        self.master.after(1,self.read_message)

    def send_message(self):
        buf = self.message_buffer.get(1.0,tk.END)
        if len(buf) > 1:
            self.message_queue.put(buf)
            self.message_buffer.delete(1.0,tk.END)
            self.insert_to_chat_log(buf,"You")

    def insert_to_chat_log(self,message,owner_name):
        self.chat_log.config(state=tk.NORMAL)
        self.chat_log.insert(tk.END,"{}: {}".format(owner_name,message))
        self.chat_log.config(state=tk.DISABLED)
