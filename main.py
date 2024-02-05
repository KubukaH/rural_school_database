import tkinter as tk
from tkinter.ttk import *

# local modules imports
from auth.index import auth_frames
from db.create_db import create_db
from main_codes.index import index_frame
from extras.user_cookie import user_cookie

school_name = "Chinonge"

class main_app(tk.Tk):
  def __init__(self) -> None:
    super().__init__()
    
    # windows settings
    self.resizable(0,0)
    self.title("school database")
    self.geometry("1312x704")

    # blank frames anchored to the parent (self)
    self.auth_blank = Frame(self)
    self.main_blank = Frame(self)

    if user_cookie() is not None:
      # working table
      self.main_blank.pack(fill='both', expand=1)
      self.wlc = index_frame(self.main_blank)
      self.wlc.pack(fill='both', expand=1)
    else:
      # authentication frames
      self.auth_blank.pack(fill='both', expand=1)
      self.authentication = auth_frames(self.auth_blank)
      self.authentication.pack(fill='both', expand=1)

# run the main app
if __name__ == '__main__':
  create_db(school_name.lower())
  app = main_app()
  app.mainloop()
