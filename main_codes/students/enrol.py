import random
from tkinter.ttk import *
from tkinter.messagebox import showerror, showinfo
import secrets
from datetime import datetime
import time

from db.models import search_student, student_enrolment

class enrol_student(Frame):
  def __init__(self, master: None) -> None:
    super().__init__(master, padding=8)

    self.regn = LabelFrame(self, name="registration_number", text="Registration Number", padding=8, labelanchor='nw')
    self.regn.pack(side='top', fill='x', padx=8, pady=8)
    Label(self.regn, text=self.gen_sid(), relief='flat').pack()

    self.frame_one = Frame(self)
    self.frame_one.pack(fill='both', expand=1)

    self.lbl_1 = Label(self.frame_one, text="Names of pupil")
    self.lbl_1.grid(row=0, column=0, sticky='w', pady=4)
    self.entry_1 = Entry(self.frame_one)
    self.entry_1.grid(row=0, column=1, sticky='w')

    self.lbl_2 = Label(self.frame_one, text='Date of birth')
    self.lbl_2.grid(row=1, column=0, sticky='w', pady=4)
    self.entry_2 = Entry(self.frame_one)
    self.entry_2.grid(row=1, column=1, sticky='w')

    self.lbl_3 = Label(self.frame_one, text="Birth entry number")
    self.lbl_3.grid(row=2, column=0, sticky='w', pady=4)
    self.entry_3 = Entry(self.frame_one)
    self.entry_3.grid(row=2, column=1, sticky='w')

    self.lbl_4 = Label(self.frame_one, text="Gender")
    self.lbl_4.grid(row=3, column=0, sticky='w', pady=4)
    self.entry_4 = Entry(self.frame_one)
    self.entry_4.grid(row=3, column=1, sticky='w')

    self.lbl_5 = Label(self.frame_one, text="Home address")
    self.lbl_5.grid(row=4, column=0, sticky='w', pady=4)
    self.entry_5 = Entry(self.frame_one)
    self.entry_5.grid(row=4, column=1, sticky='w')

    self.lbl_6 = Label(self.frame_one, text="Parent/Guardian names")
    self.lbl_6.grid(row=5, column=0, sticky='w', pady=4)
    self.entry_6 = Entry(self.frame_one)
    self.entry_6.grid(row=5, column=1, sticky='w')

    self.lbl_7 = Label(self.frame_one, text="Phone number:")
    self.lbl_7.grid(row=6, column=0, sticky='w', pady=4)
    self.entry_7 = Entry(self.frame_one)
    self.entry_7.grid(row=6, column=1, sticky='w')

    self.lbl_8 = Label(self.frame_one, text="Class")
    self.lbl_8.grid(row=7, column=0, sticky='w', pady=4)
    self.entry_8 = Entry(self.frame_one)
    self.entry_8.grid(row=7, column=1, sticky='w')

    self.lbl_9 = Label(self.frame_one, text="Sports")
    self.lbl_9.grid(row=8, column=0, sticky='w', pady=4)
    self.entry_9 = Entry(self.frame_one)
    self.entry_9.grid(row=8, column=1, sticky='w')

    self.lbl_10 = Label(self.frame_one, text="Other details")
    self.lbl_10.grid(row=9, column=0, sticky='w', pady=4)
    self.entry_10 = Entry(self.frame_one)
    self.entry_10.grid(row=9, column=1, sticky='w')

    self.login_btn = Button(self.frame_one, text="Enrol", command=self.save)
    self.login_btn.grid(row=10, column=1, sticky='e', pady=4)

    self.gen_sid()
  # generate randon ids and make strings
  def gen_sid(self):
    rand = random.randint(10,99)
    randl = random.choice('abcdefghjklmnpqrstuvwxyz')

    return f"{rand}{randl.upper()}-{time.strftime('%Y')[2:]}"
  
  def check_exists(self):
    new_sid = self.gen_sid()
    existing_sid = search_student('chinonge', new_sid)

  def save(self):
    if self.entry_1.get() != '':
      mode = student_enrolment(db_name="chinonge", school_id=self.gen_sid(), names=self.entry_1.get().encode('utf-8'), date_of_birth=self.entry_2.get().encode('utf-8'), entry_number=self.entry_3.get().encode('utf-8'), gender=self.entry_4.get().encode('utf-8'), address=self.entry_5.get().encode('utf-8'), class_grade=self.entry_6.get().encode('utf-8'), parent_names=self.entry_7.get().encode('utf-8'), parent_phone_number=self.entry_8.get().encode('utf-8'), sports=self.entry_9.get().encode('utf-8'), other_details=self.entry_10.get().encode('utf-8'), ts=datetime.now())
      if mode == "success":
        self.entry_1.delete(0, 'end')
        self.entry_2.delete(0, 'end')
      else:
        showerror('error',mode)
    else:
      showerror('', "Blank form, please add information.")
