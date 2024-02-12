from tkinter.ttk import Style

def make_styles(root):
  style = Style(root)

  # general styling that applies to all components
  style.map(
    "TButton",
    foreground=[('pressed', 'red'), ('active', 'gray')],
    background=[('pressed', '!disabled', '#3fa8a5'), ('active', '#fff')]
  )
  style.configure(
    "TButton", relief="raised", background="gray", 
    foreground="#ffe", padx=4, pady=4, cursor='hand1'
  )

  # Success and Error labels
  style.configure(
    "Success.TLabel", foreground='#a7f182'
  )
  style.configure(
    "Error.TLabel", foreground='#da2319'
  )
  style.configure(
    "Warning.TLabel", foreground='#f1d982'
  )

  # config individual button components
  style.map("Logout.TButton",
    foreground=[('pressed', 'orange'), ('active', 'orange')],
    background=[('pressed', '!disabled', '#3fa8a5'), ('active', '#fff')]
  )