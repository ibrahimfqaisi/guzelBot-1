import tkinter as tk
import tkinter.simpledialog as simpledialog
from tkinter import Button, messagebox
import psycopg2
import hashlib
import smtplib
from email.message import EmailMessage

def signup():
    username = signup_username_entry.get()
    gender = signup_gender_entry.get()
    email = signup_email_entry.get()
    password = signup_password_entry.get()
    
    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Connect to the PostgreSQL database
    conn = psycopg2.connect("postgres://vfpgukpn:w4ArNUg7hh4GJkEt9Y6RK3jxzP_-ratk@ruby.db.elephantsql.com/vfpgukpn")
    cursor = conn.cursor()

    # Check if the email already exists in the database
    query = "SELECT * FROM users WHERE email = %s"
    cursor.execute(query, (email,))
    existing_user = cursor.fetchone()

    if existing_user:
        messagebox.showerror("Sign Up Failed", "Email already exists in the database")
    else:
        code =generate_code()
        msg = EmailMessage()
        msg['Subject'] = 'Confirmation instruction'
        # msg['From'] = 'guzel.ltuc@gmail.com'
        msg['To'] = email
        msg.set_content(f'confirmation code is: {code}')
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login('ahmasamer51@gmail.com', 'ofqhdqbtnihfuysm')
            smtp.send_message(msg)
            # Clear the email field after sending the email
            reset_email_entry.delete(0, tk.END)

            # Display a success message
            status_label.config(text='code sent successfully!')            
        code_confirmation = simpledialog.askstring("confirmation code ", "Please enter the code you received via email :")

        if code_confirmation == code :
           
        
        # Insert the user's information into the database
            query = "INSERT INTO users (username, gender, email, password) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (username, gender, email, hashed_password))
            conn.commit()

            messagebox.showinfo("Sign Up Successful", "Sign-up successful!")
            show_login_page()  # Automatically switch to the login page after successful signup
        else:
             messagebox.showerror("incorrect confirmation code", "Invalid confirmation code")
    # Close the connection
    conn.close()