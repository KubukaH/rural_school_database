from tkinter.ttk import *

from .login import login_frame
from .signup import signup_frame
from terms_of_use import tou
from extras.user_cookie import user_cookie

class auth_frame(Frame):
  def __init__(self, master: None) -> None: 
    super().__init__(master)
    

    self.after(300, self.check_cookie)
    
    # Notebooks
    notebook = Notebook(self)
    notebook.pack(fill='both', expand=1, padx=2, pady=2)

    # Authentication frames
    lfrm = login_frame(self)
    sfrm = signup_frame(self)
    tfrm = tou(self)

    notebook.add(lfrm, text="User, sign in")
    notebook.add(sfrm, text="New user sign up")
    notebook.add(tfrm, text="Terms of use")

  def check_cookie(self):
    self.after(300, self.check_cookie)
    if user_cookie() is not None:
      self.pack_forget()
    else:
      self.pack(fill='both', expand=1)
