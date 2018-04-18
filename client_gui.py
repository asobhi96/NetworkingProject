import tkinter as tk
import app
if __name__ == "__main__":
    client_gui = app.App(is_host=False,master=tk.Tk())
    client_gui.read_message()
    client_gui.mainloop()
