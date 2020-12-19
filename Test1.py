import tkinter as tk
from tkinter import *

def submitact():
    user = Username.get()
    passw = password.get()

    print(f"The name entered by you is {user} and your password is {passw}")

root = tk.Tk()
root.geometry("300x300")
root.title("DBMS Login Page")

C = Canvas(root, bg="blue", height=250, width=300)

# Definging the first row 
lblfrstrow = tk.Label(root, text="Username -", )
lblfrstrow.place(x=50, y=20)

Username = tk.Entry(root, width=35)
Username.place(x=150, y=20, width=100)

lblsecrow = tk.Label(root, text="Password -")
lblsecrow.place(x=50, y=50)

password = tk.Entry(root, width=35)
password.place(x=150, y=50, width=100)

submitbtn = tk.Button(root, text="Login",bg='blue', command=submitact)
submitbtn.place(x=150, y=135, width=55)

root.mainloop() 