import tkinter as tk
from tkinter import messagebox
import csv
import os
from datetime import datetime

#to create main widget window
root = tk.Tk()
root.title("Marksheet")
window_width = 850
window_height = 300

#to create window at the center of screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width-window_width)//2
y = (screen_height-window_height)//2

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

root.resizable(False,False)

#to handle operation after submit is clicked i.e creating GPA
def display():
	
    name = name_entry.get()
    reg = reg_entry.get()
    roll = roll_entry.get()
    sub1 = sub1_entry.get()
    sub2 = sub2_entry.get()
    sub3 = sub3_entry.get()
    sub4 = sub4_entry.get()
	
    if name == '':
        messagebox.showerror('Error','Please Enter your Name')
    elif reg == '':
        messagebox.showerror('Error','Please Enter Reg. No.')
    elif roll == '':
        messagebox.showerror('Error','Please Enter your Roll No.')
    elif sub1 == '':
        messagebox.showerror('Error','Please Enter your Grade of CS 201')
    elif sub2 == '':
        messagebox.showerror('Error','Please Enter your Grade of CS 202')
    elif sub3 == '':
        messagebox.showerror('Error','Please Enter your Grade of MA 201')
    elif sub4 == '':
        messagebox.showerror('Error','Please Enter your Grade of EC 201')
    else:

        # Variable to store total marks
        tot = 0

        # grade is A
        # so credit obtained is 10*subject credit
        if sub1_entry.get() == "A":
            tk.Label(text="40",font='16').place(x=630,y=90,width=200,height=25)
            tot += 40

        # grade is B
        # so credit obtained is 9*subject credit
        if sub1_entry.get() == "B":
            tk.Label(text="36",font='16').place(x=630,y=90,width=200,height=25)
            tot += 36

        # grade is C
        # so credit obtained is 8*subject credit
        if sub1_entry.get() == "C":
            tk.Label(text="32",font='16').place(x=630,y=90,width=200,height=25)
            tot += 32
            
        # grade is D
        # so credit obtained is 7*subject credit
        if sub1_entry.get() == "D":
            tk.Label(text="28",font='16').place(x=630,y=90,width=200,height=25)
            tot += 28

        # grade is E
        # so credit obtained is 6*subject credit
        if sub1_entry.get() == "E":
            tk.Label(text="24",font='16').place(x=630,y=90,width=200,height=25)
            tot += 24

        # grade is F
        # so credit obtained is 0*subject credit
        if sub1_entry.get() == "F":
            tk.Label(text="0",font='16').place(x=630,y=90,width=200,height=25)
            tot += 0

        # Similarly doing with other objects
        if sub2_entry.get() == "A":
            tk.Label(text="40",font='16').place(x=630,y=120,width=200,height=25)
            tot += 40
        if sub2_entry.get() == "B":
            tk.Label(text="36",font='16').place(x=630,y=120,width=200,height=25)
            tot += 36
        if sub2_entry.get() == "C":
            tk.Label(text="32",font='16').place(x=630,y=120,width=200,height=25)
            tot += 32
        if sub2_entry.get() == "D":
            tk.Label(text="28",font='16').place(x=630,y=120,width=200,height=25)
            tot += 28
        if sub2_entry.get() == "E":
            tk.Label(text="24",font='16').place(x=630,y=120,width=200,height=25)
            tot += 24
        if sub2_entry.get() == "F":
            tk.Label(text="0",font='16').place(x=630,y=120,width=200,height=25)
            tot += 0

        if sub3_entry.get() == "A":
            tk.Label(text="30",font='16').place(x=630,y=150,width=200,height=25)
            tot += 30
        if sub3_entry.get() == "B":
            tk.Label(text="27",font='16').place(x=630,y=150,width=200,height=25)
            tot += 27
        if sub3_entry.get() == "C":
            tk.Label(text="24",font='16').place(x=630,y=150,width=200,height=25)
            tot += 24
        if sub3_entry.get() == "D":
            tk.Label(text="21",font='16').place(x=630,y=150,width=200,height=25)
            tot += 21
        if sub3_entry.get() == "E":
            tk.Label(text="18",font='16').place(x=630,y=150,width=200,height=25)
            tot += 24
        if sub3_entry.get() == "F":
            tk.Label(text="0",font='16').place(x=630,y=150,width=200,height=25)
            tot += 0

        if sub4_entry.get() == "A":
            tk.Label(text="40",font='16').place(x=630,y=180,width=200,height=25)
            tot += 40
        if sub4_entry.get() == "B":
            tk.Label(text="36",font='16').place(x=630,y=180,width=200,height=25)
            tot += 36
        if sub4_entry.get() == "C":
            tk.Label(text="32",font='16').place(x=630,y=180,width=200,height=25)
            tot += 32
        if sub4_entry.get() == "D":
            tk.Label(text="28",font='16').place(x=630,y=180,width=200,height=25)
            tot += 28
        if sub4_entry.get() == "E":
            tk.Label(text="24",font='16').place(x=630,y=180,width=200,height=25)
            tot += 24
        if sub4_entry.get() == "F":
            tk.Label(text="0",font='16').place(x=630,y=180,width=200,height=25)
            tot += 0

        # to display total credits
        tk.Label(text=str(tot),font='16').place(x=630,y=210,width=200,height=25)

        # to display SGPA
        tk.Label(text=str(tot/15),font='16').place(x=630,y=240,width=200,height=25)



