import random
from tkinter.ttk import *
import tkinter as tk
from tkinter.messagebox import showerror, showinfo
from datetime import datetime, timedelta
import time
from tkcalendar import DateEntry

from db.models import search_student, student_enrolment

class enrol_student(Frame):
  def __init__(self, master: None) -> None:
    super().__init__(master, padding=8)

    self.ERROR = 'Error.TLabel'
    self.SUCCESS = 'Success.TLabel'
    self.WARNING = 'Warning.TLabel'

    self.selected_gender = tk.StringVar()
    self.selected_class = tk.StringVar()
    self.selected_sport = tk.StringVar()
    self.generated_id = tk.StringVar()

    self.regn = LabelFrame(self, name="registration_number", text="Registration Number", padding=8, labelanchor='nw')
    self.regn.pack(side='top', fill='x', padx=8, pady=8)
    self.regn_lbl = Label(self.regn, relief='flat')
    self.regn_lbl.pack()

    self.frame_one = Frame(self)
    self.frame_one.pack(fill='both', expand=1)
    self.names_frame = LabelFrame(self.frame_one, name="names_of_student", text="Full names as they appear in birth-certificate", padding=8, labelanchor='nw')
    self.names_frame.pack(side='top', fill='x', padx=8, pady=(0, 8))
    self.details_frame = LabelFrame(self.frame_one, name="details_of_student", text="Further details of the student", padding=8, labelanchor='nw')
    self.details_frame.pack(side='top', fill='x', padx=8, pady=(0, 8))
    self.parent_details_frame = LabelFrame(self.frame_one, name="details_of_parent", text="Details of the parent", padding=8, labelanchor='nw')
    self.parent_details_frame.pack(side='top', fill='x', padx=8, pady=(0, 8))
    self.school_info = LabelFrame(self.frame_one, name="school_info", text="School Information", padding=8, labelanchor='nw')
    self.school_info.pack(side='top', fill='x', padx=8, pady=(0, 8))
    self.submit_frame = LabelFrame(self.frame_one, name="submit_all", text="Submit", padding=8, labelanchor='nw')
    self.submit_frame.pack(side='top', fill='x', padx=8, pady=(0, 8))

    self.lname_lbl = Label(self.names_frame, text="Surname:")
    self.lname_lbl.grid(row=0, column=0, sticky='w', pady=4, padx=8)
    self.lname_entry = Entry(self.names_frame, width=32)
    self.lname_entry.grid(row=0, column=1, sticky='w', padx=(0,16))

    self.fname_lbl = Label(self.names_frame, text="First name:")
    self.fname_lbl.grid(row=0, column=2, sticky='w', pady=4, padx=8)
    self.fname_entry = Entry(self.names_frame, width=48)
    self.fname_entry.grid(row=0, column=3, sticky='e', padx=(0,16))

    self.adname_lbl = Label(self.names_frame, text="Added names:")
    self.adname_lbl.grid(row=0, column=4, sticky='w', pady=4, padx=8)
    self.adname_entry = Entry(self.names_frame, width=32)
    self.adname_entry.grid(row=0, column=5, sticky='e')

    # gender using the combobox
    self.gender_lbl = Label(self.details_frame, text="Gender:")
    self.gender_lbl.grid(row=0, column=0, sticky='w', pady=4)
    self.gender_entry = Combobox(self.details_frame, textvariable=self.selected_gender)
    self.gender_entry["values"] = [i for i in ["Male", "Female"]]
    self.gender_entry["state"] = "readonly"
    self.gender_entry.grid(row=0, column=1, sticky='w', padx=(0, 32))

    self.dob_lbl = Label(self.details_frame, text="Date of birth:")
    self.dob_lbl.grid(row=0, column=2, sticky='w', pady=4, padx=(0, 4))
    self.dob_entry = DateEntry(self.details_frame, 
                 selectbackground='gray80',
                 selectforeground='black',
                 normalbackground='white',
                 normalforeground='black',
                 background='gray90',
                 foreground='black',
                 bordercolor='gray90',
                 othermonthforeground='gray50',
                 othermonthbackground='white',
                 othermonthweforeground='gray50',
                 othermonthwebackground='white',
                 weekendbackground='white',
                 weekendforeground='black',
                 headersbackground='white',
                 headersforeground='gray70'
                 )
    self.dob_entry["state"] = "readonly"
    self.dob_entry.grid(row=0, column=3, sticky='w', padx=(0, 32))

    self.ben_lbl = Label(self.details_frame, text="Birth Entry Number:")
    self.ben_lbl.grid(row=0, column=4, sticky='w', pady=4, padx=(0,4))
    self.ben_entry = Entry(self.details_frame)
    self.ben_entry.grid(row=0, column=5, sticky='w')

    self.perm_address_lbl = Label(self.details_frame, text='Permanent Address:', anchor='nw')
    self.perm_address_lbl.grid(row=1, column=0, sticky='w', pady=4, padx=(0,4))
    self.perm_address_entry = tk.Text(self.details_frame, width=48, height=4, pady=4, padx=4)
    self.perm_address_entry.grid(row=1, column=1, sticky='w', columnspan=4)

    self.current_address_lbl = Label(self.details_frame, text='Current Address:', anchor='ne')
    self.current_address_lbl.grid(row=1, column=4, sticky='w', pady=4, padx=(0,4))
    self.current_address_entry = tk.Text(self.details_frame, width=48, height=4, pady=4, padx=4)
    self.current_address_entry.grid(row=1, column=5, sticky='w', columnspan=4)

    self.other_det_lbl = Label(self.details_frame, text="Other details. \nInclude details such as special medication, allergies and \nother issues that affect child's concentration.\nThis is not to discriminate upon the child.", width=48)
    self.other_det_lbl.grid(row=2, column=0, sticky='w', pady=8, columnspan=2)
    self.other_det_entry = tk.Text(self.details_frame, width=96, height=4)
    self.other_det_entry.grid(row=2, column=2, sticky='w', columnspan=6)

    self.pare_g_lbl = Label(self.parent_details_frame, text="Parent/Guardian names:")
    self.pare_g_lbl.grid(row=0, column=0, sticky='w', pady=4)
    self.pare_g_entry = Entry(self.parent_details_frame, width=48)
    self.pare_g_entry.grid(row=0, column=1, sticky='w', columnspan=4, padx=(0,32))

    self.pare_g_phone_lbl = Label(self.parent_details_frame, text="Phone number:")
    self.pare_g_phone_lbl.grid(row=0, column=7, sticky='w', pady=4, padx=(0,4))
    self.pare_g_phone_entry = Entry(self.parent_details_frame)
    self.pare_g_phone_entry.grid(row=0, column=8, sticky='w')

    self.sch_cls_lbl = Label(self.school_info, text="Class:")
    self.sch_cls_lbl.grid(row=0, column=0, sticky='w', pady=4, padx=(0,4))
    self.sch_cls_entry = Combobox(self.school_info, textvariable=self.selected_class, width=8)
    self.sch_cls_entry["values"] = [i for i in ["ECDA", "ECDB", "Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5", "Grade 6", "Grade 7", "Form 1", "Form 2", "Form 3", "Form 4", "Form 5", "Form 6"]]
    self.sch_cls_entry["state"] = "readonly"
    self.sch_cls_entry.grid(row=0, column=1, sticky='w')

    self.sch_sports_lbl = Label(self.school_info, text="Sports:")
    self.sch_sports_lbl.grid(row=0, column=2, padx=(16,4), pady=4)
    self.sch_sports_entry = Combobox(self.school_info, textvariable=self.selected_sport)
    self.sch_sports_entry["values"] = [i for i in ['tennis', 'soccer', 'netball', 'volleyball', 'handball', 'cricket']]
    self.sch_sports_entry["state"] = "readonly"
    self.sch_sports_entry.grid(row=0, column=3, padx=(0,32))

    self.login_btn = Button(self.submit_frame, text="Enrol", command=self.save, cursor='hand1')
    self.login_btn.pack(side='top', pady=14)

    self.check_exists()

  # generate randon ids and make strings
  def gen_sid(self):
    rand = random.randint(10,99)
    randl = random.choice('abcdefghjklmnpqrstuvwxyz')

    return f"{rand}{randl.upper()}-{time.strftime('%Y')[2:]}"
  
  def check_exists(self):
    new_sid = self.gen_sid()
    existing_sid = search_student(new_sid)
    if existing_sid == "":
      self.generated_id.set(new_sid)
    else:
      self.generated_id.set(self.gen_sid())
    self.regn_lbl['text'] = self.generated_id.get()

  def set_message(self, type=None):
    if type:
      self.lname_lbl['style'] = type
      self.fname_lbl['style'] = type
      self.ben_lbl['style'] = type
      self.gender_lbl['style'] = type
      self.perm_address_lbl['style'] = type
      self.pare_g_lbl['style'] = type
      self.sch_cls_lbl['style'] = type

  def validate(*args):
    return
  
  def set_date_error(self, type=None):
    if type: self.dob_lbl['style'] = type

  def save(self):
    self.ds = tk.StringVar()
    self.ds.set(self.dob_entry.get_date())

    dtm = datetime(year=int(self.ds.get().split("-").pop(0)), month=int(self.ds.get().split("-").pop(1)), day=int(self.ds.get().split("-").pop(2)))

    if self.fname_entry.get() != '' and self.lname_entry.get() != "" and self.ben_entry.get() != "" and self.gender_entry.get() != "" and self.perm_address_entry.get(1.0, 'end') != "" and self.pare_g_entry.get() != "" and self.selected_class.get() != "":
      if dtm < (datetime.now() - timedelta(days=1460)):
        mode = student_enrolment(
          first_name=self.fname_entry.get().encode('utf-8'),
          last_name=self.lname_entry.get().encode('utf-8'),
          added_names=self.adname_entry.get().encode('utf-8'),
          school_id=self.generated_id.get().encode('utf-8'),
          date_of_birth=self.dob_entry.get_date(),
          birth_entry_number=self.ben_entry.get().encode('utf-8'),
          gender=self.selected_gender.get().encode('utf-8'),
          permanent_address=self.perm_address_entry.get(1.0, 'end').encode('utf-8'),
          current_address=self.current_address_entry.get(1.0, 'end').encode('utf-8'),
          student_class=self.selected_class.get().encode('utf-8'),
          parent_names=self.pare_g_entry.get().encode('utf-8'),
          parent_phone_number=self.pare_g_phone_entry.get().encode('utf-8'),
          sports=self.sch_sports_entry.get().encode('utf-8'),
          other_details=self.other_det_entry.get(1.0, 'end').encode('utf-8'),
          ts=datetime.now()
          )
        if mode == "success":
          self.reset()
        else:
          showerror('Error', mode)
      else:
        self.set_date_error(self.ERROR)
        showerror('Error', "Child is younger than the permissible date of entry into school.")
    else:
      self.set_message(self.ERROR)
      showerror("Error", "Blank form, please add information.")
  
  def reset(self):
    self.fname_entry.delete(0, 'end'),
    self.lname_entry.delete(0, 'end'),
    self.adname_entry.delete(0, 'end'),
    self.ben_entry.delete(0, 'end'),
    self.pare_g_entry.delete(0, 'end'),
    self.pare_g_phone_entry.delete(0, 'end')
    self.check_exists()
