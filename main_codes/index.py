import os
from tkinter.ttk import *

from .level_one import level_one_frame

def index_frame(root):
  main_frame = Frame(root)

  # Lvel One User frames
  level_1_frame = level_one_frame(main_frame)
  level_1_frame.pack(fill='both', expand=1)

  return main_frame