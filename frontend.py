import tkinter as tk

HEIGHT = 300
WIDTH = 395

# "About" popup window
def popupmsg(about_function):
    popup = tk.Tk()
    #popup.wm_title("About")
    l_pop=tk.Label(popup, text=about_function())
    l_pop.pack(side='top', fill='x', pady=10)
    b_pop=tk.Button(popup, text="Okay", command=popup.destroy)
    b_pop.pack()
    popup.mainloop()

# printing app info
def about_function():
    border1=(27 * "-")
    title=("Title: Tip Calculator 2019")
    author=("Author: John E. Schneider")
    rdate=("Released: 22-May-2019")
    version=("version: 1.0")
    border2=(27 * "-")

# formatting repsonse
def format_response(tiptext):
    global l1
    l1.configure(bg='#ffae59')
    return str(tiptext)

 # calculating user entries
def add(x,y,z):
    x=float(x)          # meal total
    y=float(y)          # total tippers
    z=float(z)          # tip percentage
    z=(z / 100)         # convert to percent as a decimal
    ttpp=(x * z / y)    # tip total per person
    ttpp=str(ttpp)
    tiptext= ("Tip total per person: " + ttpp)

    l1['text'] = format_response(tiptext)

root=tk.Tk()

x=tk.IntVar()
y=tk.IntVar()
z=tk.IntVar()

canvas=tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image=tk.PhotoImage(file='mathmat.png')
background_label=tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# frames
f1=tk.Frame(root, bg='#74a5a0', bd=5)
f2=tk.Frame(root, bg='#74a5a0', bd=10)

# frame positions
f1.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
f2.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.4, anchor='n')

# buttons
b1=tk.Button(root, text="About", command=lambda :popupmsg)
b2=tk.Button(f2, text="Submit",  command=lambda :add(x.get(),y.get(),z.get()))
b3=tk.Button(f2, text="Quit", command=root.destroy)

# button positions
b1.place(relx=0.74, rely=0.83, anchor='n')
b2.grid(row=3, column=1, pady=5, sticky='e')
b3.grid(row=3, column=0, padx=2.5, pady=5, sticky='w')


# labels
l1=tk.Label(f1, text='    TipCal "a simple tip calculator"    ', bg='#ffae59')
#l1=tk.Label(f1, bg='#74a5a0')
l2=tk.Label(f2, text="Meal Total",        bg='#74a5a0')
l3=tk.Label(f2, text="Total Tippers",     bg='#74a5a0')
l4=tk.Label(f2, text="Tip Percentage",    bg='#74a5a0')

# label positions
l1.pack()
#l1.grid(row=0, column=0)
l2.grid(sticky='W', row=0)
l3.grid(sticky='w', row=1)
l4.grid(sticky='w', row=2)

# entry fields
e1=tk.Entry(f2, textvariable=x)
e2=tk.Entry(f2, textvariable=y)
e3=tk.Entry(f2, textvariable=z)

# entry field positions
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

root.mainloop()