import os
import tkinter as tk
from tkinter.ttk import *
from tkinter.messagebox import showerror

from .create_db import create_db

class school_name(Frame):
  def __init__(self, master=None) -> None:
    super().__init__(master)
    self.school_value = tk.StringVar()
    self.wintop_val = tk.StringVar()

    options = { "padx": 4, "pady": 4 }


    self.top = tk.Toplevel(self)
    self.top.title("School name")
    self.top.geometry("320x140")
    self.top.resizable(0,0)
    self.top.attributes('-topmost', True)

    self.lbl1 = Label(self.top, text="School name (eg: Ntantantongwa)")
    self.lbl1.grid(options, row=0, column=0, columnspan=2)
    self.ent1 = Entry(self.top, width=30)
    self.ent1.focus()
    self.ent1.grid(options, row=1, column=0, columnspan=2)
    self.rdbtn1 = Radiobutton(self.top, text="Primary", value="primary", variable=self.school_value)
    self.rdbtn1.grid(options, row=2, column=0)
    self.rdbtn2 = Radiobutton(self.top, text="Secondary/High", value="secondary", variable=self.school_value)
    self.rdbtn2.grid(options, row=2, column=1)

    self.svbtn = Button(self.top, text="Save", command=self.save_file)
    self.svbtn.grid(options, row=3, column=1, sticky='e')

    #self.top.pack(fill='both', expand=1)
  
  def save_file(self):
    sch_name = self.ent1.get()
    sc_typ = self.school_value.get()
    if sch_name != '' and sc_typ != '':
      with open(os.path.relpath("data_base/db_names.txt"), 'w') as f:
        f.write(f"{sch_name.capitalize()} {sc_typ.capitalize()}")
        create_db(sch_name.lower())
        self.ent1.delete(0, 'end')
        self.top.destroy()
        self.wintop_val.set("done")
    elif sch_name == '':
      showerror("Blank!", "School Name is required!")
    else:
      showerror("Blank!", "Choose an option (Primary or Secondary)")

if __name__ == "__main__":
  app = school_name()
  
  app.mainloop()
