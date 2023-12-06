import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "user" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, {}".format(username))
        login_window.withdraw()  # Hide the login window
        open_homepage()  # Open the homepage window
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def open_homepage():
    global homepage_window
    homepage_window = tk.Toplevel() 
    homepage_window.title("Homepage")

    label_welcome = tk.Label(homepage_window, text="Welcome to the Homepage!")
    label_welcome.pack()

    button_logout = tk.Button(homepage_window, text="Logout", command=logout)
    button_logout.pack()

def logout():
    homepage_window.destroy() 
    login_window.deiconify() 

# Create the main login window
login_window = tk.Tk()
login_window.title("Login Page")

label_username = tk.Label(login_window, text="Username:")
label_username.pack()
entry_username = tk.Entry(login_window)
entry_username.pack()

label_password = tk.Label(login_window, text="Password:")
label_password.pack()
entry_password = tk.Entry(login_window, show="*") 

button_login = tk.Button(login_window, text="Login", command=login)
button_login.pack()

login_window.mainloop()
