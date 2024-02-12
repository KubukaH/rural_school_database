import os
from tkinter.ttk import *
import tkinter as tk
from .level_one import level_one_frame

class index_frame(Frame):
  def __init__(self, master) -> None:
    super().__init__(master)

    # Lvel One User frames
    self.level_1_frame = level_one_frame(master)
    self.level_1_frame.pack(fill='both', expand=1)