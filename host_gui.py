import tkinter as tk
import app

if __name__ == "__main__":
    host_gui = app.App(is_host=True,master=tk.Tk())
    host_gui.read_message()
    host_gui.mainloop()
