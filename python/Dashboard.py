from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import messagebox
import os
import about
import login2

'''
Sajeda
Firas
'''



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
        

        # window Icon
        icon = PhotoImage(file='python\\images3\\1.png')
        dashboard_window.iconphoto(True, icon)
        dashboard_window.title('Welcome')

        

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
        



      

        home_bgImg = Image.open('python\\assets\\image_1.png')
        home_bgImg = home_bgImg.resize((1340, 690))

        photo = ImageTk.PhotoImage(home_bgImg)
        home_bg = Label(homepage, image=photo, bg='#525561')
        home_bg.image = photo
        home_bg.place(x=-10, y=-10)

        home_bgImg1 = Image.open('python\\images3\\1.png')
        home_bgImg1 = home_bgImg1.resize((500, 500))
        photo2 = ImageTk.PhotoImage(home_bgImg1)
        home_bg1 = Label(homepage, image=photo2, bg='#272A37')
        home_bg1.image = photo2
        home_bg1.place(x=200, y=240)
      
       

        heading2 = Label(homepage, text='GUZL DASHBOARD', bg='#272A37', fg='#ff6c38', font=("", 30, "bold"))
        heading2.place(x=250, y=195)



        
         
       
        
       

        # ========== HOME BUTTON =======
        home_button = Button(homepage, text='Home', bg='#272A37', font=("", 20, "bold"), bd=0, fg='white',
                             cursor='hand2', activebackground='#fd6a36', activeforeground='white')
        home_button.place(x=150, y=100)

        def about():
            pass

        def chat():
            pass

        # ========== chat BUTTON =======
        chat_button = Button(homepage, text='chat', bg='#272A37', font=("", 20, "bold"), bd=0, fg='white',
                               cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a',command=chat
                               )
        chat_button.place(x=250, y=100)

        # ========== about  BUTTON =======
        about_button = Button(homepage, text='About us', bg='#272A37', font=("", 20, "bold"), bd=0, fg='white',
                                cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a',
                                command=about)
        about_button.place(x=350, y=100)

       

        def login():
            dashboard_window.withdraw()
            os.system("python python\\login2.py")
            dashboard_window.destroy()
            
        # ========== LOG OUT =======
        logout_button = Button(homepage, text='Login', bg='#272A37', font=("", 20, "bold"), bd=0, fg='white',
                               cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a',command=login)
        logout_button.place(x=500, y=100)


def page():
    window = Tk()
    FirstPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()
