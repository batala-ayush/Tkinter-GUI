import tkinter as tk
from tkinter import messagebox
import csv
import os
import json
from datetime import datetime

user_data =[] # to save user regsitraion data

# Function to save user data to a JSON file
def save_user_data():
    with open("user_data.json", "w") as json_file:
        json.dump(user_data, json_file)

# Function to load user data from a file
def load_user_data():
    try:
        with open("user_data.json", 'r') as file:
            data = json.load(file)
            user_data.extend(data)
    except FileNotFoundError:
        pass

load_user_data()


#to create main widget window
root = tk.Tk()
root.title("Email System")
window_width = 1150
window_height = 600

#to create window at the center of screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width-window_width)//2
y = (screen_height-window_height)//2

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.configure(bg="yellow")
root.resizable(False,False)

#action to be done after register button is clicked
def register_action():
    already_registered = False
    name = register_name_entry.get()
    email = register_email_entry.get()
    mobile = register_mobile_entry.get()
    age = register_age_entry.get()
    gender = selected_option.get()
    password = register_password_entry.get()
    reenter_password = reenter_password_entry.get()

    if name == '':
        messagebox.showerror('Error','Please Enter your Name')
    elif email == '':
        messagebox.showerror('Error','Please Enter your Email')
    elif mobile == '':
        messagebox.showerror('Error','Please Enter your Mobile')
    elif age == '':
        messagebox.showerror('Error','Please Enter your Age')
    elif gender == '':
        messagebox.showerror('Error','Please Choose your Gender')
    elif password == '':
        messagebox.showerror('Error','Please Enter your Password')
    elif reenter_password == '':
        messagebox.showerror('Error','Please Re-Enter your Password')
    else:
        for user in user_data:
            if email == user['email']:
                messagebox.showerror("Registration Failed", "Email already registered")
                already_registered = True
                break
        if not already_registered:
            if password != reenter_password:
                messagebox.showerror("Registration Failed", "Passwords do not match")
            else:
                # Store the user data in the dictionary
                user_data.append({"name": name,"email":email,"mobile": mobile, "age": age, "gender": gender, "password": password})
                messagebox.showinfo("Registration Successful", "You are registered!")
                save_user_data()  # Save the user data to a JSON file

#action to be done after login button is clicked
def login_action():
    logged = False
    email = email_entry.get()
    password = password_entry.get()
    if email == '':
        messagebox.showerror('Error', 'Please Enter your Email')
    elif password == '':
        messagebox.showerror('Error', 'Please Enter your Password')
    else:
        for user in user_data:
            if email == user["email"] and password == user["password"]:
                messagebox.showinfo("Login Successful", "Welcome, User!")
                logged = True
                break  # Exit the loop after a successful login
        if not logged:
            messagebox.showerror("Login Failed", "Invalid email or password")



#Frame for login
login_frame = tk.Frame(root, width=470,height=195,relief='solid',borderwidth=2)
login_frame.place(x=50, y=50)  


# for entering email
email_label = tk.Label(login_frame,text='Enter Email', font='16')
email_label.place(x=10,y=30,height=30)
email_entry = tk.Entry(login_frame,font='16')
email_entry.place(x=170,y=30,width=250,height=30)

# for entering password
password_label = tk.Label(login_frame,text='Enter Password', font='16')
password_label.place(x=10,y=85,height=30)
password_entry = tk.Entry(login_frame,font='16')
password_entry.place(x=170,y=85,width=250,height=30)

#button to login 
login = tk.Button(login_frame,text='Login',font='16',command=login_action)
login.place(x=200,y=140,width=200,height=45)

#frame for register
register_frame = tk.Frame(root, width=500, height=500,relief='solid',borderwidth=2)
register_frame.place(x=600, y=50)  

# for entering email to register
register_name_label = tk.Label(register_frame,text='Enter Name', font='16')
register_name_label.place(x=10,y=30,height=30)
register_name_entry = tk.Entry(register_frame,font='16')
register_name_entry.place(x=220,y=30,width=250,height=30)

# for entering email to register
register_email_label = tk.Label(register_frame,text='Enter Email',font='16')
register_email_label.place(x=10,y=85,height=30)
register_email_entry = tk.Entry(register_frame,font='16')
register_email_entry.place(x=220,y=85,width=250,height=30)

# for entering email to register
register_mobile_label = tk.Label(register_frame,text='Enter Mobile',font='16')
register_mobile_label.place(x=10,y=140,height=30)
register_mobile_entry = tk.Entry(register_frame,font='16')
register_mobile_entry.place(x=220,y=140,width=250,height=30)

# for entering email to register
register_age_label = tk.Label(register_frame,text='Enter Age',font='16')
register_age_label.place(x=10,y=195,height=30)
register_age_entry = tk.Entry(register_frame,font='16')
register_age_entry.place(x=220,y=195,width=250,height=30)

#listbox to select gender
register_gender_label = tk.Label(register_frame,text='Select Gender',font='16')
register_gender_label.place(x=10,y=250,height=30)
selected_option = tk.StringVar()
register_gender_dropdown = tk.OptionMenu(register_frame,selected_option,'Male','Female','Other')
register_gender_dropdown.place(x=220,y=250,width=250,height=35)
register_gender_dropdown.configure(font='16')


# for entering password to register
register_password_label = tk.Label(register_frame,text='Enter Password',font='16')
register_password_label.place(x=10,y=305,height=30)
register_password_entry = tk.Entry(register_frame,font='16')
register_password_entry.place(x=220,y=305,width=250,height=30)

# for re-entering password
reenter_password_label = tk.Label(register_frame,text='Re-Enter Password',font='16')
reenter_password_label.place(x=10,y=360,height=30)
reenter_password_entry = tk.Entry(register_frame,font='16')
reenter_password_entry.place(x=220,y=360,width=250,height=30)

#button to register
register = tk.Button(register_frame,text='Register',font='16',command=register_action)
register.place(x=250,y=415,width=200,height=45)




root.mainloop()
