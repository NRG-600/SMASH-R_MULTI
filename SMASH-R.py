from tkinter import *
from tkinter.ttk import *

import hashlib
import logging

root_app = Tk()
root_app.title('SMASH-R_MULTI')
root_app.geometry("400x400")

# Setting and packing (Showing) frame for our main application
root_frame = Frame(root_app)
root_frame.pack(expand=True, fill=BOTH, side='nwes')

root_app.mainloop()
