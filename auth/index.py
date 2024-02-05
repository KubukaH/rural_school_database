from tkinter.ttk import *

from .login import login_frame
from .signup import signup_frame
from terms_of_use import tou

def auth_frames(root):
  auth_frame = Frame(root)
  
  # Notebooks
  notebook = Notebook(auth_frame)
  notebook.pack(fill='both', expand=1, padx=2, pady=2)

  # Authentication frames
  lfrm = login_frame(auth_frame)
  sfrm = signup_frame(auth_frame)
  tfrm = tou(auth_frame)

  notebook.add(lfrm, text="User, sign in")
  notebook.add(sfrm, text="New user sign up")
  notebook.add(tfrm, text="Terms of use")

  return auth_frame