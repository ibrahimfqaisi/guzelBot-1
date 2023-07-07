from tkinter import *
import login2
from PIL import ImageTk, Image
from signup_page import signup

'''
Sajeda
Ibrahim
Bayan 
Aseel
'''

window = None
def destroy_signup_page():
     global window
     window.destroy()


def regestier():
    global window
    window = Tk()
    window.title('sign up ')
    height = 690
    width = 1340
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 4) - (height // 4)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    window.configure(bg="#525561")
    
    # ================Background Image ====================
    home_bgImg = Image.open('python\\new\\sigubbg.png')
    home_bgImg = home_bgImg.resize((1340, 690))

    photo = ImageTk.PhotoImage(home_bgImg)
    home_bg = Label( image=photo, bg='#525561')
    home_bg.image = photo
    home_bg.place(x=0, y=0)


   


    

    # ================ GO TO LOGIN ====================
    login_img=PhotoImage(file="python\\new\\lll.png")
    switchLogin = Button(
        home_bg,
        image=login_img,
        text="Login",
        fg="#ff6c38",
        font=("yu gothic ui Bold", 15 ),
        bg='#A28DCF',
        bd=0,
        cursor="hand2",
        activeforeground="#ffffff",
        
        command=lambda  : [destroy_signup_page(),login2.loginpage()]

        
        
        
    )
    
    switchLogin.place(x=530, y=50 )

    # ================ First Name Section ====================
    # firstName_image = PhotoImage(file="python\\assets\\lable1.png")
    # firstName_image_Label = Label(
    #     home_bg,
    #     # image=firstName_image,
    #     bg="black"
    # )
    # firstName_image_Label.place(x=30, y=260,)


    firstName_entry = Entry(
        # firstName_image_Label,
        bd=0,
       bg='#A28DCF',
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 15),
    )
    firstName_entry.place(x=110, y=200, width=150, height=60 )


    # ================ Last Name Section ====================
    # lastName_image = PhotoImage(file="python\\assets\\lable1.png")
    # lastName_image_Label = Label(
    #     home_bg,
    #     # image=lastName_image,
    #     bg="black"
    # )
    # lastName_image_Label.place(x=225, y=260)

    lastName_entry = Entry(
        # lastName_image_Label,
        bd=0,
        bg='#A28DCF',
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 15),
    )
    lastName_entry.place(x=400, y=205, width=150, height=40)
    # ================ Email Name Section ====================
    # emailName_image = PhotoImage(file="python\\assets\\lable2.png")
    # emailName_image_Label = Label(
    #     home_bg,
    #     # image=emailName_image,
    #     borderwidth=0,
    #     bg="#272A37"
    # )
    # emailName_image_Label.place(x=50, y=390)


   

    emailName_entry = Entry(
        # emailName_image_Label,
        bd=0,
        bg="#A28DCF",
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 15),
    )
    emailName_entry.place(x=120, y=340, width=400, height=40)

    # ================ Password Name Section ====================
    # passwordName_image = PhotoImage(file="python\\assets\\lable1.png")
    # passwordName_image_Label = Label(
    #     home_bg,
    #     borderwidth=0,
    #     # image=passwordName_image,
    #     bg="black"
    # )
    # passwordName_image_Label.place(x=30, y=490)
 

    passwordName_entry = Entry(
        # passwordName_image_Label,
        bd=0,
         bg="#A28DCF",
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 15),
        show="*"
    )
    passwordName_entry.place(x=120, y=470, width=400, height=40)



    # # ================ Confirm Password Name Section ====================
    # confirm_passwordName_image = PhotoImage(file="python\\assets\\lable1.png")
    # confirm_passwordName_image_Label = Label(
    #     home_bg,
    #     borderwidth=0,
    #     # image=confirm_passwordName_image,
    #     bg="#272A37"
    # )
    # confirm_passwordName_image_Label.place(x=240, y=490)





    # confirm_passwordName_entry = Entry(
    #     # confirm_passwordName_image_Label,
    #     bd=0,
    #     bg="#245c62",
    #     highlightthickness=0,
    #     font=("yu gothic ui SemiBold", 16 * -1),
    # )
    # confirm_passwordName_entry.place(x=260, y=500, width=120, height=27)
    # =============== Submit Button ====================
    submit_buttonImage = PhotoImage(
        file="python\\new\\butt.png")
    submit_button = Button(
        home_bg,
        image=submit_buttonImage,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        cursor="hand2",
        bg='black',
        command=lambda:signup(firstName_entry,lastName_entry,emailName_entry,passwordName_entry)
    )
    submit_button .place(x=290, y=545)
   


    window.resizable(False, False)
    window.mainloop()

   
if __name__ == '__main__':
    regestier()