from tkinter import *
import login2
from PIL import ImageTk, Image


window = None
def destroy_signup_page():
     global window
     window.destroy()


def regestier():
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
    home_bg = Label( image=photo, bg='#525561')
    home_bg.image = photo
    home_bg.place(x=0, y=0)


   

    headerText1 = Label(
        home_bg,
        text="GUZEL BOT",
        fg="#ff6c38",
        font=("yu gothic ui bold", 30 ),
        bg="#272A37"
    )
    headerText1.place(x=110, y=45)



    # ================ CREATE ACCOUNT HEADER ====================
    createAccount_header = Label(
        home_bg,
        text="Create new account",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 28 * -1),
        bg="#272A37"
    )
    createAccount_header.place(x=75, y=121)

    # ================ ALREADY HAVE AN ACCOUNT TEXT ====================
    text = Label(
        home_bg,
        text="Already a member?",
        fg="#FFFFFF",
        font=("yu gothic ui Regular", 15 * -1),
        bg="#272A37"
    )
    text.place(x=75, y=187)

    # ================ GO TO LOGIN ====================
    switchLogin = Button(
        home_bg,
        text="Login",
        fg="#ff6c38",
        font=("yu gothic ui Bold", 15 * -1),
        bg="#272A37",
        bd=0,
        cursor="hand2",
        activebackground="#272A37",
        activeforeground="#ffffff",
        
        command=lambda  : [destroy_signup_page(),login2.loginpage()]

        
        
        
    )
    
    switchLogin.place(x=230, y=185, width=50, height=35)

    # ================ First Name Section ====================
    firstName_image = PhotoImage(file="python\\assets\\input_img.png")
    firstName_image_Label = Label(
        home_bg,
        image=firstName_image,
        bg="#272A37"
    )
    firstName_image_Label.place(x=80, y=242)

    firstName_text = Label(
        firstName_image_Label,
        text="First name",
        fg="#FFFFFF",
        font=("yu gothic ui SemiBold", 13 * -1),
        bg="#3D404B"
    )
    firstName_text.place(x=25, y=0)

    firstName_icon = PhotoImage(file="python\\assets\\name_icon.png")
    firstName_icon_Label = Label(
        firstName_image_Label,
        image=firstName_icon,
        bg="#3D404B"
    )
    firstName_icon_Label.place(x=159, y=15)

    firstName_entry = Entry(
        firstName_image_Label,
        bd=0,
        bg="#3D404B",
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 16 * -1),
    )
    firstName_entry.place(x=8, y=17, width=140, height=27)


    # ================ Last Name Section ====================
    lastName_image = PhotoImage(file="python\\assets\\input_img.png")
    lastName_image_Label = Label(
        home_bg,
        image=lastName_image,
        bg="#272A37"
    )
    lastName_image_Label.place(x=293, y=242)

    lastName_text = Label(
        lastName_image_Label,
        text="Last name",
        fg="#FFFFFF",
        font=("yu gothic ui SemiBold", 13 * -1),
        bg="#3D404B"
    )
    lastName_text.place(x=25, y=0)

    lastName_icon = PhotoImage(file="python\\assets\\name_icon.png")
    lastName_icon_Label = Label(
        lastName_image_Label,
        image=lastName_icon,
        bg="#3D404B"
    )
    lastName_icon_Label.place(x=159, y=15)

    lastName_entry = Entry(
        lastName_image_Label,
        bd=0,
        bg="#3D404B",
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 16 * -1),
    )
    lastName_entry.place(x=8, y=17, width=140, height=27)

    # ================ Email Name Section ====================
    emailName_image = PhotoImage(file="python\\assets\\email.png")
    emailName_image_Label = Label(
        home_bg,
        image=emailName_image,
        bg="#272A37"
    )
    emailName_image_Label.place(x=80, y=311)

    emailName_text = Label(
        emailName_image_Label,
        text="Email account",
        fg="#FFFFFF",
        font=("yu gothic ui SemiBold", 13 * -1),
        bg="#3D404B"
    )
    emailName_text.place(x=25, y=0)

    emailName_icon = PhotoImage(file="python\\assets\\email-icon.png")
    emailName_icon_Label = Label(
        emailName_image_Label,
        image=emailName_icon,
        bg="#3D404B"
    )
    emailName_icon_Label.place(x=370, y=15)

    emailName_entry = Entry(
        emailName_image_Label,
        bd=0,
        bg="#3D404B",
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 16 * -1),
    )
    emailName_entry.place(x=8, y=17, width=354, height=27)


    # ================ Password Name Section ====================
    passwordName_image = PhotoImage(file="python\\assets\\input_img.png")
    passwordName_image_Label = Label(
        home_bg,
        image=passwordName_image,
        bg="#272A37"
    )
    passwordName_image_Label.place(x=80, y=380)

    passwordName_text = Label(
        passwordName_image_Label,
        text="Password",
        fg="#FFFFFF",
        font=("yu gothic ui SemiBold", 13 * -1),
        bg="#3D404B"
    )
    passwordName_text.place(x=25, y=0)

    passwordName_icon = PhotoImage(file="python\\assets\\pass-icon.png")
    passwordName_icon_Label = Label(
        passwordName_image_Label,
        image=passwordName_icon,
        bg="#3D404B"
    )
    passwordName_icon_Label.place(x=159, y=15)

    passwordName_entry = Entry(
        passwordName_image_Label,
        bd=0,
        bg="#3D404B",
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 16 * -1),
    )
    passwordName_entry.place(x=8, y=17, width=140, height=27)


    # ================ Confirm Password Name Section ====================
    confirm_passwordName_image = PhotoImage(file="python\\assets\\input_img.png")
    confirm_passwordName_image_Label = Label(
        home_bg,
        image=confirm_passwordName_image,
        bg="#272A37"
    )
    confirm_passwordName_image_Label.place(x=293, y=380)

    confirm_passwordName_text = Label(
        confirm_passwordName_image_Label,
        text="Confirm Password",
        fg="#FFFFFF",
        font=("yu gothic ui SemiBold", 13 * -1),
        bg="#3D404B"
    )
    confirm_passwordName_text.place(x=25, y=0)

    confirm_passwordName_icon = PhotoImage(file="python\\assets\\pass-icon.png")
    confirm_passwordName_icon_Label = Label(
        confirm_passwordName_image_Label,
        image=confirm_passwordName_icon,
        bg="#3D404B"
    )
    confirm_passwordName_icon_Label.place(x=159, y=15)

    confirm_passwordName_entry = Entry(
        confirm_passwordName_image_Label,
        bd=0,
        bg="#3D404B",
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 16 * -1),
    )
    confirm_passwordName_entry.place(x=8, y=17, width=140, height=27)

    # =============== Submit Button ====================
    submit_buttonImage = PhotoImage(
        file="python\\assets\\button_1.png")
    submit_button = Button(
        home_bg,
        image=submit_buttonImage,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#272A37",
        cursor="hand2",
        bg='#272A37'
    )
    submit_button .place(x=200, y=470, width=150, height=50)

   


    window.resizable(False, False)
    window.mainloop()

   
if __name__ == '__main__':
    regestier()