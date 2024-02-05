from tkinter.ttk import *
from tkinter.messagebox import showerror, showinfo
import secrets
from datetime import datetime

from db.models import create_account
from extras.secrets import hashed_id

class signup_frame(Frame):
  def __init__(self, master: None) -> None:
    super().__init__(master)

    self.pack(fill='both', expand=True)

    Label(self, text="New user only").pack(fill='x')
    self.frame_one = Frame(self)
    self.frame_one.pack(fill='both', expand=1)

    self.lbl_1 = Label(self.frame_one, text="Username:")
    self.lbl_1.grid(row=0, column=0, sticky='w', pady=4)
    self.entry_1 = Entry(self.frame_one)
    self.entry_1.grid(row=0, column=1, sticky='w')

    self.lbl_2 = Label(self.frame_one, text='Password')
    self.lbl_2.grid(row=1, column=0, sticky='w', pady=4)
    self.entry_2 = Entry(self.frame_one, show='*')
    self.entry_2.grid(row=1, column=1, sticky='w')

    self.lbl_3 = Label(self.frame_one, text="Roles:")
    self.lbl_3.grid(row=2, column=0, sticky='w', pady=4)
    self.entry_3 = Entry(self.frame_one)
    self.entry_3.grid(row=2, column=1, sticky='w')

    self.lbl_4 = Label(self.frame_one, text="Name:")
    self.lbl_4.grid(row=3, column=0, sticky='w', pady=4)
    self.entry_4 = Entry(self.frame_one)
    self.entry_4.grid(row=3, column=1, sticky='w')

    self.lbl_5 = Label(self.frame_one, text="Surname:")
    self.lbl_5.grid(row=4, column=0, sticky='w', pady=4)
    self.entry_5 = Entry(self.frame_one)
    self.entry_5.grid(row=4, column=1, sticky='w')

    self.lbl_6 = Label(self.frame_one, text="Email:")
    self.lbl_6.grid(row=5, column=0, sticky='w', pady=4)
    self.entry_6 = Entry(self.frame_one)
    self.entry_6.grid(row=5, column=1, sticky='w')

    self.lbl_7 = Label(self.frame_one, text="Phone number:")
    self.lbl_7.grid(row=6, column=0, sticky='w', pady=4)
    self.entry_7 = Entry(self.frame_one)
    self.entry_7.grid(row=6, column=1, sticky='w')

    self.lbl_8 = Label(self.frame_one, text="Home address:")
    self.lbl_8.grid(row=7, column=0, sticky='w', pady=4)
    self.entry_8 = Entry(self.frame_one)
    self.entry_8.grid(row=7, column=1, sticky='w')

    self.lbl_9 = Label(self.frame_one, text="Position:")
    self.lbl_9.grid(row=8, column=0, sticky='w', pady=4)
    self.entry_9 = Entry(self.frame_one)
    self.entry_9.grid(row=8, column=1, sticky='w')

    self.login_btn = Button(self.frame_one, text="Create account", command=self.save)
    self.login_btn.grid(row=9, column=1, sticky='e', pady=4)

  def save(self):
    mode = create_account(db_name="chinonge", user_id=hashed_id(secrets.token_bytes(24)), user_name=self.entry_1.get().encode('utf-8'), password=self.entry_2.get().encode('utf-8'), roles=self.entry_3.get().encode('utf-8'), name=self.entry_4.get().encode('utf-8'), surname=self.entry_5.get().encode('utf-8'), email=self.entry_6.get().encode('utf-8'), phone_number=self.entry_7.get().encode('utf-8'), home_address=self.entry_8.get().encode('utf-8'), position=self.entry_9.get().encode('utf-8'), ts=datetime.now())
    if mode == "success":
      self.entry_1.delete(0, 'end')
      self.entry_2.delete(0, 'end')
    else:
      showerror('error',mode)
