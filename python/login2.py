from tkinter import *
import register_page
import os 
from PIL import ImageTk, Image
import tkinter as tk
import tkinter.simpledialog as simpledialog
from tkinter import Button, messagebox
import psycopg2
import hashlib
import reset_page

def login():
    # Implement the login functionality here
    email = Login_emailName_entry.get()
    password = Login_passwordName_entry.get()

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
        if entered_password_hash == user[4]:  # Assuming the password hash is stored in column index 4
            
            destroy_login()
            os.system("python python\\chat.py")
            
        else:
            messagebox.showerror("Login Failed", "Invalid Password")
    else:
        messagebox.showerror("Login Failed", "Invalid Email")

    # Close the connection
    conn.close()

window = None

def destroy_login():
    global window
    window.destroy()

def loginpage ():
    global window
    window = Tk()

    height = 690
    width = 1340
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 4) - (height // 4)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    window.configure(bg="#525561")
    

    # ================Background Image ====================
     
    home_bgImg = Image.open('python\\assets\\image_1.png')
    home_bgImg = home_bgImg.resize((1340, 690))

    photo = ImageTk.PhotoImage(home_bgImg)
    bg_imageLogin = Label( image=photo, bg='#525561')
    bg_imageLogin.image = photo
    bg_imageLogin.place(x=0, y=0)

   
    Login_headerText1 = Label(
        bg_imageLogin,
        text="GUZEL BOT",
        fg="#ff6c38",
        font=("yu gothic ui bold", 30 ),
        bg="#272A37"
    )
    Login_headerText1.place(x=110, y=45)



    # ================ LOGIN TO ACCOUNT HEADER ====================
    loginAccount_header = Label(
        bg_imageLogin,
        text="Login to continue",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 28 * -1),
        bg="#272A37"
    )
    loginAccount_header.place(x=75, y=121)

    # ================ NOT A MEMBER TEXT ====================
    loginText = Label(
        bg_imageLogin,
        text="Not a member?",
        fg="#FFFFFF",
        font=("yu gothic ui Regular", 15 * -1),
        bg="#272A37"
    )
    loginText.place(x=75, y=187)

    # ================ GO TO SIGN UP ====================
    switchSignup = Button(
        bg_imageLogin,
        text="Sign Up",
        fg="#ff6c38",
        font=("yu gothic ui Bold", 15 * -1),
        bg="#272A37",
        bd=0,
        cursor="hand2",
        activebackground="#272A37",
        activeforeground="#ffffff",
        command=lambda  : [destroy_login(),register_page.regestier()]

    )
    switchSignup.place(x=220, y=185, width=70, height=35)


    # ================ Email Name Section ====================
    Login_emailName_image = PhotoImage(file="python\\assets\\email.png")
    Login_emailName_image_Label = Label(
        bg_imageLogin,
        image=Login_emailName_image,
        bg="#272A37"
    )
    Login_emailName_image_Label.place(x=76, y=242)

    Login_emailName_text = Label(
        Login_emailName_image_Label,
        text="Email account",
        fg="#FFFFFF",
        font=("yu gothic ui SemiBold", 13 * -1),
        bg="#3D404B"
    )
    Login_emailName_text.place(x=25, y=0)

    Login_emailName_icon = PhotoImage(file="python\\assets\\email-icon.png")
    Login_emailName_icon_Label = Label(
        Login_emailName_image_Label,
        image=Login_emailName_icon,
        bg="#3D404B"
    )
    Login_emailName_icon_Label.place(x=370, y=15)
    global Login_emailName_entry
    Login_emailName_entry = Entry(
        Login_emailName_image_Label,
        bd=0,
        bg="#3D404B",
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 16 * -1),
    )
    Login_emailName_entry.place(x=8, y=17, width=354, height=27)


    # ================ Password Name Section ====================
    Login_passwordName_image = PhotoImage(file="python\\assets\\email.png")
    Login_passwordName_image_Label = Label(
        bg_imageLogin,
        image=Login_passwordName_image,
        bg="#272A37"
    )
    Login_passwordName_image_Label.place(x=80, y=330)

    Login_passwordName_text = Label(
        Login_passwordName_image_Label,
        text="Password",
        fg="#FFFFFF",
        font=("yu gothic ui SemiBold", 13 * -1),
        bg="#3D404B"
    )
    Login_passwordName_text.place(x=25, y=0)

    Login_passwordName_icon = PhotoImage(file="python\\assets\\pass-icon.png")
    Login_passwordName_icon_Label = Label(
        Login_passwordName_image_Label,
        image=Login_passwordName_icon,
        bg="#3D404B"
    )
    Login_passwordName_icon_Label.place(x=370, y=15)
    global Login_passwordName_entry
    Login_passwordName_entry = Entry(
        Login_passwordName_image_Label,
        bd=0,
        bg="#3D404B",
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 16 * -1),
    )
    Login_passwordName_entry.place(x=8, y=17, width=354, height=27)


    # def login():
    #         login.withdraw()
    #         os.system("python Dashboard.py")
    #         login.destroy()
    # =============== Submit Button ====================
    Login_button_image_1 = PhotoImage(
        file="python\\assets\\button_1.png")
    Login_button_1 = Button(
        bg_imageLogin,
        image=Login_button_image_1,
        borderwidth=0,
        highlightthickness=0,
        # command=lambda:login,
        relief="flat",
        activebackground="#272A37",
        cursor="hand2",
        bg='#272A37',
        command=lambda:login()
    )
    
    Login_button_1.place(x=200, y=470, width=150, height=50)

   
    forgotPassword = Button(
        bg_imageLogin,
        text="Forgot Password",
        fg="#ff6c38",
        font=("yu gothic ui Bold", 15 * -1),
        bg="#272A37",
        bd=0,
        activebackground="#272A37",
        activeforeground="#ffffff",
        cursor="hand2",
        command=lambda: forgot_password(),
    )
    forgotPassword.place(x=210, y=400, width=150, height=35)


    def forgot_password():

        win = Toplevel()
        window_width = 350
        window_height = 350
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        position_top = int(screen_height / 4 - window_height / 4)
        position_right = int(screen_width / 2 - window_width / 2)
        win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

        win.title('Forgot Password')
        # win.iconbitmap('images\\aa.ico')
        win.configure(background='#272A37')
        win.resizable(False, False)

        # ====== Email ====================
        email_entry3 = Entry(win, bg="#3D404B", font=("yu gothic ui semibold", 12), highlightthickness=1,
                            bd=0)
        email_entry3.place(x=40, y=80, width=256, height=50)
        email_entry3.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
        email_label3 = Label(win, text='• Email', fg="#FFFFFF", bg='#272A37',
                            font=("yu gothic ui", 11, 'bold'))
        email_label3.place(x=40, y=50)

        # ====  New Password ==================
        new_password_entry = Entry(win, bg="#3D404B", font=("yu gothic ui semibold", 12), show='•', highlightthickness=1,
                                bd=0)
        new_password_entry.place(x=40, y=180, width=256, height=50)
        new_password_entry.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
        new_password_label = Label(win, text='• New Password', fg="#FFFFFF", bg='#272A37',
                                font=("yu gothic ui", 11, 'bold'))
        new_password_label.place(x=40, y=150)

        # ======= Update password Button ============
        update_pass = Button(win, fg='#f8f8f8', text='Update Password', bg='#ff6c38', font=("yu gothic ui", 12, "bold"),
                            cursor='hand2', relief="flat", bd=0, highlightthickness=0, activebackground="#1D90F5",
                            command=lambda:reset_page.reset_password(email_entry3))
        update_pass.place(x=40, y=260, width=256, height=45)


    window.resizable(False, False)


    window.mainloop()
    

if __name__ == '__main__':
    loginpage()