#for entering name
name_label = tk.Label(text='Name', font='16')
name_label.place(x=5,y=0,width=100,height=25)
name_entry = tk.Entry(font='16')
name_entry.place(x=110,y=0,width=200,height=25)

#for entering Reg.no
reg_label = tk.Label(text='Reg.No', font='16')
reg_label.place(x=510,y=0,width=120,height=25)
reg_entry = tk.Entry(font='16')
reg_entry.place(x=630,y=0,width=200,height=25)

# for entering rollno
roll_label = tk.Label(text='Roll.No', font='16')
roll_label.place(x=5,y=30,width=100,height=25)
roll_entry = tk.Entry(font='16')
roll_entry.place(x=110,y=30,width=200,height=25)

#for labeling srl no.
srl_label = tk.Label(text='Srl.No', font='16')
srl_label.place(x=5,y=60,width=100,height=25)

#for labeling subject title
subject_label = tk.Label(text='Subject', font='16')
subject_label.place(x=140,y=60,width=100,height=25)

# to display grade label
grade_label = tk.Label(text='Grade', font='16')
grade_label.place(x=310,y=60,width=200,height=25)

#to display sub credit 
sub_credit_label = tk.Label(text='Sub Credit', font='16')
sub_credit_label.place(x=510,y=60,width=120,height=25)

#to display credit obtained label
credit_obtained_label = tk.Label(text='Credit Obainted', font='16')
credit_obtained_label.place(x=630,y=60,width=200,height=25)


#for labeling subjectsss
sr1_label = tk.Label(text='1', font='16') #to display serial number
sr1_label.place(x=5,y=90,width=100,height=25) #to place position of serial label
sub1_label = tk.Label(text='CS 201', font='16') # to display CS 201 subject label
sub1_label.place(x=140,y=90,width=100,height=25)
sub1_entry = tk.Entry(font='16') # to input grades of CS201 subject
sub1_entry.place(x=310,y=90,width=200,height=25)
sc1_label = tk.Label(text='4',font='16')#to display Sub Credit for CS201 subject
sc1_label.place(x=510,y=90,width=120,height=25)

sr2_label = tk.Label(text='2', font='16')
sr2_label.place(x=5,y=120,width=100,height=25)
sub2_label = tk.Label(text='CS 202', font='16')
sub2_label.place(x=140,y=120,width=100,height=25)
sub2_entry = tk.Entry(font='16') # to input grades of CS201 subject
sub2_entry.place(x=310,y=120,width=200,height=25)
sc2_label = tk.Label(text='4',font='16')
sc2_label.place(x=510,y=120,width=120,height=25)

sr3_label = tk.Label(text='3', font='16')
sr3_label.place(x=5,y=150,width=100,height=25)
sub3_label = tk.Label(text='MA 201', font='16')
sub3_label.place(x=140,y=150,width=100,height=25)
sub3_entry = tk.Entry(font='16') # to input grades of CS201 subject
sub3_entry.place(x=310,y=150,width=200,height=25)
sc3_label = tk.Label(text='4',font='16')#to display Sub Credit for CS201 subject
sc3_label.place(x=510,y=150,width=120,height=25)

sr4_label = tk.Label(text='4', font='16')
sr4_label.place(x=5,y=180,width=100,height=25)
sub4_label = tk.Label(text='EC 201', font='16')
sub4_label.place(x=140,y=180,width=100,height=25)
sub4_entry = tk.Entry(font='16') # to input grades of CS201 subject
sub4_entry.place(x=310,y=180,width=200,height=25)
sc4_label = tk.Label(text='4',font='16')#to display Sub Credit for CS201 subject
sc4_label.place(x=510,y=180,width=120,height=25)


#to display total credit label
Total_credit_label = tk.Label(text='Total credit', font='16')
Total_credit_label.place(x=510,y=210,width=120,height=25)

#to display GPA label
gpa_label = tk.Label(text='GPA', font='16')
gpa_label.place(x=510,y=240,width=120,height=25)



# to create submit button
submit = tk.Button(text='Submit',bg='green',font='16',command=display)
submit.place(x=140,y=240,width=100,height=30)



root.mainloop()


