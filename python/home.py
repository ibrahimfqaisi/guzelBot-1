from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import messagebox
import os
import about
import login2
from face_register import App
import os.path
import tkinter as tk
import util
from  face_emotion import emotion
from PIL import Image, ImageTk
import random


class FirstPage():
    def __init__(self, dashboard_window):
        self.dashboard_window = dashboard_window

        # Load the background image
        background_image = Image.open("python\\new\\home.png")
        background_image2 = Image.open("python\\new\\welcome.png")
        background_image2= background_image2.resize((700,460))
        self.background_photo = ImageTk.PhotoImage(background_image)
        self.background_photo2 = ImageTk.PhotoImage(background_image2)        
        # Window Size and Placement
        dashboard_window.rowconfigure(0, weight=1)
        dashboard_window.columnconfigure(0, weight=1)
        screen_width = dashboard_window.winfo_screenwidth()
        screen_height = dashboard_window.winfo_height()
        app_width = 1340
        app_height = 690
        dashboard_window.title("Home")
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
        

        def faceId():
            dashboard_window.destroy()
            app = App()
            app.start() 
            page()
                #  pass  
        def Dashboard():
            dashboard_window.withdraw()
            file_path = 'userinfo.txt'
            os.remove(file_path)
            os.system("python python\\Dashboard.py")
            os.system("python python/chat.py")
            dashboard_window.destroy()

      

        home_bgImg = Image.open('python\\new\\home.png')
        home_bgImg = home_bgImg.resize((1300, 690))

        photo = ImageTk.PhotoImage(home_bgImg)
        home_bg = Label(homepage, image=photo, bg='#525561')
        home_bg.image = photo
        home_bg.place(x=-10, y=-10)

        
        
        home_bgImg1 = Image.open('python\\new\\homentn.png')
        home_bgImg1= home_bgImg1.resize((130, 46))
        photo2 = ImageTk.PhotoImage(home_bgImg1)
        home_bg1 = Label(homepage, image=photo2, bg='#272A37')
        home_bg1.image = photo2
      
        home_bgImg2 = Image.open('python\\new\\chatbtn.png')
        home_bgImg2= home_bgImg2.resize((130, 46))
        photo3 = ImageTk.PhotoImage(home_bgImg2)
        home_bg2 = Label(homepage, image=photo3, bg='#272A37')
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
            relief="flat",)
        home_button.place(x=140, y=90)
        def about():
            dashboard_window.withdraw()
            os.system("python python\\about.py")
            dashboard_window.destroy()
        def chat():
            dashboard_window.withdraw()
            os.system("python python\\chat.py")
            dashboard_window.destroy()
                    
        
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
        chat_button.place(x=300, y=90)


         # ========== face  BUTTON =======
        face_button = Button(homepage,image=photo4 , borderwidth=0,
            highlightthickness=0,
            cursor='hand2',
            relief="flat" ,
            command=faceId)
        face_button.place(x=765, y=90)
        
        # ========== about  BUTTON =======
        about_button = Button(
            homepage, 
            image=photo5,
            borderwidth=0,
            highlightthickness=0,
            cursor='hand2',
            relief="flat" ,         
            command=about)
        about_button.place(x=460, y=90)
        




            
        # ========== LOG OUT =======
        logout_button = Button(homepage,  image=photo6,
            borderwidth=0,
            highlightthickness=0,
            cursor='hand2',
            relief="flat" , command=Dashboard
)
        logout_button.place(x=1000, y=90)
        self.Welcome()
               # ========== Welcome message =======
    def Welcome(self):
        file_path1 = 'most_emotion.txt'
        if os.path.exists(file_path1):
            with open(file_path1, 'r') as file:
                emotion = file.read()

            file_path2 = 'userinfo.txt'
            # Read the contents of the file
            with open(file_path2, 'r') as file:
                str_userinfo = file.read()
                userinfo=str_userinfo.split(",")
                name=userinfo[1]

                if emotion == "Neutral" :
                    self.pop(f"Hi {name} ,\n You are capable of \namazing things. " )
                else :
                      self.pop(f"Hi {name},\n{message_emotion(emotion)}")

            os.remove(file_path1) 
    def chat2(self):
        self.register_new_user_window.destroy()
        self.dashboard_window.withdraw()

        os.system("python python\\chat.py")

        self.dashboard_window.destroy()
    def pop(self, text2):
        if hasattr(self, 'welcome') and self.register_new_user_window.winfo_exists():
            self.register_new_user_window.destroy()

        self.register_new_user_window = tk.Toplevel(self.dashboard_window)
        self.register_new_user_window.attributes('-topmost', True)
        self.register_new_user_window.geometry("600x400")
        self.register_new_user_window.title("welcome")
        self.center_window()

        self.background_label = tk.Label(self.register_new_user_window, image=self.background_photo2)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.accept_button_register_new_user_window = util.get_button(
            self.register_new_user_window, 'Chat', 'turquoise1', self.chat2
        )
        self.accept_button_register_new_user_window.place(x=170, y=300)


        self.try_again_button_register_new_user_window = util.get_button(
            self.register_new_user_window, 'Close', 'navy', self.try_again_register_new_user
        )
        self.try_again_button_register_new_user_window.place(x=330, y=300)

        # Calculate the position of the additional text label dynamically
        # label_width = 400
        # label_height = 200
        label_x = 25
        label_y = 160

        self.additional_text_label = tk.Label(self.register_new_user_window, text=text2,bg='#A28DCF')
        self.additional_text_label.config(font=("Arial", 16))
        self.additional_text_label.place(x=label_x, y=label_y)

        self.register_new_user_window.resizable("false", 'false')

    def center_window(self):
        self.register_new_user_window.update_idletasks()
        width = self.register_new_user_window.winfo_width()
        height = self.register_new_user_window.winfo_height()

        screen_width = self.register_new_user_window.winfo_screenwidth()
        screen_height = self.register_new_user_window.winfo_screenheight()

        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        self.register_new_user_window.geometry(f"{width}x{height}+{x}+{y}")
            # self.add_img_to_label(self.capture_label)
    def try_again_register_new_user(self):
        self.register_new_user_window.destroy()
