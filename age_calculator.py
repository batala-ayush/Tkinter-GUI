import tkinter as tk
from tkinter import messagebox
import csv
import os
from datetime import datetime

#to create main widget window
root = tk.Tk()
root.title("Age Calculator")
window_width = 850
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
def calculate_age():
    birth_day = day_entry.get()
    birth_month = month_entry.get()
    birth_year = year_entry.get()
    given_day = given_day_entry.get()
    given_month = given_month_entry.get()
    given_year = given_year_entry.get()
    if birth_day == '':
        messagebox.showerror('Error','Please Enter your Birth Day')
    elif birth_month == '':
        messagebox.showerror('Error','Please Enter your Birth Month')
    elif birth_year == '':
        messagebox.showerror('Error','Please Enter your Birth Year')
    elif given_day == '':
        messagebox.showerror('Error','Please Enter Current Day')
    elif given_month == '':
        messagebox.showerror('Error','Please Enter Current Month')
    elif given_year == '':
        messagebox.showerror('Error','Please Enter Current Year')
    else:
        try:
            #print("i will do this")
            date1 = datetime(int(birth_year),int(birth_month),int(birth_day))
            date2 = datetime(int(given_year),int(given_month),int(given_day))
            difference = date2- date1
            years = difference.days//365
            months = (difference.days%365)//30
            days = (difference.days%365)%30
            
            calculated_year_entry.delete(0, tk.END)#clears the entry box
            calculated_year_entry.insert(0, years)#fill the entry box by calculated years

            calculated_month_entry.delete(0, tk.END)
            calculated_month_entry.insert(0, months)

            calculated_day_entry.delete(0, tk.END)
            calculated_day_entry.insert(0, days)
        except:
            messagebox.showerror('Error', 'Invalid date format')

#to clear the data
def clear_data():
    day_entry.delete(0, tk.END)
    month_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    given_day_entry.delete(0, tk.END)
    given_month_entry.delete(0, tk.END)
    given_year_entry.delete(0, tk.END)
    calculated_year_entry.delete(0, tk.END)
    calculated_month_entry.delete(0, tk.END)
    calculated_day_entry.delete(0, tk.END)


#to disply date of birth label
data_of_birth_label = tk.Label(text='Date Of Birth',bg="Blue",font='16')
data_of_birth_label.place(x=100,y=0,height=25)


# for enter date of birth day
day_label = tk.Label(text='Day', bg="light green", font='16')
day_label.place(x=10,y=30,width=50,height=25)
day_entry = tk.Entry(font='16')
day_entry.place(x=70,y=30,width=200,height=25)

# for entering date of birth month
month_label = tk.Label(text='Month', bg="light green", font='16')
month_label.place(x=10,y=60,width=50,height=25)
month_entry = tk.Entry(font='16')
month_entry.place(x=70,y=60,width=200,height=25)

#for entering date of birth year
year_label = tk.Label(text='Year', bg="light green", font='16')
year_label.place(x=10,y=90,width=50,height=25)
year_entry = tk.Entry(font='16')
year_entry.place(x=70,y=90,width=200,height=25)


#to disply current date label
given_date_label = tk.Label(text='Given Date',bg="Blue",font='16')
given_date_label.place(x=650,y=0,height=25)



#for entering given day
given_day_label = tk.Label(text='Given Day', bg="light green", font='16')
given_day_label.place(x=470,y=30,width=120,height=25)
given_day_entry = tk.Entry(font='16')
given_day_entry.place(x=600,y=30,width=200,height=25)

#for entering given month
given_month_label = tk.Label(text='Given Month', bg="light green", font='16')
given_month_label.place(x=470,y=60,width=120,height=25)
given_month_entry = tk.Entry(font='16')
given_month_entry.place(x=600,y=60,width=200,height=25)

#for entering given month
given_year_label = tk.Label(text='Given Year', bg="light green", font='16')
given_year_label.place(x=470,y=90,width=120,height=25)
given_year_entry = tk.Entry(font='16')
given_year_entry.place(x=600,y=90,width=200,height=25)



#button to calculate resultant
resultant_age = tk.Button(root,text='Resultant Age',bg='red',font='16',command=calculate_age)
resultant_age.place(x=300,y=120,height=25)

#to display calculated years
calculated_year_label = tk.Label(text='Years', bg="light green", font='16')
calculated_year_label.place(x=270,y=150,width=200,height=25)
calculated_year_entry = tk.Entry(font='16')
calculated_year_entry.place(x=270,y=180,width=200,height=25)

#to display calculated months
calculated_month_label = tk.Label(text='Months', bg="light green", font='16')
calculated_month_label.place(x=270,y=210,width=200,height=25)
calculated_month_entry = tk.Entry(font='16')
calculated_month_entry.place(x=270,y=240,width=200,height=25)

#to display calculated day
calculated_day_label = tk.Label(text='Days', bg="light green", font='16')
calculated_day_label.place(x=270,y=270,width=200,height=25)
calculated_day_entry = tk.Entry(font='16')
calculated_day_entry.place(x=270,y=300,width=200,height=25)

#button to calculate clear
clear_data = tk.Button(root,text='Clear All',bg='red',font='16',command=clear_data)
clear_data.place(x=320,y=330,height=25)



root.mainloop() 
