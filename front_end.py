from tkinter import *
from tkinter import ttk
import pattern_finder


def header_line(col, row):
    """
    The method to create a line
    :param col: the column that the line should be in
    :param row: the row that the line should be in
    :return: none
    """
    ttk.Label(mainframe, text="-"*60).grid(column=col, row=row, columnspan=4)


def filler():
    """
    The method to create the layout
    :return: none
    """
    row_range = range(4, 14)
    header_line(0, 1)
    header_line(0, 3)
    for row_count in row_range:
        if row_count % 2 == 0:
            ttk.Label(mainframe, text="==").grid(column=1, row=row_count)
            ttk.Label(mainframe, text="am").grid(column=2, row=row_count)
        else:
            ttk.Label(mainframe, text="pm").grid(column=2, row=row_count)


def get_price(day):
    """
    The method to convert the string values to integers
    :param day: the day and time that should be replaced
    :return: the integer value of day
    """
    return int(day.get())


def find_pattern():
    """
    The method to find out which pattern you have. All of the logic is in a separate .py file called pattern_finder
    :return: none
    """
    text = ""
    # get prices in ints
    try:
        buying_val = get_price(sun)
        monam_val = get_price(monam)
        monpm_val = get_price(monpm)
        tuesam_val = get_price(tuesam)
        tuespm_val = get_price(tuespm)
        wedam_val = get_price(wedam)
        wedpm_val = get_price(wedpm)
        thursam_val = get_price(thursam)
        thurspm_val = get_price(thurspm)
        friam_val = get_price(friam)
        fripm_val = get_price(fripm)

        text = "You have pleased madam Zeroni"
        # Find out which pattern you have and print out what you should do with it.
        if not pattern_finder.is_decreasing(buying_val, monam_val, monpm_val, tuesam_val, tuespm_val, wedam_val, wedpm_val, thursam_val, thurspm_val, friam_val, fripm_val):
            if not pattern_finder.is_random(buying_val, monam_val, monpm_val, tuesam_val, tuespm_val, wedam_val, wedpm_val, thursam_val, thurspm_val, friam_val, fripm_val):
                if not pattern_finder.is_big_peak(buying_val, monam_val, monpm_val, tuesam_val, tuespm_val, wedam_val, wedpm_val, thursam_val, thurspm_val, friam_val, fripm_val):
                    text = "You have small peak. If you're at the third increase and the value is below 250 then you " \
                           "should wait for the fourth increase and then sell."
                else:
                    text = "You have big peak. Wait for the third increase and sell."
            else:
                text = "You have random. Once it gets above 115 then you should sell."
        else:
            text = "You have decreasing. If it hasn't changed by Thursday afternoon then sell."
        print(text)
    except ValueError:
        text = "All values must only be numbers"
        print(text)

    message.insert(END, text)
    #ttk.Label(mainframe, text=text).grid(column=0, row=15, columnspan=4, width=50, sticky=W)


root = Tk()
root.title("Turnip Tracker")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


# making the labels for mon-fri
ttk.Label(mainframe, text="Day of the week").grid(column=0, row=0, sticky=W)
ttk.Label(mainframe, text="Price").grid(column=3, row=0, sticky=E)
ttk.Label(mainframe, text="Buying price").grid(column=0, row=2, sticky=W)
ttk.Label(mainframe, text="Monday").grid(column=0, row=4, sticky=W)
ttk.Label(mainframe, text="Tuesday").grid(column=0, row=6, sticky=W)
ttk.Label(mainframe, text="Wednesday").grid(column=0, row=8, sticky=W)
ttk.Label(mainframe, text="Thursday").grid(column=0, row=10, sticky=W)
ttk.Label(mainframe, text="Friday").grid(column=0, row=12, sticky=W)

# make filler labels in between days and price
filler()

# buying price
sun = StringVar()

# text variables for mon-fri
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

# entry point for sunday buying price
sun_entry = ttk.Entry(mainframe, width=4, textvariable=sun)
sun_entry.grid(column=3, row=2)
# making the entry points for turnip prices for each day
monam_entry = ttk.Entry(mainframe, width=4, textvariable=monam).grid(column=3, row=4)
monpm_entry = ttk.Entry(mainframe, width=4, textvariable=monpm).grid(column=3, row=5)

tuesam_entry = ttk.Entry(mainframe, width=4, textvariable=tuesam).grid(column=3, row=6)
tuespm_entry = ttk.Entry(mainframe, width=4, textvariable=tuespm).grid(column=3, row=7)

wedam_entry = ttk.Entry(mainframe, width=4, textvariable=wedam).grid(column=3, row=8)
wedpm_entry = ttk.Entry(mainframe, width=4, textvariable=wedpm).grid(column=3, row=9)

thursam_entry = ttk.Entry(mainframe, width=4, textvariable=thursam).grid(column=3, row=10)
thurspm_entry = ttk.Entry(mainframe, width=4, textvariable=thurspm).grid(column=3, row=11)

friam_entry = ttk.Entry(mainframe, width=4, textvariable=friam).grid(column=3, row=12)
fripm_entry = ttk.Entry(mainframe, width=4, textvariable=fripm).grid(column=3, row=13)

# button for entry
ttk.Button(mainframe, text="Enter", command=find_pattern).grid(column=2, row=14, columnspan=2, sticky=W)

message = Text(mainframe, height=3, width=40)
message.grid(column=0, row=15, columnspan=4)

sun_entry.focus()
for child in mainframe.winfo_children():
    child.grid_configure(pady=2)
#root.bind('<Return>', find_pattern)
root.mainloop()