def message_emotion(emotion):
    messages = {
        'Sad': [
            "This sadness is temporary, and brighter\n days are on the horizon.",
            "You are stronger than you know, and you \n have the power to overcome this sadness.",
            "Remember that you are surrounded by people\n who care about you and want to support you.",
            "This sadness is a temporary setback, and it \n will only make your eventual triumph even more satisfying.",
            "Every day is a new opportunity for positive \n experiences and personal growth.",
            "Believe in yourself and your ability to find \n happiness and fulfillment once again."
        ],
        'Angry': [
            "Take a deep breath and remind yourself that you have the\n power to choose how\ you respond to this anger.",
            "Use your anger as motivation to make a  difference and \nadvocate for positive solutions.",
            "Channel your anger into productive actions that promote \nunderstanding, justice, and positive outcomes.",
            "Remember that forgiveness and letting go of anger can bring \nyou peace and allow you to move forward.",
            "Surround yourself with positive influences and seek support \nfrom loved ones who can offer guidance and encouragement.",
            "Believe in your ability to rise above anger and transform it\n into compassion, resilience, and positive change."
        ],
        'Happy': [
            "Your happiness is contagious and radiates \n positive energy to those around you.",
            "Embrace and savor this moment of happiness,\n for it is a precious gift.",
            "Allow your happiness to inspire and uplift \nothers, spreading joy wherever you go.",
            "Let your happiness be a reminder to cherish\n and appreciate the beauty in everyday moments.",
            "Use this happiness as fuel to pursue your \n dreams and live a fulfilling, purposeful life.",
            "Remember that your happiness is a reflection\n of your own inner strength, resilience, and positivity."
        ]
    }

    if emotion in messages:
        random_message = random.choice(messages[emotion])
        return random_message
    
def page():
        window = Tk()
        window.title("Home")
        FirstPage(window)
        window.mainloop()

if __name__ == '__main__':
    page()
