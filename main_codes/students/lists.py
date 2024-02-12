import tkinter as tk
from tkinter.ttk import *
from tkinter.messagebox import askyesnocancel

from db.models import search_student, get_all_students, delete_std_record, get_last_transaction

class class_lists(Frame):
  def __init__(self, master: None) -> None:
    super().__init__(master, padding=4)

    self.select_school_id = tk.StringVar()

    # frame holding elements in this section
    self.lv_fram = Frame(self)
    self.lv_fram.pack(fill='both', expand=1)
    
    # frame with control buttons
    self.controls_frame = Frame(self.lv_fram, height=12)
    self.controls_frame.pack(fill='x', expand=1)

    '''Control Items'''
    self.edit_std_btn = Button(self.controls_frame, text="Edit")
    self.edit_std_btn["state"] = 'disabled'
    self.edit_std_btn.grid(row=0, column=0)

    self.del_std_btn = Button(self.controls_frame, text="Delete")
    self.del_std_btn['state'] = 'disabled'
    self.del_std_btn.grid(row=0, column=1, padx=64)

    # treeview 
    self.list_of_students = Treeview(self.lv_fram, height=28)

    # scrollbars
    self.lv_scbar = Scrollbar(self.lv_fram, command=self.list_of_students.yview)
    self.lv_scbar.pack(side='right', fill='y')
    self.lv_b_scbar = Scrollbar(self.lv_fram, orient=tk.HORIZONTAL, command=self.list_of_students.xview)
    self.lv_b_scbar.pack(fill='x', side='bottom')

    # set scrollbar to treeview
    self.list_of_students['xscrollcommand'] = self.lv_b_scbar.set
    self.list_of_students['yscrollcommand'] = self.lv_scbar.set
    
    # treeview columns defintion
    self.list_of_students['columns'] = ('school_id', 'last_name', 'first_name', 'added_names', 'gender', 'date_of_birth', 'birth_entry_number', 'permanent_address', 'current_address', 'other_details', 'parent_names', 'parent_phone_number', 'student_class', 'sports', 'created')

    # formatting the columns
    self.list_of_students.column("#0", width=0, stretch=tk.NO)
    self.list_of_students.column("school_id", anchor=tk.W, width=80, minwidth=60, stretch=tk.NO)
    self.list_of_students.column("last_name", anchor=tk.W, width=160, minwidth=120, stretch=tk.NO)
    self.list_of_students.column("first_name", anchor=tk.W, width=160, minwidth=120, stretch=tk.NO)
    self.list_of_students.column("added_names", anchor=tk.W, width=140, minwidth=120, stretch=tk.NO)
    self.list_of_students.column("gender", anchor=tk.W, width=60, stretch=tk.NO)
    self.list_of_students.column("date_of_birth", anchor=tk.W, width=120, minwidth=100, stretch=tk.NO)
    self.list_of_students.column("birth_entry_number", anchor=tk.W, width=120, minwidth=100, stretch=tk.NO)
    self.list_of_students.column("permanent_address", anchor=tk.W, width=160, stretch=tk.NO)
    self.list_of_students.column("current_address", anchor=tk.W, width=160, stretch=tk.NO)
    self.list_of_students.column("other_details", anchor=tk.W, width=180, minwidth=120, stretch=tk.NO)
    self.list_of_students.column("parent_names", anchor=tk.W, width=160, minwidth=120, stretch=tk.NO)
    self.list_of_students.column("parent_phone_number", anchor=tk.W, width=120, stretch=tk.NO)
    self.list_of_students.column("student_class", anchor=tk.W, width=80, stretch=tk.NO)
    self.list_of_students.column("sports", anchor=tk.W, width=100, minwidth=80, stretch=tk.NO)
    self.list_of_students.column('created', anchor=tk.W, width=80, stretch=tk.NO)

    # creating headings
    self.list_of_students.heading("#0", text="", anchor=tk.W)
    self.list_of_students.heading("school_id", text="Reg #", anchor=tk.W)
    self.list_of_students.heading("last_name", text="Surname", anchor=tk.W)
    self.list_of_students.heading("first_name", text="First Name", anchor=tk.W)
    self.list_of_students.heading("added_names", text="Added Names", anchor=tk.W)
    self.list_of_students.heading("gender", text="Gender", anchor=tk.W)
    self.list_of_students.heading("date_of_birth", text="Date of birth", anchor=tk.W)
    self.list_of_students.heading("birth_entry_number", text="Entry number", anchor=tk.W)
    self.list_of_students.heading("permanent_address", text="Home address", anchor=tk.W)
    self.list_of_students.heading("current_address", text="Home address", anchor=tk.W)
    self.list_of_students.heading("other_details", text="Other details", anchor=tk.W)
    self.list_of_students.heading("parent_names", text="Parent/Guardian names", anchor=tk.W)
    self.list_of_students.heading("parent_phone_number", text="Phone number", anchor=tk.W)
    self.list_of_students.heading("student_class", text="Class", anchor=tk.W)
    self.list_of_students.heading("sports", text="Sports", anchor=tk.W)
    self.list_of_students.heading('created', text="Enrolled", anchor=tk.W)
    
    # # # # # # #
    # The list  #
    # # # # # # #

    global count
    count = 0
    for student in get_all_students():
      self.list_of_students.insert(parent='', index='end', iid=count, text='', values=(student[0].decode('utf-8'), student[1].decode('utf-8'), student[2].decode('utf-8'), student[3].decode('utf-8'), student[4].decode('utf-8'), student[5], student[6].decode('utf-8'), student[7].decode('utf-8'), student[8].decode('utf-8'), student[9].decode('utf-8'), student[10].decode('utf-8'), student[11].decode('utf-8'), student[12].decode('utf-8'), student[13].decode('utf-8'), student[14]))

      count += 1

    self.list_of_students.after(300, self.update_lst)
    self.list_of_students.pack(fill='both', expand=1)
    self.list_of_students.bind("<<TreeviewSelect>>", self.select_std)

  def update_lst(self):
    self.list_of_students.after(300, self.update_lst)

  def update_std(self):
    return
  
  def delete_std(self):
    ret = askyesnocancel("Delete Student Record", message="You are about to delete this record.Are you sure?")
    if ret:
      dele = delete_std_record(self.select_school_id.get())
      print(f"Response: {dele}")
    else:
      pass
  
  def select_std(self, event=None):
    widget = event.widget
    value = widget.focus()

    selected = self.list_of_students.item(value, "values")

    self.edit_std_btn["state"] = "normal"
    self.del_std_btn["state"] = "normal"

    self.select_school_id.set(selected[0])

    self.del_std_btn['command'] = self.delete_std
