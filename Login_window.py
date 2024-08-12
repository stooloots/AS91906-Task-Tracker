# Purpose: Testing login window before its added to main program
# Name: Andrew Wood
# Date: 21/06/24
# Version: 1.0

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from functools import partial
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

        # Adding the users username to the class
        self.profile_user_username = entry_user_username

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
        self.login_edit_button = Button(self.login_edit_frame, text=self.login_edit_button_text, anchor="n", command= lambda: self.login_edit_window(), state=DISABLED)
        self.login_edit_button.grid(column=0, row=0, sticky="NESW")

        # FRAME 2 for Entry window
        self.profile_enter_frame = Frame(self.root, borderwidth=2, relief=SOLID)
        self.profile_enter_frame.grid(column=3, row=1, sticky="NESW")
        self.profile_enter_frame.columnconfigure((0), weight= 1)
        self.profile_enter_frame.rowconfigure((0), weight = 1)

        # Button 2 Profile enter for entry window in  FRAME 2
        self.profile_enter_button_text = "Select Profile"
        self.profile_enter_button = Button(self.profile_enter_frame, text=self.profile_enter_button_text, anchor="n", command= lambda: self.profile_entry_window())
        self.profile_enter_button.grid(column=0, row=0, sticky="NESW")

    def login_edit_window(self, *args):
        # This window will allow the user to edit their login information

        self.entry_welcome_label.destroy()
        self.login_edit_frame.destroy()
        self.profile_enter_frame.destroy()
        
    def profile_entry_window(self):
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

        self.profile_entry_welcome_text = f"Welcome {self.profile_user_username}, please select a profile."
        self.profile_entry_entry_welcome_label = Label(self.root, text=self.profile_entry_welcome_text, font=(self.COMMON_FONT))
        self.profile_entry_entry_welcome_label.grid(column=1, row=0, columnspan= 5, sticky="NESW")

        profile_list = []
        for keys in saved_users[self.profile_user_username]["profiles"]:
            # Grabs ditctionary containing profiles
            profile_list.append(keys)
            # Grabs profile dictionary 
            # print(saved_users[self.profile_user_username]["profiles"][keys])

        # Creating list of profile frames and buttons
        self.template_profile_frame = []
        self.template_profile_button = []
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
            self.template_profile_button.append(Button(self.template_profile_frame[-1], text=self.template_profile_frame_text, anchor="n", command=partial(self.task_window, profile_list[i]))) # Fixed by Jensen # Now sends "profile_list[i] instead of task dictionary"
            self.template_profile_button[-1].grid(column=0, row=0, sticky="NESW")

    def task_window(self, profile_tasks):
        ''' This method will open the task window where all tasks are visible, profile_tasks is the tasks dictionary taken from the profile '''
        # profile tasks is a name
        # eg "profile 1", "profile 2"

        global saved_users

        # Adds the profile_task selected into the class
        self.profile_number = profile_tasks

        # Runs through list of profile frames and deletes them
        for i in self.template_profile_frame:
            i.destroy()
        self.profile_entry_entry_welcome_label.destroy()

        # Setting root column and row configs for task window
        self.root.columnconfigure((0,4), weight= 1)
        self.root.columnconfigure((1,3), weight = 4)
        self.root.columnconfigure((2), weight=12)
        self.root.columnconfigure((5,6,7,8,9),weight=0)
        self.root.rowconfigure((0), weight = 1)
        self.root.rowconfigure((1,2,3,4,5,6,7,8), weight = 0)

        # Frame 1 for left side of task window. This frame will include the title and the listed tasks section
        self.task_window_frame1 = Frame(self.root)
        self.task_window_frame1.grid(column=1, row=0, sticky="NESW")
        
        # Getting list of tasks (keys) and priority
        task_list = []
        for task in saved_users[self.profile_user_username]["profiles"][self.profile_number]:
            task_list.append([saved_users[self.profile_user_username]["profiles"][self.profile_number][task]["priority"], task])
        task_list.sort(reverse=True, key=lambda x: x[0])

        # Setting task_window_frame1 columns, rows will be set when each task is set
        self.task_window_frame1.columnconfigure((1), weight= 4)
        self.task_window_frame1.columnconfigure((0,2), weight = 1)
        # Setting task_window_fram1 bottom row
        self.task_window_frame1.rowconfigure((len(task_list*2)), weight=1) 

        # Title label
        self.task_window_title = Label(self.task_window_frame1, text="Profile")
        self.task_window_title.grid(column=1, row=0, sticky="NESW")
        
        self.template_task_frame = []
        for i in range(len(task_list)):
            # Setting task_window_frame1 row configurations
            self.task_window_frame1.rowconfigure(((i*2)), weight = 1)
            self.task_window_frame1.rowconfigure(((i*2)+1), weight = 2)

            # Creating frames for each task label
            self.template_task_frame.append(Frame(self.task_window_frame1, borderwidth=2, relief=SOLID))
            self.template_task_frame[-1].grid(column=1, row=((i*2)+1), sticky="NESW")
            self.template_task_frame[-1].columnconfigure((0), weight= 1)
            self.template_task_frame[-1].rowconfigure((0), weight = 1)
            # Button placed in task frame (created for tasks) located inside profile entry window
            self.template_task_frame_text = task_list[i][1]
            self.template_task_button = Button(self.template_task_frame[-1], text=self.template_task_frame_text, anchor="n", command= partial(self.tasking, task_list[i][1]))# task_list[i] sends task name
            self.template_task_button.grid(column=0, row=0, sticky="NESW")
        
        # Frame 2 for Right side of window. This frame will include the recently editted, prioity button
        self.task_window_frame2 = Frame(self.root)
        self.task_window_frame2.grid(column=3, row=0, sticky="NESW")
        
        # Setting task_window_frame2 columns and rows
        self.task_window_frame2.columnconfigure((0), weight= 1)
        # Layout of rows
        self.task_window_frame2.rowconfigure((1,3,5), weight = 2)
        self.task_window_frame2.rowconfigure((0,2,4), weight = 1)
        self.task_window_frame2.rowconfigure((6), weight=4)

        # Recently edited frame and label
        # Recent edit frame
        self.recent_edit_frame = Frame(self.task_window_frame2, borderwidth=2, relief=SOLID)
        self.recent_edit_frame.grid(column=0, row=1, sticky="NESW")

        # Setting recent_edit_frame columns and rows
        self.recent_edit_frame.columnconfigure((0,2), weight= 1)
        self.recent_edit_frame.columnconfigure((1), weight=2)
        # Layout of rows
        self.recent_edit_frame.rowconfigure((1,3), weight = 2)
        self.recent_edit_frame.rowconfigure((0,4), weight = 1)
        self.recent_edit_frame.rowconfigure((2), weight=3)

        # Recent edit label
        self.recent_edit_task = "None"
        self.recent_edit_label_text = f"Recently\n edited:"
        self.recent_edit_label_1 = Label(self.recent_edit_frame, text=self.recent_edit_label_text)
        self.recent_edit_label_1.grid(column=1, row=1, sticky="NESW")

        self.recent_edit_label_task = self.recent_edit_task
        self.recent_edit_label_2 = Label(self.recent_edit_frame, text=self.recent_edit_label_task)
        self.recent_edit_label_2.grid(column=1, row=3, sticky="NESW")

        # Priority button
        self.priority_button_frame = Frame(self.task_window_frame2, borderwidth=2, relief=SOLID)
        self.priority_button_frame.grid(column=0, row=3, sticky="NESW")
        self.priority_button_frame.columnconfigure((0), weight=1)
        self.priority_button_frame.rowconfigure((0), weight=1)

        self.profile_button_text = "Change Priority"
        self.profile_button = Button(self.priority_button_frame, text=self.profile_button_text, command=lambda: self.priority_change(task_list))
        self.profile_button.grid(column=0, row=0, sticky="NESW")

        # Task Edit button (previously delete button)
        self.task_edit_button_frame = Frame(self.task_window_frame2, borderwidth=2, relief=SOLID)
        self.task_edit_button_frame.grid(column=0, row=5, sticky="NESW")
        self.task_edit_button_frame.columnconfigure((0), weight=1)
        self.task_edit_button_frame.rowconfigure((0), weight=1)

        self.task_edit_button_text = "Delete Task"
        self.task_edit_button = Button(self.task_edit_button_frame, text=self.task_edit_button_text)
        self.task_edit_button.grid(column=0, row=0, sticky="NESW")

    def priority_change(self, task_list):
        ''' Allows the user to edit the priority of each task 
        | task | prio | <-- Frame
        |      | entry| 
        |Submit|Cancel| <-- Frame
        '''
        # Retreieves saved_users
        global saved_users

        # Creates toplevel window and makes it grabset
        self.priority_window = Toplevel()
        self.priority_window.grab_set()
        self.priority_window.title("Priority change")

        # Setting grid layout        
        self.priority_window.columnconfigure((0), weight = 1)
        self.priority_window.rowconfigure((0), weight = 1)
        self.priority_window.rowconfigure((1), weight = 1)

        # Frame for labels
        self.priority_window_labelframe = Frame(self.priority_window)
        self.priority_window_labelframe.grid(column=0, row=0, sticky="NESW")

        # Grid for frame
        self.priority_window_labelframe.columnconfigure((0,1), weight = 1)

        # Setting labels for tasks and priority
        self.priority_window_tasklabel = []
        self.priority_window_priorityentry = []
        for i in range(len(task_list)):
            # Setting additional row weights
            self.priority_window_labelframe.rowconfigure(((i)), weight = 1)
            # task label
            self.priority_window_tasklabel_text = task_list[i][1]
            self.priority_window_tasklabel.append(Label( self.priority_window_labelframe, text=self.priority_window_tasklabel_text, font=self.COMMON_FONT))
            self.priority_window_tasklabel[-1].grid(column=0, row=(i), sticky="NESW")
            # entry
            self.priority_window_priorityentry_text = task_list[i][0]
            self.priority_window_priorityentry.append(Entry(self.priority_window_labelframe, font=self.COMMON_FONT))
            self.priority_window_priorityentry[-1].grid(column=1, row=(i), sticky="NESW")
            self.priority_window_priorityentry[-1].insert(0, self.priority_window_priorityentry_text)

        # Submit changes button frame
        self.priority_window_submit_button_frame = Frame(self.priority_window)
        self.priority_window_submit_button_frame.grid(column=0, row=1, sticky="NESW")
        self.priority_window_submit_button_frame.columnconfigure((0,1), weight=1)
        self.priority_window_submit_button_frame.rowconfigure((0), weight=1)
        
        # Submit changes button
        self.priority_window_submit_button_text = "Submit"
        self.priority_window_submit_button = Button(self.priority_window_submit_button_frame, text=self.priority_window_submit_button_text, font=self.COMMON_FONT, command= lambda: self.priority_submit(task_list))
        self.priority_window_submit_button.grid(column=0, row=0, sticky="NESW")

        # Cancel changes button
        self.priority_window_cancel_button_text = "Cancel"
        self.priority_window_cancel_button = Button(self.priority_window_submit_button_frame, text=self.priority_window_cancel_button_text, font=self.COMMON_FONT, command= lambda: self.priority_cancel())
        self.priority_window_cancel_button.grid(column=1, row=0, sticky="NESW")

    def priority_submit(self, task_list):
        ''' Submits priority changes '''

        global saved_users  

        for i in range(len(task_list)):
            saved_users[self.profile_user_username]["profiles"][self.profile_number][task_list[i][1]]["priority"] = self.priority_window_priorityentry[i].get()

        # Submits changes to database.
        with open("database.json", "w") as f:
           json.dump(saved_users, f,indent=4)

        self.priority_window.destroy()
        self.task_window(self.profile_number)

    def priority_cancel(self):
        ''' Closes the priority window '''

        self.priority_window.destroy()
        self.task_window(self.profile_number)

    def tasking(self, task_name):
        ''' Opens task windows'''

        # Getting the saved_users database
        global saved_users

        # Getting the task_info
        self.task_info = saved_users[self.profile_user_username]["profiles"][self.profile_number][task_name]["tasks"]
        
        # Changes recent edit label
        self.recent_edit_label_2.configure(text=task_name)

        # Opens Toplevel window that will be each task
        self.task_toplevel = Toplevel(self.root)
        self.task_toplevel.title(task_name.title())
        #self.task_toplevel.geometry("250x150")

        # Additional rows required for additional poins
        self.addtional_rows = len(self.task_info)

        # Weights for columns and rows
        self.task_toplevel.columnconfigure((1), weight=2)
        self.task_toplevel.columnconfigure((2+self.addtional_rows), weight=2)
        self.task_toplevel.rowconfigure((3+self.addtional_rows, 2+self.addtional_rows), weight=2)

        # Creating a line for each task in the task_info list
        self.task_toplevel_label = []
        self.task_toplevel_bulletpoint = []
        for i in range(len(self.task_info)):
            self.task_toplevel.rowconfigure((i), weight=2)
            # Label for bullet points (I might allow the user to change to - or a check box / other symbols if they wish to do so)
            self.task_toplevel_bulletpoint_symbol = "•" + " "
            self.task_toplevel_bulletpoint.append(Label(self.task_toplevel, text=self.task_toplevel_bulletpoint_symbol, font=self.COMMON_FONT))
            self.task_toplevel_bulletpoint[-1].grid(column=0, row=0+i, sticky="E")

            # Label for text within the task
            self.task_toplevel_label_text = self.task_info[i]
            self.task_toplevel_label.append(Label(self.task_toplevel, text=self.task_toplevel_label_text, font=self.COMMON_FONT))
            self.task_toplevel_label[-1].grid(column=1, row=0+i, sticky="W")

        # Edit button 
        # Edit button Frame
        self.task_toplevel_edit_frame = Frame(self.task_toplevel)
        self.task_toplevel_edit_frame.grid(column=2+self.addtional_rows, row=3+self.addtional_rows, sticky="NESW")
        # Edit button button
        self.task_toplevel_edit_frame.columnconfigure((0), weight=1)
        self.task_toplevel_edit_frame.rowconfigure((0), weight=1)
        self.task_toplevel_edit_button_image = PhotoImage(file= "edit_icon_photoimage.png")
        self.task_toplevel_edit_button = Button(self.task_toplevel_edit_frame, image=self.task_toplevel_edit_button_image, command= lambda: self.tasking_edit(task_name))  
        self.task_toplevel_edit_button.grid(column=0, row=0, sticky="NESW")

    def tasking_edit(self, task_name):
        ''' Allows the user to edit their task'''

        # Deletes old task text
        for i in range(len(self.task_toplevel_label)):
            self.task_toplevel_label[i].destroy()
        
        # Sets deletion and addition values to False
        self.del_point_run = False
        self.add_point_run = False

        # Additional rows required
        self.addtional_rows = len(self.task_info)

        # Change geometry
        geometry = str(450+(self.addtional_rows*50)) + "x" + str(150+(self.addtional_rows*50))
        self.task_toplevel.geometry(geometry)

        # Going through the list of points in the task and creating and entry for each of them. 
        self.task_toplevel_entry = []
        for i in range(len(self.task_info)):
            # Entry for user to enter new task in
            self.task_toplevel_entry.append(Entry(self.task_toplevel, font=self.COMMON_FONT))
            self.task_toplevel_entry[-1].grid(column=1, row=0+i, sticky="NESW")

            # Inserting the old text
            self.task_toplevel_label_text = self.task_info[i]
            self.task_toplevel_entry[-1].insert(0, self.task_toplevel_label_text)

        # Submit changes button frame
        self.task_toplevel_submit_button_frame = Frame(self.task_toplevel)
        self.task_toplevel_submit_button_frame.grid(column=1, row=3+self.addtional_rows, sticky="NESW")
        self.task_toplevel_submit_button_frame.columnconfigure((0,1), weight=1)
        self.task_toplevel_submit_button_frame.rowconfigure((0), weight=1)
        
        # Submit changes button
        self.task_toplevel_submit_button_text = "Submit"
        self.task_toplevel_submit_button = Button(self.task_toplevel_submit_button_frame, text=self.task_toplevel_submit_button_text, font=self.COMMON_FONT, command= lambda: self.submit_button(task_name))
        self.task_toplevel_submit_button.grid(column=0, row=0, sticky="NESW")

        # Cancel changes button
        self.task_toplevel_cancel_button_text = "Cancel"
        self.task_toplevel_cancel_button = Button(self.task_toplevel_submit_button_frame, text=self.task_toplevel_cancel_button_text, font=self.COMMON_FONT, command= lambda: self.cancel_button(task_name))
        self.task_toplevel_cancel_button.grid(column=1, row=0, sticky="NESW")

        # Add bullet point button
        # Frame
        self.task_toplevel_addpoint_frame = Frame(self.task_toplevel)
        self.task_toplevel_addpoint_frame.grid(column=2+self.addtional_rows, row=0, sticky="NESW")
        self.task_toplevel_addpoint_frame.columnconfigure((0), weight=1)
        self.task_toplevel_addpoint_frame.rowconfigure((0), weight=1)

        # Button
        self.task_toplevel_addpoint_button_text = "+" + "•"
        self.task_toplevel_addpoint_button = Button(self.task_toplevel_addpoint_frame, text=self.task_toplevel_addpoint_button_text, font=self.COMMON_FONT, command = lambda: self.add_point(task_name))
        self.task_toplevel_addpoint_button.grid(column=0, row=0, sticky="NESW")

        # Delete bullet point button(s)
        # Frame
        self.task_toplevel_delpoint_frame = Frame(self.task_toplevel)
        self.task_toplevel_delpoint_frame.grid(column=2+self.addtional_rows, row=1, sticky="NESW")
        self.task_toplevel_delpoint_frame.columnconfigure((0), weight=1)
        self.task_toplevel_delpoint_frame.rowconfigure((0,1), weight=1)

        # Button
        self.task_toplevel_delpoint_button_text = "-" + "•"
        self.task_toplevel_delpoint_button = Button(self.task_toplevel_delpoint_frame, text=self.task_toplevel_delpoint_button_text, font=self.COMMON_FONT, command= lambda: self.remove_point(task_name))
        self.task_toplevel_delpoint_button.grid(column=0, row=0, sticky="NESW")

        # Combobox
        self.task_toplevel_delpoint_combobox = ttk.Combobox(self.task_toplevel_delpoint_frame, state="readonly")
        task_toplevel_delpoint_combobox_values = []
        for i in range(len(self.task_info)):
            task_toplevel_delpoint_combobox_values.append(1+i)
        self.task_toplevel_delpoint_combobox['values'] = task_toplevel_delpoint_combobox_values
        self.task_toplevel_delpoint_combobox.grid(column=0, row=1, sticky="NESW")
        
    def add_point(self, task_name):
        ''' Adds points to the task (button will disable once a point is added, while I try find a way to let the user add multiple) '''
        global saved_users

        # Disables addpoint button
        self.task_toplevel_addpoint_button.configure(state=DISABLED)

        # Label for additional bullet points 
        self.task_toplevel_bulletpoint.append(Label(self.task_toplevel, text=self.task_toplevel_bulletpoint_symbol, font=self.COMMON_FONT))
        self.task_toplevel_bulletpoint[-1].grid(column=0, row=0+len(saved_users[self.profile_user_username]["profiles"][self.profile_number][task_name]), sticky="E")

        # Label for text within the task
        self.task_toplevel_entry.append(Entry(self.task_toplevel, font=self.COMMON_FONT))
        self.task_toplevel_entry[-1].grid(column=1, row=0+len(saved_users[self.profile_user_username]["profiles"][self.profile_number][task_name]), sticky="NESW")

        # Tells submit button that there was an addition of a new point
        self.add_point_run = True

    def remove_point(self, task_name):
        ''' Removes points from task '''
        global saved_users

        # Removes point from task_window
        point = self.task_toplevel_delpoint_combobox.get()
        if point == "":
            messagebox.showerror("Error", "Invalid input: Please enter a value in the combobox", parent=self.task_toplevel)
        else:  
            # Disables delpoint button
            self.task_toplevel_delpoint_button.configure(state=DISABLED)

            # Makes point into an integer
            self.point = int(point)

            # Deletes point from GUI
            self.task_toplevel_entry[self.point-1].destroy()
            self.task_toplevel_bulletpoint[self.point-1].destroy()

            # Tells submit button that deletion of point was run
            self.del_point_run = True
            # To do: Delete point from combobox list, reprint task window to be reformatted
    
    def cancel_button(self, task_name):
        ''' Cancels the edits done by the user, this method will cancel the edits done and send the user back into the task screen '''

        self.task_toplevel.destroy()
        self.tasking(task_name)


    def submit_button(self, task_name):
        ''' Submits edits to task '''

        # Checks if a point has been deleted
        if self.del_point_run == True:
            # Deletion from self.task_toplevel_entry
            del self.task_toplevel_entry[self.point-1]
            # Deletetion of point from database
            del saved_users[self.profile_user_username]["profiles"][self.profile_number][task_name]["tasks"][self.point-1]

        # Adds all current tasks to saved_users including any new tasks
        for i in range(len(self.task_toplevel_entry)):
            # Checks if a task exists in position, if task exists at position it changes task to new one, if task doesnt exist at that postion it adds it
            try:  
                # Edits tasks to be new tasks (will remain the same if the user hasnt changed it)
                saved_users[self.profile_user_username]["profiles"][self.profile_number][task_name]["tasks"][i] = self.task_toplevel_entry[i].get()
                
            except IndexError:
                # Addition of point saved_users
                saved_users[self.profile_user_username]["profiles"][self.profile_number][task_name]["tasks"].append(self.task_toplevel_entry[-1].get())

        # Adds changes to database
        with open("database.json", "w") as f:
           json.dump(saved_users, f,indent=4)

        self.task_toplevel.destroy()
        self.tasking(task_name)