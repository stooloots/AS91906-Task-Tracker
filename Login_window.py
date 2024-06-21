# Purpose: Testing login window before its added to main program
# Name: Andrew Wood
# Date: 21/06/24
# Version: 1.0

from tkinter import *

# Login window

root = Tk()
root.title("Task Tracker")
# Size of GUI window from paint root.geometry("575x370")
# Size of GUI including border from paint
root.geometry("586x370")
root.resizable(0,0)

# Window sizing
root.columnconfigure((0,2), weight= 2)
root.columnconfigure((1), weight = 1)
root.rowconfigure((0,2), weight = 2)
root.rowconfigure((1), weight = 1)

# Frame 1 for login system
login_main_colour = "#7092BE"
login = Frame(root, bg=login_main_colour, borderwidth=2, relief=SOLID)
login.grid(column=1, row=1, sticky="NESW")
login.columnconfigure((0,2), weight= 1)
login.columnconfigure((1), weight = 4)
login.rowconfigure((0,2,4,6,8), weight = 1)
login.rowconfigure((1,3,5,7), weight = 3)

# Text lable for login title
login_text = "User Login"
login_label = Label(login, text=login_text, font=("Calibri", "12"), bg=login_main_colour)
login_label.grid(column=1, row=1, sticky="NESW")

# Frame 2 for Username entry and image
username = Frame(login, bg="white", borderwidth=2, relief=SOLID)
username.grid(column=1, row=3)
username.columnconfigure((0), weight=1)
username.columnconfigure((1), weight=7)
username.rowconfigure((0), weight=3)

# Frame 2 username image
username_photoimage = PhotoImage(file = "username_photoimage.png")
username_image = Label(username, image=username_photoimage)
username_image.grid(column=0, row=1, sticky="NESW")

# Frame 2 username entry
username_entry_default = "Username"
username_entry = Entry(username, )

root.mainloop()