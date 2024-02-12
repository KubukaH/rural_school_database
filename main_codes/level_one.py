from tkinter.ttk import *
import tkinter as tk
import time
from tkinter.messagebox import showwarning

from db.models import logout
from extras.user_cookie import user_cookie
from .students.enrol import enrol_student
from .students.lists import class_lists

class level_one_frame(Frame):
  def __init__(self, master: None) -> None:
    super().__init__(master)

    self.user = user_cookie()
    self.sign_out_clicked = tk.BooleanVar(value=False)

    self.notebook = Notebook(self)
    self.notebook.pack(fill='both', expand=1)

    # home frame with all tools for level one user
    self.home_frm = Frame(self, padding=4)
    self.home_frm.pack(fill='both', expand=1)

    # frames with grids
    self.blank_grid_frm = Frame(self.home_frm)
    self.blank_grid_frm.pack(fill='both', expand=1)

    # widgets inside the home blank_grid_frame
    self.add_student_btn = Button(self.blank_grid_frm, text='Add Student', command=self.add_enrol_event)
    self.add_student_btn.grid(row=0, column=0, ipadx=1, ipady=2, pady=32, padx=16)
    self.view_students_btn = Button(self.blank_grid_frm, text='View Students', command=self.view_lists_event)
    self.view_students_btn.grid(row=0, column=1, ipadx=1, ipady=2, pady=32, padx=16)

    # frame for end elements such as signout and licences labels
    self.end_frm = Frame(self, border=1, height=8, borderwidth=2, relief='sunken', padding=2)
    self.end_frm.pack(fill='x', side='bottom', anchor='sw', padx=2, pady=(0,2))
    Label(self.end_frm, text=f"© Copyright {time.strftime('%Y')} - Kubuka Space PBC").pack(side='left')
    Button(self.end_frm, text="Sign Out", command=self.sign_out, style="Logout.TButton").pack(fill='y', side='right')

    self.notebook.add(self.home_frm, text=f"Welcome {self.user[2].decode('utf-8').capitalize()} {self.user[3].decode('utf-8').capitalize()}")

    # enrol new student widgets
    self.enrol_frm = enrol_student(self)
    self.enrol_frm.pack(fill='both', expand=1)
    self.notebook.add(self.enrol_frm, text="Enrol new student")

    self.view_ls = class_lists(self)
    self.view_ls.pack(fill='both', expand=1)
    self.notebook.add(self.view_ls, text="View students")

  def add_enrol_event(self):
    self.notebook.select(self.enrol_frm)
  
  def view_lists_event(self):
    self.notebook.select(self.view_ls)

  def sign_out(self):
    res = logout(self.user.cookie_id)
    if res != 'done':
      showwarning("Uh oh!", res)
    else:
      while self.notebook.index('end'):
        self.notebook.forget(0)
      self.sign_out_clicked.set(True)
      #self.pack_forget()
