import tkinter as tk
from tkinter import messagebox
import csv
import os

root = tk.Tk()
root.title("Registration form")
window_width = 700
window_height = 450

#to create window at the center of screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width-window_width)//2
y = (screen_height-window_height)//2

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.configure(bg="light green")
root.resizable(False,False)

#function which activates when the submit button is clicked
def submit_details():
    name = name_entry.get()
    course = course_entry.get()
    semester = semester_entry.get()
    form_no = form_no_entry.get()
    contact = contact_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    if name == '':
        messagebox.showerror('Error','Please Enter your Name')
    elif course == '':
        messagebox.showerror('Error','Please Enter your Course')
    elif semester == '':
        messagebox.showerror('Error','Please Enter your Semester')
    elif form_no == '':
        messagebox.showerror('Error','Please Enter your Form No.')
    elif contact == '':
        messagebox.showerror('Error','Please Enter your Contact No.')
    elif email == '':
        messagebox.showerror('Error','Please Enter your Email Id')
    elif address == '':
        messagebox.showerror('Error','Please Enter your Address')
    else:
        csv_file = "registration_details.csv"
        if not os.path.isfile(csv_file):
            with open(csv_file,mode='w',newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Name','Course','Semester','Form No.','Contact No.','Email Id','Address'])

        with open(csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name,course,semester,form_no,contact,email,address])
            message_label.config(text="Registration data has been added to csv successfully")


#to displya form label
form_label = tk.Label(text='Form',bg="light green",font='16')
form_label.place(x=300,y=0,width=100,height=25)


# for enter name
name_label = tk.Label(text='Name', bg="light green", font='16')
name_label.place(x=10,y=30,width=110,height=25)
name_entry = tk.Entry(font='16')
name_entry.place(x=120,y=30,width=450,height=25)

# for entering course
course_label = tk.Label(text='Course', bg="light green", font='16')
course_label.place(x=10,y=60,width=110,height=25)
course_entry = tk.Entry(font='16')
course_entry.place(x=120,y=60,width=450,height=25)

#for entering semester
semester_label = tk.Label(text='Semester', bg="light green", font='16')
semester_label.place(x=10,y=90,width=110,height=25)
semester_entry = tk.Entry(font='16')
semester_entry.place(x=120,y=90,width=450,height=25)

#for entering form no
form_no_label = tk.Label(text='Form No.', bg="light green", font='16')
form_no_label.place(x=10,y=120,width=110,height=25)
form_no_entry = tk.Entry(font='16')
form_no_entry.place(x=120,y=120,width=450,height=25)

#for entering contact no
contact_label = tk.Label(text='Contact No.', bg="light green", font='16')
contact_label.place(x=10,y=150,width=110,height=25)
contact_entry = tk.Entry(font='16')
contact_entry.place(x=120,y=150,width=450,height=25)

#for entering email id
email_label = tk.Label(text='Email Id', bg="light green", font='16')
email_label.place(x=10,y=180,width=110,height=25)
email_entry = tk.Entry(font='16')
email_entry.place(x=120,y=180,width=450,height=25)

#for entering adress
address_label = tk.Label(text='Address', bg="light green", font='16')
address_label.place(x=10,y=210,width=110,height=25)
address_entry = tk.Entry(font='16')
address_entry.place(x=120,y=210,width=450,height=25)

#button to submit details
submit = tk.Button(text='Submit',bg='red',font='16',command=submit_details)
submit.place(x=300,y=240,width=80)

message_label = tk.Label(text='', bg="light green", font='16')
message_label.place(x=100,y=280,height=25)


root.mainloop() 
