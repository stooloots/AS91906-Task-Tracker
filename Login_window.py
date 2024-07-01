# Purpose: Testing login window before its added to main program
# Name: Andrew Wood
# Date: 21/06/24
# Version: 1.0

from tkinter import *
from tkinter import messagebox
import json

with open("database.json", "r+") as f:
    saved_users =json.load(f)

class Window:
    def __init__ (self):
        self.root = Tk()
        # Constants
        self.COMMON_FONT = ("Calibri", "12")
        self.LIGHT_BG_COLOUR = "#99B0D0"
        self.LOGIN_MAIN_COLOUR = "#7092BE"

        # Login window
        self.root.title("Task Tracker")
        # Size of GUI window from paint root.geometry("575x370")
        # Size of GUI including border from paint
        self.root.geometry("586x370")

        # Window sizing
        self.root.columnconfigure((0,2), weight= 7)
        self.root.columnconfigure((1), weight = 1)
        self.root.rowconfigure((0,2), weight = 3)
        self.root.rowconfigure((1), weight = 1)

        # FRAME 1 for login system
        self.login = Frame(self.root, bg=self.LOGIN_MAIN_COLOUR, borderwidth=2, relief=SOLID)
        self.login.grid(column=1, row=1, sticky="NESW")
        self.login.columnconfigure((0,2), weight= 3)
        self.login.columnconfigure((1), weight = 4)
        self.login.rowconfigure((0,2,4,6,8), weight = 3)
        self.login.rowconfigure((1,3,5,7), weight = 3)

        # Text lable for login title
        self.login_text = "User Login"
        self.login_label = Label(self.login, text=self.login_text, font=self.COMMON_FONT, bg=self.LOGIN_MAIN_COLOUR)
        self.login_label.grid(column=1, row=1, sticky="NESW")

        # FRAME 2 for Username entry and image
        self.username = Frame(self.login, bg="white", borderwidth=2, relief=SOLID)
        self.username.grid(column=1, row=3, sticky="NESW")
        self.username.columnconfigure((0), weight=1)
        self.username.columnconfigure((1), weight=7)
        self.username.rowconfigure((0), weight=2)

        # Frame 2 username image
        self.username_photoimage = PhotoImage(file = "username_photoimage.png")
        self.username_image = Label(self.username, image=self.username_photoimage)
        self.username_image.grid(column=0, row=0, sticky="NESW")

        # Frame 2 username entry
        self.username_entry_default = "Username"
        self.username_entry = Entry(self.username)
        self.username_entry.insert(0, self.username_entry_default)
        self.username_entry.grid(column=1, row=0, sticky="NESW")
        self.username_entry.bind("<Enter>", lambda e: self.entry_remove(self.username_entry))

        # FRAME 3 for Password entry and image
        self.password = Frame(self.login, bg="white", borderwidth=2, relief=SOLID)
        self.password.grid(column=1, row=5, sticky="NESW")
        self.password.columnconfigure((0), weight=1)
        self.password.columnconfigure((1), weight=7)
        self.password.rowconfigure((0), weight=2)

        # Frame 3 Password image
        self.password_photoimage = PhotoImage(file = "password_photoimage.png")
        self.password_image = Label(self.password, image=self.password_photoimage)
        self.password_image.grid(column=0, row=0, sticky="NESW")

        # Frame 3 Password entry
        self.password_entry_default = "Password"
        self.password_entry = Entry(self.password)
        self.password_entry.insert(0, self.password_entry_default)
        self.password_entry.grid(column=1, row=0, sticky="NESW")
        self.password_entry.bind("<Enter>", lambda e: self.entry_remove(self.password_entry))
        self.password_entry.bind("<Return>", lambda e: self.entry_getter())

        # FRAME 4 for login button
        self.login_button_frame = Frame(self.login, bg=self.LIGHT_BG_COLOUR, borderwidth=2, relief=SOLID)
        self.login_button_frame.grid(column=1, row=7, sticky="NESW")
        self.login_button_frame.columnconfigure((0), weight=1)
        self.login_button_frame.rowconfigure((0), weight=2)

        # Login button for frame 4
        self.login_button_text = "Login"
        self.login_button = Button(self.login_button_frame, text=self.login_button_text, bg=self.LIGHT_BG_COLOUR, font=self.COMMON_FONT, command=lambda: self.entry_getter())
        self.login_button.grid(column=0, row=0, sticky="NESW")

        self.root.mainloop()

    def entry_getter(self):
        global saved_users
        users_username = self.username_entry.get()
        users_password = self.password_entry.get()
        if users_username in saved_users:
            if saved_users[users_username]["password"] == users_password:
                self.login.destroy()
                self.entry_window(users_username)
            else:
                messagebox.showerror("Error", "Invalid input: Please enter the correct username or password", parent=self.root)
        else:
            messagebox.showerror("Error", "Invalid input: Please enter the correct username or password", parent=self.root)
        
    def entry_remove(self, entry):
        if entry == self.username_entry:
            if self.username_entry.get() == "Username":
                entry.delete(0, END)
        if entry == self.password_entry:
            if self.password_entry.get() == "Password":
                entry.delete(0, END)
                entry.configure(show="*")
    
    def entry_window(self, user_username):

        # Changed Window sizing to fit new grid
        self.root.columnconfigure((0,2,4,6,8), weight= 2)
        self.root.columnconfigure((1,3,5), weight = 4)
        self.root.rowconfigure((0,2,4,6,8), weight = 1)
        self.root.rowconfigure((1,3,5), weight = 4)

        # Label welcoming user
        self.entry_welcome_text = f"Welcome {user_username}, please select an option."
        self.entry_welcome_label = Label(self.root, text=self.entry_welcome_text, font=(self.COMMON_FONT))
        self.entry_welcome_label.grid(column=1, row=0, columnspan= 6, sticky="NESW")

        # FRAME 1 for Entry window
        self.login_edit_frame = Frame(self.root, borderwidth=2, relief=SOLID)
        self.login_edit_frame.grid(column=1, row=1, sticky="NESW")
        self.login_edit_frame.columnconfigure((0), weight= 1)
        self.login_edit_frame.rowconfigure((0), weight = 1)

        # Button 1 Profile edit for Entry window in FRAME 1
        self.login_edit_button_text = "Edit Login"
        self.login_edit_button = Button(self.login_edit_frame, text=self.login_edit_button_text, anchor="n")
        self.login_edit_button.grid(column=0, row=0, sticky="NESW")

        # FRAME 2 for Entry window
        self.profile_enter_frame = Frame(self.root, borderwidth=2, relief=SOLID)
        self.profile_enter_frame.grid(column=3, row=1, sticky="NESW")
        self.profile_enter_frame.columnconfigure((0), weight= 1)
        self.profile_enter_frame.rowconfigure((0), weight = 1)

        # Button 2 Profile enter for entry window in  FRAME 2
        self.profile_enter_button_text = "Select Profile"
        self.profile_enter_button = Button(self.profile_enter_frame, text=self.profile_enter_button_text, anchor="n")
        self.profile_enter_button.grid(column=0, row=0, sticky="NESW")