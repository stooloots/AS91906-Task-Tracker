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
        ''' Gets the username and password from their entries'''
        global saved_users

        # Gets username and password
        users_username = self.username_entry.get()
        users_password = self.password_entry.get()

        # Validates username and password
        if users_username in saved_users:
            if saved_users[users_username]["password"] == users_password:
                self.login.destroy()
                self.entry_window(users_username)
            else:
                messagebox.showerror("Error", "Invalid input: Please enter the correct username or password", parent=self.root)
        else:
            messagebox.showerror("Error", "Invalid input: Please enter the correct username or password", parent=self.root)
        
    def entry_remove(self, entry):
        ''' Removes default values when users hovers cursor over entry '''
        if entry == self.username_entry:
            if self.username_entry.get() == "Username":
                entry.delete(0, END)
        if entry == self.password_entry:
            if self.password_entry.get() == "Password":
                entry.delete(0, END)
                entry.configure(show="*")
    
    def entry_window(self, entry_user_username):
        ''' Entry window screen '''

        # Adding the users username to the class
        self.profile_user_username = entry_user_username

        # Resetting Root window
        self.root_reset()

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
    
    def root_reset(self):
        ''' Resets the root window to have no objects or weights '''
        # Resting window config
        for i in range(100):
            self.root.columnconfigure((i), weight = 0)
            self.root.rowconfigure((i), weight = 0)
        # Destroying anything open on the screen
        for child in self.root.winfo_children(): 
            child.destroy()
        
    def profile_entry_window(self):
        # This window will allow the user to create groupings for tasks

        # Retrieving saved_users
        global saved_users

        # Destroying old widgets
        self.entry_welcome_label.destroy()
        self.login_edit_frame.destroy()
        self.profile_enter_frame.destroy()
        self.root_reset()

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
            self.template_profile_button.append(Button(self.template_profile_frame[-1], wraplength=100, text=self.template_profile_frame_text, anchor="n", command=partial(self.task_window, profile_list[i]))) # Fixed by Jensen # Now sends "profile_list[i] instead of task dictionary"
            self.template_profile_button[-1].grid(column=0, row=0, sticky="NESW")

        # Profile add button
        # Frame new profile button
        self.new_profile_frame = Frame(self.root, highlightthickness=4, highlightbackground="#7F7F7F")
        self.new_profile_frame.grid(column=((len(profile_list))%3)*2+1, row= math.floor((len(profile_list))/3)*2+1, sticky="NESW")
        self.new_profile_frame.columnconfigure((0), weight= 1)
        self.new_profile_frame.rowconfigure((0), weight = 1)

        # Button for new profile frame
        self.new_profile_iamge = PhotoImage(file= "plus_photoimage.png")
        self.new_profile_button = Button(self.new_profile_frame, image=self.new_profile_iamge, relief="flat", command= lambda: self.new_profile(profile_list))
        self.new_profile_button.grid(column=0, row=0, sticky="NESW")

        # Profile edit button (includes deletion)
        # Frame edit proifle button
        self.profile_edit_frame = Frame(self.root, borderwidth=2, relief=SOLID)
        self.profile_edit_frame.grid(column=5, row= math.floor((((len(profile_list)+1)/3)*2+1)+3), sticky="NESW")
        self.profile_edit_frame.columnconfigure((0), weight= 1)
        self.profile_edit_frame.rowconfigure((0), weight = 1)

        # Button for profile edit frame
        self.profile_edit_text = "Edit Profiles"
        self.profile_edit_button = Button(self.profile_edit_frame, text=self.profile_edit_text, command= lambda: self.profile_edit(profile_list))
        self.profile_edit_button.grid(column=0, row=0, sticky="NESW")

        # Moves settings button to match
        settings_button_position = {"column":6, "row":math.floor((((len(profile_list)+1)/3)*2+1)+3)}
        # Adds settings button
        self.settings_button(settings_button_position)
    
    def profile_edit(self, profile_list):
        ''' Method that allows the user to edit their profiles / name / delete profiles'''

        # Retreieves saved_users
        global saved_users

        # Resets profile deletion
        self.profile_deletion = False

        # Creates toplevel window and makes it grabset
        self.profile_adjust_window = Toplevel()
        self.profile_adjust_window.grab_set()
        self.profile_adjust_window.title("Profile edit")

        # Additional rows required for len of profile
        profile_adjust_additional_rows = len(profile_list)

        # Setting grid layout        
        self.profile_adjust_window.columnconfigure((0,1), weight = 1)
        self.profile_adjust_window.rowconfigure((0, profile_adjust_additional_rows), weight = 1)

        # Setting labels for profiles
        self.profile_adjust_window_name_entry = []
        for i in range(len(profile_list)):
            # Setting additional row weights
            self.profile_adjust_window.rowconfigure(((i)), weight = 1)
            # entry
            self.profile_adjust_window_name_entry_text = profile_list[i]
            self.profile_adjust_window_name_entry.append(Entry(self.profile_adjust_window, font=self.COMMON_FONT))
            self.profile_adjust_window_name_entry[-1].grid(column=0, row=(i), sticky="NESW")
            self.profile_adjust_window_name_entry[-1].insert(0, self.profile_adjust_window_name_entry_text)
        
        # Submit changes button
        self.profile_adjust_window_submit_button_text = "Submit"
        self.profile_adjust_window_submit_button = Button(self.profile_adjust_window, text=self.profile_adjust_window_submit_button_text, font=self.COMMON_FONT, command= lambda: self.profile_submit(profile_list))
        self.profile_adjust_window_submit_button.grid(column=0, row=profile_adjust_additional_rows, sticky="NESW")

        # Cancel changes button
        self.profile_adjust_window_cancel_button_text = "Cancel"
        self.profile_adjust_window_cancel_button = Button(self.profile_adjust_window, text=self.profile_adjust_window_cancel_button_text, font=self.COMMON_FONT, command= lambda: self.profile_cancel())
        self.profile_adjust_window_cancel_button.grid(column=1, row=profile_adjust_additional_rows, sticky="NESW")

        # Deletion frame
        self.profile_adjust_window_del_frame = Frame(self.profile_adjust_window)
        self.profile_adjust_window_del_frame.grid(column=1, row=0, rowspan=2)

        # Deletion frame config
        self.profile_adjust_window_del_frame.columnconfigure((0), weight=1)
        self.profile_adjust_window_del_frame.rowconfigure((0,1), weight=1)

        # Combobox for profile deletion
        # Reseting deleted profiles
        self.deleted_profiles = []
        # Combobox
        self.profile_adjust_window_combobox = ttk.Combobox(self.profile_adjust_window_del_frame, state="readonly")
        self.profile_adjust_window_combobox_values = []
        for i in range(len(profile_list)):
            self.profile_adjust_window_combobox_values.append(profile_list[i])
        self.profile_adjust_window_combobox['values'] = self.profile_adjust_window_combobox_values
        self.profile_adjust_window_combobox.grid(column=0, row=0, sticky="NESW")

        # Button for deleting profile
        self.profile_adjust_window_delete_button_text = "Delete profile"
        self.profile_adjust_window_delete_button = Button(self.profile_adjust_window_del_frame, text=self.profile_adjust_window_delete_button_text, font=self.COMMON_FONT, command= lambda: self.profile_delete(profile_list))
        self.profile_adjust_window_delete_button.grid(column=0, row=1, sticky="NESW")

    def profile_delete(self, profile_list):
        ''' Allows for the deletion of profiles from the program'''

        # Grabs deleted profile name
        self.profile_deletion_value = self.profile_adjust_window_combobox.get()
    
        # Checks if combo has a value
        if self.profile_deletion_value == "":
            messagebox.showerror("Error", "Invalid input: Please enter a value in the combobox", parent=self.profile_adjust_window)
        else:  
            for i in range(len(self.profile_adjust_window_combobox_values)):
                # Gets position of value
                if self.profile_deletion_value == self.profile_adjust_window_combobox_values[i]:
                    deleted_profile_postion = i
            # Deletes profile from GUI
            self.profile_adjust_window_name_entry[deleted_profile_postion].destroy()
            del self.profile_adjust_window_name_entry[deleted_profile_postion]

            # Adds deleted profile name and postion to list
            try:
                self.deleted_profiles.append([self.profile_deletion_value, deleted_profile_postion])
            except:
                # Creates list to track deleted profiles
                self.deleted_profiles = []
                self.deleted_profiles.append([self.profile_deletion_value, deleted_profile_postion])

            # Removes deleted profile from combobox
            del self.profile_adjust_window_combobox_values[deleted_profile_postion]
            self.profile_adjust_window_combobox['values'] = self.profile_adjust_window_combobox_values
            self.profile_adjust_window_combobox.set("")

            # Tells the program a profile was deleted
            self.profile_deletion = True

        #self.profile_adjust_window.destroy()


    def profile_submit(self, profile_list):
        ''' Submits the edited profile names and changes'''

        # Retrieving saved_users
        global saved_users  

        # Checks if the user has deleted a profile
        if self.profile_deletion == True:
            for i in range(len(self.deleted_profiles)): # Deleted profiles is formatted like [["profile name", postion], ["profile_name", position]]
                del saved_users[self.profile_user_username]["profiles"][self.deleted_profiles[i][0]]
                if self.deleted_profiles[i][0] == profile_list[i]:
                    del profile_list[i]

        # Adds changes to saved_users
        for i in range(len(profile_list)):
            try:
                # Gets entry value
                profile_submit_value = self.profile_adjust_window_name_entry[i].get()
                if profile_submit_value != profile_list[i]:
                    # Changes key in saved_users
                    saved_users[self.profile_user_username]["profiles"][f"{profile_submit_value}"] = saved_users[self.profile_user_username]["profiles"][profile_list[i]]
                    del saved_users[self.profile_user_username]["profiles"][profile_list[i]]
            except:
                pass
        # Submits changes to database.
        with open("database.json", "w") as f:
            json.dump(saved_users, f,indent=4)
                

        self.profile_adjust_window.destroy()
        self.profile_entry_window()

    def profile_cancel(self):
        ''' Cancels the edits done to the profile names / deletion'''
        # Destroys window
        self.profile_adjust_window.destroy()

    
    def settings_button(self, positioning):
        ''' Method that adds a settings button to the bottom right of the page'''
        # Settings / Back button
        self.root.rowconfigure((positioning["column"]), weight=0)
        self.root.columnconfigure((positioning["row"]), weight=0)
        self.profile_entry_settings_button_image = PhotoImage(file= "settings_photoimage.png")
        self.profile_entry_settings_button = Button(self.root, image=self.profile_entry_settings_button_image ,command = lambda: self.entry_window(self.profile_user_username))
        self.profile_entry_settings_button.grid(column=positioning["column"], row=positioning["row"], sticky="NESW")

    def new_profile(self, profile_list):
        ''' This method allows the user to create new profiles'''

        # Disabled new_profile_button
        self.new_profile_button.configure(state=DISABLED)

        # Adds new profile in replacement for new_profile_button
        # New frame
        self.template_profile_frame.append(Frame(self.root, borderwidth=2, relief=SOLID))

        # Moving new_profile_button and profile_edit_button
        self.new_profile_frame.grid(column=((len(profile_list)+1)%3)*2+1, row= math.floor((len(profile_list)+1)/3)*2+1, sticky="NESW")
        # Frame and Entry
        self.template_profile_frame[-1].grid(column=((len(profile_list))%3)*2+1, row= math.floor((len(profile_list))/3)*2+1, sticky="NESW")
        self.template_profile_frame[-1].columnconfigure((0), weight= 1)
        self.template_profile_frame[-1].rowconfigure((0), weight = 1)

        # Entry placed in profile frame (created for profile) located inside profile entry window
        self.new_profile_entry = Entry(self.template_profile_frame[-1], justify='center')
        self.new_profile_entry.grid(column=0, row=0, sticky="NESW")
        self.new_profile_entry.insert(0, f"Profile {len(profile_list)+1}")

        # When the users presses enter whilst in the entry it will add the new task with, "" priority and "" tasks
        self.new_profile_entry.bind("<Return>", lambda e: self.new_profile_addition(profile_list))

    def new_profile_addition(self, profile_list):
        ''' This method adds the new profile to the database'''

        # Re-enables new_profile_button
        self.new_profile_button.configure(state=ACTIVE)

        # Grabs saved_users
        global saved_users

        # Gets new_task_name
        new_profile_name = self.new_profile_entry.get()

        # Deletes new_task_entry
        self.new_profile_entry.destroy()

        # Puts button in entry's place
        self.template_profile_frame_text = new_profile_name
        self.template_profile_button.append(Button(self.template_profile_frame[-1], text=self.template_profile_frame_text, anchor="n", command=partial(self.task_window, new_profile_name))) 
        self.template_profile_button[-1].grid(column=0, row=0, sticky="NESW")

        saved_users[self.profile_user_username]["profiles"][new_profile_name] = {}

        with open("database.json", "w") as f:
            json.dump(saved_users, f,indent=4)

    def task_window(self, profile_tasks):
        ''' This method will open the task window where all tasks are visible, profile_tasks is the tasks dictionary taken from the profile '''
        # profile tasks is a name
        # eg "profile 1", "profile 2"

        # Retreive saved_users
        global saved_users

        # Reseting page config
        self.root_reset()

        # Adds settings button
        settings_button_position = {"column":5, "row":1}
        self.settings_button(settings_button_position)

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
        self.root.rowconfigure((0), weight = 1)

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
        
        # Tasks
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
            self.template_task_button = Button(self.template_task_frame[-1], wraplength=100, text=self.template_task_frame_text, anchor="n", command= partial(self.tasking, task_list[i][1]))# task_list[i] sends task name
            self.template_task_button.grid(column=0, row=0, sticky="NESW")

        # new task button
        # new task additional rows
        self.new_task_additional_rows = len(self.template_task_frame)
        # Configuring rows to add the button
        self.task_window_frame1.rowconfigure(((self.new_task_additional_rows*2, ((self.new_task_additional_rows+1)*2))), weight = 1)
        self.task_window_frame1.rowconfigure(((self.new_task_additional_rows*2)+1), weight = 2)

        # Frame for new_task
        self.new_task_frame = Frame(self.task_window_frame1, highlightthickness=4, highlightbackground="#7F7F7F")
        self.new_task_frame.grid(column=1, row=((self.new_task_additional_rows*2)+1), sticky="NESW")
        self.new_task_frame.columnconfigure((0), weight= 1)
        self.new_task_frame.rowconfigure((0), weight = 1)

        # Label
        self.new_task_image = PhotoImage(file= "plus_photoimage.png")
        self.new_task_button = Button(self.new_task_frame, image=self.new_task_image, relief="flat", command= lambda: self.new_task(task_list))
        self.new_task_button.grid(column=0, row=0, sticky="NESW")

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

        self.profile_button_text = "Change Priority\n(0 - <10)"
        self.profile_button = Button(self.priority_button_frame, text=self.profile_button_text, command=lambda: self.priority_change(task_list))
        self.profile_button.grid(column=0, row=0, sticky="NESW")

        # Task Edit button (previously delete button)
        self.task_edit_button_frame = Frame(self.task_window_frame2, borderwidth=2, relief=SOLID)
        self.task_edit_button_frame.grid(column=0, row=5, sticky="NESW")
        self.task_edit_button_frame.columnconfigure((0), weight=1)
        self.task_edit_button_frame.rowconfigure((0), weight=1)

        self.task_edit_button_text = "Edit Tasks"
        self.task_edit_button = Button(self.task_edit_button_frame, text=self.task_edit_button_text, command= lambda: self.task_change(task_list))
        self.task_edit_button.grid(column=0, row=0, sticky="NESW")
    
    def new_task(self, task_list):
        ''' Allows the user to create a new task '''

        # Disabled new_task_button
        self.new_task_button.configure(state=DISABLED)

        # Adds new task above new_task_button
        # New frame
        self.template_task_frame.append(Frame(self.task_window_frame1, borderwidth=2, relief=SOLID))
        # additional rows and columns
        self.new_task_additional_rows = len(self.template_task_frame)
        self.task_window_frame1.rowconfigure(((self.new_task_additional_rows*2)), weight = 1)
        self.task_window_frame1.rowconfigure(((self.new_task_additional_rows*2)+1), weight = 2)
        # swaps position of new task button and new task
        self.new_task_frame.grid(column=1, row=((self.new_task_additional_rows*2)+1), sticky="NESW")
        # adds bottom row underneath
        self.task_window_frame1.rowconfigure(((self.new_task_additional_rows*2)+2), weight = 2)
        
        # Frame and Entry
        self.template_task_frame[-1].grid(column=1, row=(((self.new_task_additional_rows-1)*2)+1), sticky="NESW")
        self.template_task_frame[-1].columnconfigure((0), weight= 1)
        self.template_task_frame[-1].rowconfigure((0), weight = 1)

        # Entry placed in task frame (created for tasks) located inside profile entry window
        self.new_task_entry = Entry(self.template_task_frame[-1])
        self.new_task_entry.grid(column=0, row=0, sticky="NESW")
        self.new_task_entry.insert(0, f"task {len(self.template_task_frame)}")

        # When the users presses enter whilst in the entry it will add the new task with, "" priority and "" tasks
        self.new_task_entry.bind("<Return>", lambda e: self.new_task_addition(task_list))

    def new_task_addition(self, task_list):
        ''' Makes the new_task into an actual task '''

        # Re-enables new_task_button
        self.new_task_button.configure(state=ACTIVE)

        # Grabs saved_users
        global saved_users

        # Gets new_task_name
        new_task_name = self.new_task_entry.get()

        # Deletes new_task_entry
        self.new_task_entry.destroy()

        # Puts button in entry's place
        self.template_task_frame_text = new_task_name
        self.template_task_button = Button(self.template_task_frame[-1], text=self.template_task_frame_text, anchor="n", command= partial(self.tasking, new_task_name))
        self.template_task_button.grid(column=0, row=0, sticky="NESW")

        #try:
        saved_users[self.profile_user_username]["profiles"][self.profile_number][new_task_name] = {"priority": 0,
                                                                                                   "tasks": []}
        #except:
            # If program cant excetue the addition 

        task_list.append([0, f'{new_task_name}'])

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

        # Max and min values for entry box
        PRIORITY_MAX = 10
        PRIORITY_MIN = 0.0

        # Retrieving saved_users
        global saved_users  

        #
        priority_valid = []
        # Runs through each entry value and checks 1) If its a float or integer, 2) if its within the range
        for i in range(len(self.priority_window_priorityentry)):
            # Reseting priority state
            priority_valid.append(True)
            
            # Checks if entry box value is a float, if not sends error
            try:
                priority_value = float(self.priority_window_priorityentry[i].get())
            except:
                messagebox.showerror("Error", f"Invalid input on line {i+1}: Please enter an integer or decimal value in the entry", parent=self.priority_window)
                priority_valid[i] = False # Doesn't allow for the users changes to be saved
            
            # Checks if the user has entered all floats / integers
            if priority_valid[i] == True:
                # Checks if the user has entered values outside the range
                if priority_value >= PRIORITY_MAX or priority_value < PRIORITY_MIN:
                    messagebox.showerror("Error", f"Invalid input on line {i+1}: Please enter a value within the range (0 - <10)", parent=self.priority_window)
                    priority_valid[i] = False
                else:
                    # Changes old priority to new priority
                    saved_users[self.profile_user_username]["profiles"][self.profile_number][task_list[i][1]]["priority"] = priority_value
        
        # If none of the values are false the program will dump the changes
        if False not in priority_valid:
            # Submits changes to database.
            with open("database.json", "w") as f:
                json.dump(saved_users, f,indent=4)
                

            self.priority_window.destroy()
            self.task_window(self.profile_number)

    def priority_cancel(self):
        ''' Closes the priority window '''

        self.priority_window.destroy()
        self.task_window(self.profile_number)

    def task_change(self, task_list):
        ''' Allows the user to edit names or delete each task 
        | task  | drop do| <-- Frame
        | entry | wn menu| 
        |       |Delete task|
        | Submit| Cancel | 
        '''
        # Retreieves saved_users
        global saved_users

        # Resets task deletion
        self.task_deletion = False

        # Creates toplevel window and makes it grabset
        self.task_adjust_window = Toplevel()
        self.task_adjust_window.grab_set()
        self.task_adjust_window.title("Task edit")

        # Additional rows required for len of task
        task_adjust_additional_rows = len(task_list)

        # Setting grid layout        
        self.task_adjust_window.columnconfigure((0,1), weight = 1)
        self.task_adjust_window.rowconfigure((0, task_adjust_additional_rows), weight = 1)

        # Setting labels for tasks and priority
        self.task_adjust_window_task_entry = []
        for i in range(len(task_list)):
            # Setting additional row weights
            self.task_adjust_window.rowconfigure(((i)), weight = 1)
            # entry
            self.task_adjust_window_task_entry_text = task_list[i][1]
            self.task_adjust_window_task_entry.append(Entry(self.task_adjust_window, font=self.COMMON_FONT))
            self.task_adjust_window_task_entry[-1].grid(column=0, row=(i), sticky="NESW")
            self.task_adjust_window_task_entry[-1].insert(0, self.task_adjust_window_task_entry_text)
        
        # Submit changes button
        self.task_adjust_window_submit_button_text = "Submit"
        self.task_adjust_window_submit_button = Button(self.task_adjust_window, text=self.task_adjust_window_submit_button_text, font=self.COMMON_FONT, command= lambda: self.task_submit(task_list))
        self.task_adjust_window_submit_button.grid(column=0, row=task_adjust_additional_rows, sticky="NESW")

        # Cancel changes button
        self.task_adjust_window_cancel_button_text = "Cancel"
        self.task_adjust_window_cancel_button = Button(self.task_adjust_window, text=self.task_adjust_window_cancel_button_text, font=self.COMMON_FONT, command= lambda: self.task_cancel())
        self.task_adjust_window_cancel_button.grid(column=1, row=task_adjust_additional_rows, sticky="NESW")

        # Deletion frame
        self.task_adjust_window_del_frame = Frame(self.task_adjust_window)
        self.task_adjust_window_del_frame.grid(column=1, row=0, rowspan=2)

        # Deletion frame config
        self.task_adjust_window_del_frame.columnconfigure((0), weight=1)
        self.task_adjust_window_del_frame.rowconfigure((0,1), weight=1)

        # Combobox for task deletion
        # Reseting deleted tasks
        self.deleted_tasks = []

        # Combobox
        self.task_adjust_window_combobox = ttk.Combobox(self.task_adjust_window_del_frame, state="readonly")
        self.task_adjust_window_combobox_values = []
        for i in range(len(task_list)):
            self.task_adjust_window_combobox_values.append(task_list[i][1])
        self.task_adjust_window_combobox['values'] = self.task_adjust_window_combobox_values
        self.task_adjust_window_combobox.grid(column=0, row=0, sticky="NESW")

        # Button for deleting task
        self.task_adjust_window_delete_button_text = "Delete task"
        self.task_adjust_window_delete_button = Button(self.task_adjust_window_del_frame, text=self.task_adjust_window_delete_button_text, font=self.COMMON_FONT, command= lambda: self.task_delete(task_list))
        self.task_adjust_window_delete_button.grid(column=0, row=1, sticky="NESW")

    def task_delete(self, task_list):
        ''' Deletes the users task from the program '''

        # Grabs deleted task name
        self.task_deletion_value = self.task_adjust_window_combobox.get()
    
        # Checks if combo has a value
        if self.task_deletion_value == "":
            messagebox.showerror("Error", "Invalid input: Please enter a value in the combobox", parent=self.task_adjust_window)
        else:  
            for i in range(len(self.task_adjust_window_combobox_values)):
                # Gets position of value
                if self.task_deletion_value == self.task_adjust_window_combobox_values[i]:
                    deleted_task_postion = i
            # Deletes task from GUI
            self.task_adjust_window_task_entry[deleted_task_postion].destroy()
            del self.task_adjust_window_task_entry[deleted_task_postion]

            # Adds deleted task name and postion to list
            try:
                self.deleted_tasks.append([self.task_deletion_value, deleted_task_postion])
            except:
                # Creates list to track deleted tasks
                self.deleted_tasks = []
                self.deleted_tasks.append([self.task_deletion_value, deleted_task_postion])

            # Removes deleted task from combobox
            del self.task_adjust_window_combobox_values[deleted_task_postion]
            self.task_adjust_window_combobox['values'] = self.task_adjust_window_combobox_values
            self.task_adjust_window_combobox.set("")

            # Tells the program a task was deleted
            self.task_deletion = True

        #self.task_adjust_window.destroy()

    def task_submit(self, task_list):
        ''' Submits priority changes '''

        # Retrieving saved_users
        global saved_users  

        # Checks if the user has deleted a task
        if self.task_deletion == True:
            for i in range(len(self.deleted_tasks)): # Deleted tasks is formatted like [["task name", postion], ["task_name", position]]
                del saved_users[self.profile_user_username]["profiles"][self.profile_number][self.deleted_tasks[i][0]]
                if self.deleted_tasks[i][0] == task_list[i][0]:
                    del task_list[i]

        # Adds changes to saved_users
        for i in range(len(task_list)):
            try:
                # Gets entry value
                task_submit_value = self.task_adjust_window_task_entry[i].get()
                if task_submit_value != task_list[i][1]:
                    # Changes key in saved_users
                    saved_users[self.profile_user_username]["profiles"][self.profile_number][f"{task_submit_value}"] = saved_users[self.profile_user_username]["profiles"][self.profile_number][task_list[i][1]]
                    del saved_users[self.profile_user_username]["profiles"][self.profile_number][task_list[i][1]]
            except:
                pass
        # Submits changes to database.
        with open("database.json", "w") as f:
            json.dump(saved_users, f,indent=4)
                
        # Deletes task_adjust_window
        self.task_adjust_window.destroy()
        # Re-opens task_window
        self.task_window(self.profile_number)

    def task_cancel(self):
        ''' Closes the priority window '''

        self.task_adjust_window.destroy()
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

        # Disabling self.task_toplevel_edit_button button
        self.task_toplevel_edit_button.configure(state=DISABLED)

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

        # Task info
        self.task_toplevel.rowconfigure((0), weight=2)
        
        # Label for bullet points (I might allow the user to change to - or a check box / other symbols if they wish to do so)
        self.task_toplevel_bulletpoint_symbol = "•" + " "
        self.task_toplevel_bulletpoint.append(Label(self.task_toplevel, text=self.task_toplevel_bulletpoint_symbol, font=self.COMMON_FONT))
        self.task_toplevel_bulletpoint[-1].grid(column=0, row=(len(self.task_toplevel_entry)), sticky="E")
        
        # Entry for new task
        self.task_toplevel_entry.append(Entry(self.task_toplevel, font=self.COMMON_FONT))
        self.task_toplevel_entry[-1].grid(column=1, row=(len(self.task_toplevel_entry)-1), sticky="NESW")

        # Default text for new entry
        self.task_toplevel_label_text = "No information provided"
        self.task_toplevel_entry[-1].insert(0, self.task_toplevel_label_text)

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

        # Re enabling task edit button
        self.task_toplevel_edit_button.configure(state=ACTIVE)

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