import tkinter as tk
from tkinter.ttk import *

from db.models import search_student, get_all_students

class class_lists(Frame):
  def __init__(self, master: None) -> None:
    super().__init__(master, padding=8)

    # frame holding elements in this section
    self.lv_fram = Frame(self)
    self.lv_fram.pack(fill='both', expand=1)

    # treeview 
    self.list_of_students = Treeview(self.lv_fram)

    # scrollbars
    self.lv_scbar = Scrollbar(self.lv_fram, command=self.list_of_students.yview)
    self.lv_scbar.pack(side='right', fill='y')
    self.lv_b_scbar = Scrollbar(self.lv_fram, orient=tk.HORIZONTAL, command=self.list_of_students.xview)
    self.lv_b_scbar.pack(fill='x', side='bottom')

    # set scrollbar to treeview
    self.list_of_students['xscrollcommand'] = self.lv_b_scbar.set
    self.list_of_students['yscrollcommand'] = self.lv_scbar.set
    
    # treeview columns defintion
    self.list_of_students['columns'] = ('school_id', 'names', 'date_of_birth', 'entry_number', 'gender', 'address', 'class', 'parent_names', 'parent_phone_number', 'sports', 'other_details')

    # formatting the columns
    self.list_of_students.column("#0", width=0, stretch=tk.NO)
    self.list_of_students.column("school_id", anchor=tk.W,)
    self.list_of_students.column("names", anchor=tk.W,)
    self.list_of_students.column("date_of_birth", anchor=tk.W,)
    self.list_of_students.column("entry_number", anchor=tk.W,)
    self.list_of_students.column("gender", anchor=tk.W,)
    self.list_of_students.column("address", anchor=tk.W,)
    self.list_of_students.column("class", anchor=tk.W,)
    self.list_of_students.column("parent_names", anchor=tk.W,)
    self.list_of_students.column("parent_phone_number", anchor=tk.W,)
    self.list_of_students.column("sports", anchor=tk.W,)
    self.list_of_students.column("other_details", anchor=tk.W,)

    # creating headings
    self.list_of_students.heading("#0", text="", anchor=tk.W)
    self.list_of_students.heading("school_id", text="Reg Number", anchor=tk.W)
    self.list_of_students.heading("names", text="Names", anchor=tk.W)
    self.list_of_students.heading("date_of_birth", text="Date of birth", anchor=tk.W)
    self.list_of_students.heading("entry_number", text="Birth entry number", anchor=tk.W)
    self.list_of_students.heading("gender", text="Gender", anchor=tk.W)
    self.list_of_students.heading("address", text="Home address", anchor=tk.W)
    self.list_of_students.heading("class", text="Class", anchor=tk.W)
    self.list_of_students.heading("parent_names", text="Parent/Guardian names", anchor=tk.W)
    self.list_of_students.heading("parent_phone_number", text="Phone number", anchor=tk.W)
    self.list_of_students.heading("sports", text="Sports", anchor=tk.W)
    self.list_of_students.heading("other_details", text="Other details", anchor=tk.W)

    self.all_students = get_all_students('chinonge')
    
    # # # # # # #
    # the list  #
    # # # # # # #
    self.list_of_students.after(300, self.upd_list)
    [self.list_of_students.insert(parent='', index='end', iid=student, text='', values=(student[0], student[1].decode('utf-8'), student[2].decode('utf-8'), student[3].decode('utf-8'), student[4].decode('utf-8'), student[5].decode('utf-8'), student[8].decode('utf-8'), student[6].decode('utf-8'), student[7].decode('utf-8'), student[9].decode('utf-8'), student[10].decode('utf-8'))) for student in self.all_students]

    self.list_of_students.pack(fill='both', expand=1)

  def upd_list(self):
    self.list_of_students.after(300, self.upd_list)

  def get_list(self):
    [self.list_of_students.insert(parent='', index='end', iid=student, text='', values=(student[0], student[1].decode('utf-8'), student[2].decode('utf-8'), student[3].decode('utf-8'), student[4].decode('utf-8'), student[5].decode('utf-8'), student[8].decode('utf-8'), student[6].decode('utf-8'), student[7].decode('utf-8'), student[9].decode('utf-8'), student[10].decode('utf-8'))) for student in self.all_students]
