from tkinter.ttk import *
from tkinter.messagebox import showerror, showinfo

from db.models import login

class login_frame(Frame):
  def __init__(self, master: None) -> None:
    super().__init__(master)

    self.pack(fill='both', expand=1)

    Label(self, text='Existing user sign in').pack(fill='x')
    
    self.frame_one = Frame(self)
    self.frame_one.pack(fill='both', expand=1)

    self.lbl_1 = Label(self.frame_one, text="Username:")
    self.lbl_1.grid(row=0, column=0, sticky='w', pady=4)
    self.entry_1 = Entry(self.frame_one)
    self.entry_1.focus()
    self.entry_1.grid(row=0, column=1, sticky='w')

    self.lbl_2 = Label(self.frame_one, text='Password')
    self.lbl_2.grid(row=1, column=0, sticky='w', pady=4)
    self.entry_2 = Entry(self.frame_one, show='*')
    self.entry_2.grid(row=1, column=1, sticky='w')

    self.login_btn = Button(self.frame_one, text="Login", command=self.connect)
    self.login_btn.bind("<Return>", self.connect)
    self.login_btn.grid(row=2, column=1, sticky='e', pady=4)

  def connect(self, event=None):
    cookie = login(user_name=self.entry_1.get().encode('utf-8'), password=self.entry_2.get().encode('utf-8'))
    if cookie is not None:
      self.reset()
    else:
      showerror('error', "Incorrect username or password")
  
  def reset(self):
    self.entry_1.delete(0, 'end')
    self.entry_2.delete(0, 'end')
