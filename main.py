import tkinter as tk
from tkinter.ttk import *
from datetime import datetime
from os.path import relpath

# local modules imports
from auth.index import auth_frame
from main_codes.index import index_frame
from extras.user_cookie import user_cookie
from db.store_db_name import school_name
from db.get_db_name import get_db_name
from styles import make_styles

class ControlFrame(Frame):
  def __init__(self, container):
    super().__init__(container)

    self.selected_value = tk.IntVar()
    self.container = container

    # initialize frames
    self.frames = {}
    self.frame_zero = Frame(self.container)
    self.frames[0] = self.frame_zero

    self.frame_one = auth_frame(self.container)
    self.frames[1] = self.frame_one

    def chk():
      self.check_frame_number(self.selected_value)
      self.after(300, chk)
    
    self.after(300, chk)
    self.pack(fill='both', expand=1)
    if user_cookie() is not None and not self.selected_value.get() is int(1):
      self.frame_zero.pack()
      self.fram0 = index_frame(self.frame_zero)
      self.fram0.pack(fill='both', expand=1)
      self.selected_value.set(0)
    else:
      self.frame_one.pack(fill='both', expand=1)
      self.selected_value.set(1)
    #self.change_frame()
    self.pack(fill='both', expand=1)

  def change_frame(self):
    frame = self.frames[self.selected_value.get()]
    frame.tkraise()

  def check_frame_number(self, selected):
    if user_cookie() is not None:
      selected.set(0)
      #if index_frame(self.frame_zero).level_1_frame.sign_out_clicked.get() is True :
      #  selected.set(1)
      #else:
      #  selected.set(0)
    else:
      selected.set(1)
      #if selected.get() is not int(1):
      #  selected.set(0)
      #else:
      #  selected.set(1)
    self.change_frame()

# The APP class
class App(tk.Tk):
  def __init__(self):
    super().__init__()
    self.school_name = tk.StringVar()
    make_styles(self)

    with open(relpath("data_base/db_names.txt"), 'r') as f:
      sch = f.read()
      self.school_name.set(sch)

    self.title(f"{self.school_name.get().capitalize()} School")
    self.resizable(0,0)
    self.geometry("1312x704")

# run the main app
if __name__ == '__main__':
  app = App()
  if get_db_name() == "":
    wn1 = school_name(app)
    app.wait_window(wn1.top)
    app.destroy()
  else:
    ControlFrame(app)
  app.mainloop()
