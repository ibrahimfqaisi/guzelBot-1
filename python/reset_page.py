import tkinter as tk
import tkinter.simpledialog as simpledialog
from tkinter import Button, messagebox
import psycopg2
import hashlib
import smtplib
from email.message import EmailMessage

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
        code_confirmation = simpledialog.askstring("confirmation code ", "Please enter the code you received via email :")

        if code_confirmation == code :
              
             
            new_password = simpledialog.askstring("Password Reset", "Enter a new password:")
            if new_password:
                # Hash the new password
                hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
                update_password_in_system(email, new_password)

                # Update the user's password in the database
                update_query = "UPDATE users SET password = %s WHERE id = %s"
                cursor.execute(update_query, (hashed_password, user[0]))  # Assuming the user ID is stored in column index 0
                conn.commit()

                messagebox.showinfo("Password Reset", "Password successfully updated!")
                import login2  # Automatically switch to the login page after password reset
            else:
                messagebox.showerror("Password Reset Failed", "Invalid new password")
        else:
                messagebox.showerror("incorrect confirmation code", "Invalid confirmation code")
    else:
        messagebox.showerror("Password Reset Failed", "Invalid email or security answers")
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
