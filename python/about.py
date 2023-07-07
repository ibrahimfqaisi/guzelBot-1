from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import messagebox
import os
from face_register import App
import about
import login2



class FirstPage:
    def __init__(self, dashboard_window):
        self.dashboard_window = dashboard_window

        # Window Size and Placement
        dashboard_window.rowconfigure(0, weight=1)
        dashboard_window.columnconfigure(0, weight=1)
        screen_width = dashboard_window.winfo_screenwidth()
        screen_height = dashboard_window.winfo_height()
        app_width = 1340
        app_height = 690
        x = (screen_width/2)-(app_width/2)
        y = (screen_height/160)-(app_height/160)
        dashboard_window.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        dashboard_window.title('About us')



        # Navigating through windows
        homepage = Frame(dashboard_window)
        dashboard_page = Frame(dashboard_window)

        for frame in (homepage, dashboard_page):
            frame.grid(row=0, column=0, sticky='nsew')

        def show_frame(frame):
            frame.tkraise()

        show_frame(homepage)

        # ======================================================================================
        # =================== HOME PAGE ========================================================
        # ======================================================================================
        homepage.config(background='#525561')

        home_bgImg = Image.open('python\\new\\aboutbg.png')
        home_bgImg = home_bgImg.resize((1300, 690))

        photo = ImageTk.PhotoImage(home_bgImg)
        home_bg = Label(homepage, image=photo, )
        home_bg.image = photo
        home_bg.place(x=-10, y=-10)

        # ====== MENU BAR ==========


        def faceId():
            dashboard_window.destroy()
            app = App()
            app.start() 
            page()
                
        def delet_info():
            dashboard_window.withdraw()
            file_path = 'userinfo.txt'
            os.remove(file_path)
            os.system("python python\\Dashboard.py")
            os.system("python python/chat.py")
            dashboard_window.destroy()

        def Dashboard():
            dashboard_window.withdraw()
            file_path = 'userinfo.txt'
            os.remove(file_path)
            os.system("python python\\Dashboard.py")
            dashboard_window.destroy()

        def delet_info():
            dashboard_window.withdraw()
            file_path = 'userinfo.txt'
            os.remove(file_path)
            os.system("python python\\Dashboard.py")
            os.system("python python/chat.py")
            dashboard_window.destroy()

        def about():
            dashboard_window.withdraw()
            os.system("python python\\about.py")
            dashboard_window.destroy()
        def chat():
            dashboard_window.withdraw()
            os.system("python python\\chat.py")
            dashboard_window.destroy()

        def home():
            dashboard_window.withdraw()
            os.system("python python\\home.py")
            dashboard_window.destroy()


        home_bgImg1 = Image.open('python\\new\\homentn.png')
        home_bgImg1= home_bgImg1.resize((130, 46))
        photo2 = ImageTk.PhotoImage(home_bgImg1)
        home_bg1 = Label(homepage, image=photo2, )
        home_bg1.image = photo2

        home_bgImg2 = Image.open('python\\new\\chatbtn.png')
        home_bgImg2= home_bgImg2.resize((130, 46))
        photo3 = ImageTk.PhotoImage(home_bgImg2)
        home_bg2 = Label(homepage, image=photo3, )
        home_bg2.image = photo3


        home_bgImg3 = Image.open('python\\new\\facid.png')
        home_bgImg2= home_bgImg2.resize((90,37))
        photo4 = ImageTk.PhotoImage(home_bgImg3)
        home_bg3 = Label(homepage, image=photo4, )
        home_bg3.image = photo4

        home_bgImg4 = Image.open('python\\new\\aboutbtn.png')
        home_bgImg2= home_bgImg2.resize((90,37))
        photo5 = ImageTk.PhotoImage(home_bgImg4)
        home_bg4 = Label(homepage, image=photo5, )
        home_bg4.image = photo5

        home_bgImg5 = Image.open('python\\new\\logout.png')
        home_bgImg2= home_bgImg2.resize((90, 37))
        photo6 = ImageTk.PhotoImage(home_bgImg5)
        home_bg5 = Label(homepage, image=photo6, )
        home_bg5.image = photo6



        # ========== HOME BUTTON =======
        home_button = Button(
            homepage, 
            image=photo2, 
            borderwidth=0,
            highlightthickness=0,
            cursor='hand2',
            relief="flat",
            command=home)
        home_button.place(x=140, y=50)


        # ========== chat BUTTON =======
        chat_button = Button(
            homepage, 
            image=photo3,
            borderwidth=0,
            highlightthickness=0,
            cursor='hand2',
            relief="flat" ,
            command=chat
                    )
        chat_button.place(x=300, y=50)



         # ========== face  BUTTON =======
        face_button = Button(homepage,image=photo4 , borderwidth=0,
            highlightthickness=0,
            cursor='hand2',
            relief="flat" ,command=faceId)
        face_button.place(x=765, y=50)

        # ========== about  BUTTON =======
        about_button = Button(
            homepage, 
            image=photo5,
            borderwidth=0,
            highlightthickness=0,
            cursor='hand2',
            relief="flat" )
        about_button.place(x=460, y=50)

        # ========== LOG OUT =======
        logout_button = Button(homepage,  image=photo6,
            borderwidth=0,
            highlightthickness=0,
            cursor='hand2',
            relief="flat" , command=delet_info)
        logout_button.place(x=1000, y=50)

def page():
    window = Tk()
    FirstPage(window)
    window.mainloop()

if __name__ == '__main__':
    page()