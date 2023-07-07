import tkinter as tk
from tkinter import *
import tkinter.simpledialog as simpledialog
from tkinter import Button, messagebox, Label, Toplevel
import psycopg2
import hashlib
import smtplib
from email.message import EmailMessage

'''
Ibrahim
Bayan 
Aseel
'''


def show_custom_error(title, message):
    win = Toplevel()
    window_width = 350
    window_height = 150
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    win.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
    win.title(title)
    win.configure(background="#272A37")
    win.resizable(False, False)

    label = Label(win, text=message, fg="white", bg="#272A37")
    label.pack(pady=20)

    ok_button = Button(win, text="OK", command=win.destroy)
    ok_button.pack(pady=10)

class EntryMessageWindow:
    def __init__(self, title, message):
        self.email_value = None

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

        self.email_entry = Entry(self.win, bg="#3D404B", font=("yu gothic ui semibold", 12), highlightthickness=1, bd=0)
        self.email_entry.place(x=40, y=80, width=256, height=50)
        self.email_entry.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
        email_label = Label(self.win, text=message, fg="#FFFFFF", bg='#272A37', font=("yu gothic ui", 11, 'bold'))
        email_label.place(x=40, y=50)

        update_pass = Button(self.win, fg='#f8f8f8', text='submit', bg='#ff6c38', font=("yu gothic ui", 12, "bold"),
                             cursor='hand2', relief="flat", bd=0, highlightthickness=0, activebackground="#1D90F5",
                             command=self.get_email)
        update_pass.place(x=40, y=260, width=256, height=45)

        self.win.protocol("WM_DELETE_WINDOW", self.on_close)

        self.win.wait_window()

    def get_email(self):
        self.email_value = self.email_entry.get()
        self.win.destroy()

    def on_close(self):
        self.win.destroy()







def reset_password(reset_email_entry):
    email = reset_email_entry.get()
    
    # Connect to the PostgreSQL database
    conn = psycopg2.connect("postgres://vfpgukpn:w4ArNUg7hh4GJkEt9Y6RK3jxzP_-ratk@ruby.db.elephantsql.com/vfpgukpn")
    cursor = conn.cursor()

    # Check if the email and security answers match in the database
    query = "SELECT * FROM users WHERE email = %s "
    cursor.execute(query, (email,))
    user = cursor.fetchone()

    if user:
        root = tk.Tk()
        root.withdraw()
        # Prompt the user to enter a new password
        code =generate_code()
        msg = EmailMessage()
        msg['Subject'] = 'Password Reset'
        # msg['From'] = 'guzel.ltuc@gmail.com'
        msg['To'] = email
        msg.set_content(f'confirmation code is: {code}')
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login('ahmasamer51@gmail.com', 'ofqhdqbtnihfuysm')
            smtp.send_message(msg)
            # Clear the email field after sending the email
            reset_email_entry.delete(0, tk.END)  
            
        entry_window = EntryMessageWindow("confirmation", "Please enter the code you received via email :")
        email_val = entry_window.email_value 

        code_confirmation = email_val

        if code_confirmation == code :
            entry_window = EntryMessageWindow("Password Reset", "Enter a new password:")
            email_val = entry_window.email_value 
            new_password=email_val
        
            # new_password = simpledialog.askstring("Password Reset", "Enter a new password:")
            if new_password:
                # Hash the new password
                hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
                update_password_in_system(email, new_password)

                # Update the user's password in the database
                update_query = "UPDATE users SET password = %s WHERE id = %s"
                cursor.execute(update_query, (hashed_password, user[0]))  # Assuming the user ID is stored in column index 0
                conn.commit()

                invalid_password_message =  "Password successfully updated!"
                show_custom_error("Login Failed", invalid_password_message)
                root.destroy()
                import login2  # Automatically switch to the login page after password reset
            else:
          
                invalid_password_message =  "Invalid new password"
                show_custom_error("Login Failed", invalid_password_message)
                
        else:
               
                invalid_password_message =  "Invalid confirmation code"
                show_custom_error("Login Failed", invalid_password_message)
    else:
      
        invalid_password_message =  "Invalid email or security answers"
        show_custom_error("Login Failed", invalid_password_message)
    # Close the connection
    conn.close()

def update_password_in_system(email, new_password):
    # Implement your own logic to update the password in your system
    # For example, you can update the password in a database or a file
    # Replace this with your own code to update the password
    print(f"Updating bayann sey hi*******  password for {email} to: {new_password}")

def generate_code():
    # Implement your own logic to generate a code
    # For example, you can use a library like "secrets" to generate a secure random code
    import secrets
    alphabet = "1234567890"
    code = ''.join(secrets.choice(alphabet) for _ in range(6))  # Generate an 6-character code
    return code