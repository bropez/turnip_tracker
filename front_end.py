from tkinter import *
from tkinter import ttk

row_range = range(2, 12)


def filler():
    ttk.Label(mainframe, text="-------------------------------------").grid(column=0, row=1, columnspan=4)
    for row_count in row_range:
        if row_count % 2 == 0:
            ttk.Label(mainframe, text="==").grid(column=1, row=row_count)
            ttk.Label(mainframe, text="am").grid(column=2, row=row_count)
        else:
            ttk.Label(mainframe, text="pm").grid(column=2, row=row_count)


# TODO: a way to put which pattern you have under the button (column=2, row=12)


root = Tk()
root.title("Tracker")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


# making the labels for mon-fri
ttk.Label(mainframe, text="Day of the week").grid(column=0, row=0, sticky=E)
ttk.Label(mainframe, text="Price").grid(column=3, row=0, sticky=E)
ttk.Label(mainframe, text="Monday").grid(column=0, row=2, sticky=W)
ttk.Label(mainframe, text="Tuesday").grid(column=0, row=4, sticky=W)
ttk.Label(mainframe, text="Wednesday").grid(column=0, row=6, sticky=W)
ttk.Label(mainframe, text="Thursday").grid(column=0, row=8, sticky=W)
ttk.Label(mainframe, text="Friday").grid(column=0, row=10, sticky=W)

# make filler labels in between days and price
filler()

# text variables for mon-fri
# TODO: use IntVar() instead
monam = StringVar()
tuesam = StringVar()
wedam = StringVar()
thursam = StringVar()
friam = StringVar()

monpm = StringVar()
tuespm = StringVar()
wedpm = StringVar()
thurspm = StringVar()
fripm = StringVar()

# making the entry points for turnip prices for each day
monam_entry = ttk.Entry(mainframe, width=4, textvariable=monam)
monam_entry.grid(column=3, row=2)
monpm_entry = ttk.Entry(mainframe, width=4, textvariable=monpm)
monpm_entry.grid(column=3, row=3)

tuesam_entry = ttk.Entry(mainframe, width=4, textvariable=tuesam).grid(column=3, row=4)
tuespm_entry = ttk.Entry(mainframe, width=4, textvariable=tuespm).grid(column=3, row=5)

wedam_entry = ttk.Entry(mainframe, width=4, textvariable=wedam).grid(column=3, row=6)
wedpm_entry = ttk.Entry(mainframe, width=4, textvariable=wedpm).grid(column=3, row=7)

thursam_entry = ttk.Entry(mainframe, width=4, textvariable=thursam).grid(column=3, row=8)
thurspm_entry = ttk.Entry(mainframe, width=4, textvariable=thurspm).grid(column=3, row=9)

friam_entry = ttk.Entry(mainframe, width=4, textvariable=friam).grid(column=3, row=10)
fripm_entry = ttk.Entry(mainframe, width=4, textvariable=fripm).grid(column=3, row=11)

# button for entry
ttk.Button(mainframe, text="Enter").grid(column=2, row=12, columnspan=2, sticky=W)

monam_entry.focus()
for child in mainframe.winfo_children():
    child.grid_configure(pady=2)
#root.bind('<Return>', find_pattern)
root.mainloop()
