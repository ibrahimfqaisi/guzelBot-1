import tkinter as tk
from tkinter import *
import tkinter.simpledialog as simpledialog
from tkinter import messagebox
import psycopg2
import hashlib
import smtplib
from email.message import EmailMessage
import login2
import register_page
from PIL import ImageTk, Image

from tkinter import Button, messagebox
import os

from dotenv import load_dotenv

load_dotenv()
connectDatabase = os.getenv("conn")

# from reset_page import EntryMessageWindow
class EntryMessageWindow:
    def __init__(self, title, message):
        self.code_confirmation = None

        self.win = Toplevel()
        window_width = 350
        window_height = 350
        screen_width = self.win.winfo_screenwidth()
        screen_height = self.win.winfo_screenheight()
        position_top = int(screen_height / 4 - window_height / 4)
        position_right = int(screen_width / 2 - window_width / 2)
        self.win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

        self.win.title(title)
        self.win.configure(background='#272A37')
        self.win.resizable(False, False)
        

        home_bgImg = Image.open('python\\new\\Guzel.png')
        home_bgImg = home_bgImg.resize((370, 360))

        photo = ImageTk.PhotoImage(home_bgImg)
        home_bg = Label(self.win, image=photo, bg='#525561')
        home_bg.image = photo
        home_bg.place(x=-10, y=-10)




        self.email_entry = Entry(self.win, bg="#A28DCF", font=("yu gothic ui semibold", 12), highlightthickness=1, bd=0)
        self.email_entry.place(x=40, y=110, width=256, height=50)
        self.email_entry.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
        email_label = Label(self.win, text=message, fg="#FFFFFF", bg='#623F82', font=("yu gothic ui", 11, 'bold'))
        email_label.place(x=20, y=50)

        update_pass = Button(self.win, fg='#f8f8f8', text='submit', bg='#53A9D4', font=("yu gothic ui", 12, "bold"),
                             cursor='hand2', relief="flat", bd=0, highlightthickness=0, activebackground="#623F82",
                             command=self.get_email)
        update_pass.place(x=40, y=200, width=256, height=45)

        self.win.protocol("WM_DELETE_WINDOW", self.on_close)

        self.win.wait_window()

    def get_email(self):
        self.code_confirmation= self.email_entry.get()
        self.win.destroy()

    def on_close(self):
        self.win.destroy()

def show_custom_error(title, message):
    global win
    win = Toplevel()
    
    window_width = 350
    window_height = 150
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    win.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
    win.title(title)
    win.configure(background="#6C5692")
    win.resizable(False, False)

    label = Label(win, text=message, fg="white", bg="#6C5692")
    label.pack(pady=20)

    ok_button = Button(win, text="OK", command=win.destroy)
    ok_button.pack(pady=10)
def signup(signup_first_name_entry, signup_last_name_entry, signup_email_entry, signup_password_entry):
    first_name = signup_first_name_entry.get()
    last_name = signup_last_name_entry.get()
    username = f'{first_name} {last_name}'
    email = signup_email_entry.get()
    password = signup_password_entry.get()
    
    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(connectDatabase)
    cursor = conn.cursor()

    # Check if the email already exists in the database
    query = "SELECT * FROM users WHERE email = %s"
    cursor.execute(query, (email,))
    existing_user = cursor.fetchone()

    if existing_user:
        show_custom_error("Sign Up Failed", "Email already exists in the database")
    else:
        code = generate_code()
        msg = EmailMessage()
        msg['Subject'] = 'Confirmation instruction'
        msg['To'] = email
        msg.set_content(f'confirmation code is: {code}')
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login('ahmasamer51@gmail.com', 'ofqhdqbtnihfuysm')
            smtp.send_message(msg)

        confirmation = EntryMessageWindow("Confirmation code", "Please enter the code you received via email:")
        code_confirmation_box = confirmation.code_confirmation
        if code_confirmation_box == code:
            # Insert the user's information into the database
            query = "INSERT INTO users (username,email, password) VALUES (%s, %s, %s)"
            cursor.execute(query, (username, email, hashed_password))
            conn.commit()

            show_custom_error("Sign Up Successful", "Sign-up successful!")
            register_page.destroy_signup_page()
            login2.loginpage()  # Automatically switch to the login page after successful signup
        else:
            show_custom_error("Incorrect Confirmation Code", "Invalid confirmation code")

    # Close the connection
    conn.close()

def generate_code():
    # Implement your own logic to generate a code
    # For example, you can use a library like "secrets" to generate a secure random code
    import secrets
    alphabet = "1234567890"
    code = ''.join(secrets.choice(alphabet) for _ in range(6))  # Generate a 6-character code
    return code