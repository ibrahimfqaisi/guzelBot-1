import tkinter as tk
import tkinter.simpledialog as simpledialog
from tkinter import Button, messagebox
import psycopg2
import hashlib

'''
Ibrahim
Bayan 
Aseel
'''

def login():
    # Implement the login functionality here
    email = login_email_entry.get()
    password = login_password_entry.get()

    # Connect to the PostgreSQL database
    conn = psycopg2.connect("postgres://vfpgukpn:w4ArNUg7hh4GJkEt9Y6RK3jxzP_-ratk@ruby.db.elephantsql.com/vfpgukpn")
    cursor = conn.cursor()

    # Check if the email exists in the database
    query = "SELECT * FROM users WHERE email = %s"
    cursor.execute(query, (email,))
    user = cursor.fetchone()

    if user:
        # Hash the entered password
        entered_password_hash = hashlib.sha256(password.encode()).hexdigest()

        # Compare the hashed passwords
        if entered_password_hash == user[3]:  # Assuming the password hash is stored in column index 4
            messagebox.showinfo("Login Successful", f"Welcome, {user[1]}!")
        else:
            messagebox.showerror("Login Failed", "Invalid Password")
    else:
        messagebox.showerror("Login Failed", "Invalid Email")

    # Close the connection
    conn.close()

login_email_entry=""
login_password_entry=""


def show_login_page(root,show_signup_page, show_reset_page):
    root.geometry("300x200")
    root.title("Login Page")

    login_frame = tk.Frame(root)

    login_email_label = tk.Label(login_frame, text="Email")
    login_email_label.pack()

    global login_email_entry
    login_email_entry = tk.Entry(login_frame)
    login_email_entry.pack()

    global login_password_entry
    login_password_label = tk.Label(login_frame, text="Password")
    login_password_label.pack()

    login_password_entry = tk.Entry(login_frame, show="*")
    login_password_entry.pack()

    login_button = Button(login_frame, text="Login", command=login)
    login_button.pack()

    signup_link_label = tk.Label(login_frame, text="Don't have an account? Sign up!", fg="blue", cursor="hand2")
    signup_link_label.pack()
    signup_link_label.bind("<Button-1>", lambda event: show_signup_page(root))

    reset_link_label = tk.Label(login_frame, text="Forgot password? Reset it!", fg="blue", cursor="hand2")
    reset_link_label.pack()
    reset_link_label.bind("<Button-1>", lambda event: show_reset_page(root))

    login_frame.pack()

