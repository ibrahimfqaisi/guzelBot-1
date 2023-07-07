from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import messagebox
import os
import about
import login2
from face_logIn import App

# '''
# Sajeda
# Firas
# '''



class FirstPage:
    def __init__(self, dashboard_window):
        self.dashboard_window = dashboard_window

        # Window Size and Placement
        dashboard_window.state('zoomed')
        dashboard_window.rowconfigure(0, weight=1)
        dashboard_window.columnconfigure(0, weight=1)
        screen_width = dashboard_window.winfo_screenwidth()
        screen_height = dashboard_window.winfo_height()
        app_width = 1340
        app_height = 690
        self.dashboard_window.title("Guzel Bot")
        x = (screen_width/2)-(app_width/2)
        y = (screen_height/160)-(app_height/160)
        dashboard_window.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        

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

        # ====== MENU BAR ==========
        
        home_bgImg = Image.open('python\\new\\dash.png')
        home_bgImg = home_bgImg.resize((1340, 690))

        photo = ImageTk.PhotoImage(home_bgImg)
        home_bg = Label(homepage, image=photo, bg='#525561')
        home_bg.image = photo
        home_bg.place(x=-10, y=-10)

        home_bgImg1 = Image.open('python\\new\\log2.png')
        home_bgImg1= home_bgImg1.resize((160, 55))

        photo2 = ImageTk.PhotoImage(home_bgImg1)
        home_bg1 = Label(homepage, image=photo2, )
        home_bg1.image = photo2
        
      
       
        home_bgImg2 = Image.open('python\\new\\face.png')
        home_bgImg2= home_bgImg2.resize((160, 55))

        photo3 = ImageTk.PhotoImage(home_bgImg2)
        home_bg2 = Label(homepage, image=photo3, )
        home_bg2.image = photo3


        
        def login():
            dashboard_window.withdraw()
            os.system("python python\\login2.py")
        
        logoin_button = Button(
            homepage,
            image=photo2, 
            borderwidth=0,
            highlightthickness=0,
            cursor='hand2',
            relief="flat",
            command=login
            
            )
        logoin_button.place(x=110, y=490,) 
        def face():
            
            dashboard_window.destroy()
            app = App()
            app.start()
            
            file_path = 'userinfo.txt'
            try:
                with open(file_path, 'r') as file:
                    str_userinfo = file.read()
                os.system("python python\\home.py")
                
            except:
                messagebox.showinfo("sign in using email", "face didn't find")
                file_path1 = 'most_emotion.txt'
                if os.path.exists(file_path1):
                    os.remove(file_path1)                 
                page()


        face_button = Button(
            homepage,
            image=photo3, 
            borderwidth=0,
            highlightthickness=0,
            cursor='hand2',
            relief="flat",
            command=face
    
            )
        face_button.place(x=310, y=490,)
    

        

      


def page():
    window = Tk()
    window.title("Guzel Bot")
    FirstPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()
