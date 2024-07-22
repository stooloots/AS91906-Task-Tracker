# Purpose: Testing login window before its added to main program
# Name: Andrew Wood
# Date: 21/06/24
# Version: 1.0

from tkinter import *
from tkinter import messagebox
import json
import math

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
        self.password_entry.bind("<Return>", self.entry_getter)

        # FRAME 4 for login button
        self.login_button_frame = Frame(self.login, bg=self.LIGHT_BG_COLOUR, borderwidth=2, relief=SOLID)
        self.login_button_frame.grid(column=1, row=7, sticky="NESW")
        self.login_button_frame.columnconfigure((0), weight=1)
        self.login_button_frame.rowconfigure((0), weight=2)

        # Login button for frame 4
        self.login_button_text = "Login"
        self.login_button = Button(self.login_button_frame, text=self.login_button_text, bg=self.LIGHT_BG_COLOUR, font=self.COMMON_FONT, command= self.entry_getter)
        self.login_button.grid(column=0, row=0, sticky="NESW")

        self.root.mainloop()

    def entry_getter(self, *args):
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
    
    def entry_window(self, entry_user_username):
        # Entry window screen 

        # Changed Window sizing to fit new grid
        self.root.columnconfigure((0,2,4,6), weight= 2)
        self.root.columnconfigure((1,3,5), weight = 4)
        self.root.rowconfigure((0,2,4,6), weight = 1)
        self.root.rowconfigure((1,3,5), weight = 4)

        # Label welcoming user
        self.entry_welcome_text = f"Welcome {entry_user_username}, please select an option."
        self.entry_welcome_label = Label(self.root, text=self.entry_welcome_text, font=(self.COMMON_FONT))
        self.entry_welcome_label.grid(column=1, row=0, columnspan= 5, sticky="NESW")

        # FRAME 1 for Entry window
        self.login_edit_frame = Frame(self.root, borderwidth=2, relief=SOLID)
        self.login_edit_frame.grid(column=1, row=1, sticky="NESW")
        self.login_edit_frame.columnconfigure((0), weight= 1)
        self.login_edit_frame.rowconfigure((0), weight = 1)

        # Button 1 Profile edit for Entry window in FRAME 1
        self.login_edit_button_text = "Edit Login"
        self.login_edit_button = Button(self.login_edit_frame, text=self.login_edit_button_text, anchor="n", command= lambda: self.login_edit_window())
        self.login_edit_button.grid(column=0, row=0, sticky="NESW")

        # FRAME 2 for Entry window
        self.profile_enter_frame = Frame(self.root, borderwidth=2, relief=SOLID)
        self.profile_enter_frame.grid(column=3, row=1, sticky="NESW")
        self.profile_enter_frame.columnconfigure((0), weight= 1)
        self.profile_enter_frame.rowconfigure((0), weight = 1)

        # Button 2 Profile enter for entry window in  FRAME 2
        self.profile_enter_button_text = "Select Profile"
        self.profile_enter_button = Button(self.profile_enter_frame, text=self.profile_enter_button_text, anchor="n", command= lambda: self.profile_entry_window(entry_user_username))
        self.profile_enter_button.grid(column=0, row=0, sticky="NESW")

    def login_edit_window(self, *args):
        # This window will allow the user to edit their login information

        self.entry_welcome_label.destroy()
        self.login_edit_frame.destroy()
        self.profile_enter_frame.destroy()
        
    def profile_entry_window(self, profile_user_username):
        # This window will allow the user to create groupings for tasks

        global saved_users

        # Destroying old widgets
        self.entry_welcome_label.destroy()
        self.login_edit_frame.destroy()
        self.profile_enter_frame.destroy()

        # Setting root column and row configs 
        self.root.columnconfigure((0,2,4,6), weight= 2)
        self.root.columnconfigure((1,3,5), weight = 4)
        self.root.rowconfigure((0,2,4,6), weight = 1)
        self.root.rowconfigure((1,3,5), weight = 4)

        self.profile_entry_welcome_text = f"Welcome {profile_user_username}, please select a profile."
        self.profile_entry_entry_welcome_label = Label(self.root, text=self.profile_entry_welcome_text, font=(self.COMMON_FONT))
        self.profile_entry_entry_welcome_label.grid(column=1, row=0, columnspan= 5, sticky="NESW")

        profile_list = []
        for keys in saved_users[profile_user_username]["profiles"]:
            # Grabs ditctionary containing profiles
            profile_list.append(keys)
            # Grabs profile dictionary 
            # print(saved_users[profile_user_username]["profiles"][keys])
            

        # Creating list of profile frames
        self.template_profile_frame = []
        for i in range(len(profile_list)):
            # Maths😜
            column = (i%3)*2+1
            row = math.floor(i/3)*2+1
            # Creating frame for each profile inside the profile entry window and appending it to the frame list
            self.template_profile_frame.append(Frame(self.root, borderwidth=2, relief=SOLID))
            self.template_profile_frame[-1].grid(column=column, row=row, sticky="NESW")
            self.template_profile_frame[-1].columnconfigure((0), weight= 1)
            self.template_profile_frame[-1].rowconfigure((0), weight = 1)
            # Button place in frame (created for profile) located inside profile entry window
            self.template_profile_frame_text = profile_list[i]
            self.template_profile_button = Button(self.template_profile_frame[-1], text=self.template_profile_frame_text, anchor="n", command= lambda: self.task_window(saved_users[profile_user_username]["profiles"][profile_list[i]])) 
            self.template_profile_button.grid(column=0, row=0, sticky="NESW")

    def task_window(self, profile_tasks):
        ''' This method will open the task window where all tasks are visible, profile_tasks is the tasks dictionary taken from the profile '''

        # Runs through list of profile frames and deletes them
        for i in self.template_profile_frame:
            i.destroy()
        self.profile_entry_entry_welcome_label.destroy()

        # Setting root column and row configs for task window
        self.root.columnconfigure((0,4), weight= 1)
        self.root.columnconfigure((1,3), weight = 4)
        self.root.columnconfigure((2), weight=6)
        self.root.rowconfigure((0), weight = 1)
        self.root.rowconfigure((1), weight = 9)

        