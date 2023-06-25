from tkinter import *
from PIL import ImageTk, Image
import os


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

        heading2 = Label(homepage, text='TEAM GUZEL BOT', bg='#272A37', fg='#ff6c38', font=("", 30, "bold"))
        heading2.place(x=250, y=195)


 

        def home():
            dashboard_window.withdraw()
            os.system("python Dashboard.py")
            dashboard_window.destroy()

        # ========== HOME BUTTON =======
        home_button = Button(homepage, text='Home', bg='#272A37', font=("", 20, "bold"), bd=0, fg='white',
                             cursor='hand2', activebackground='#fd6a36', activeforeground='white',command=home)
        home_button.place(x=150, y=100)
        def chat():
            dashboard_window.withdraw()
            os.system("python chat.py")
            dashboard_window.destroy()
        # ========== chat BUTTON =======
        chat_button = Button(homepage, text='chat', bg='#272A37', font=("", 20, "bold"), bd=0, fg='white',
                               cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a',command=chat
                               )
        chat_button.place(x=250, y=100)

        def about():
            dashboard_window.withdraw()
            os.system("python about.py")
            dashboard_window.destroy()

        # ========== about  BUTTON =======
        about_button = Button(homepage, text='About us', bg='#272A37', font=("", 20, "bold"), bd=0, fg='white',
                                cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a',
                                command=about)
        about_button.place(x=350, y=100)


        def logout():
            dashboard_window.withdraw()
        # ========== LOG OUT =======
        logout_button = Button(homepage, text='Logout', bg='#272A37', font=("", 20, "bold"), bd=0, fg='white',
                               cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a',command=logout)
        logout_button.place(x=500, y=100)

        # Image paths and names for the cards
        card_data = [
        {"name": "ibrhem", "links": "https://github.com/", "image": "team\ibra.jpg"},
        {"name": "bayan", "links": "https://github.com/", "image": "team\\bayan.jpg"},
        {"name": "mhmad", "links": "https://github.com/", "image": "team\mha.jpg"},
        {"name": "sajeda", "links": "https://github.com/", "image": "team\sajeda.jpg"},
        {"name": "aseel", "links": "https://github.com/", "image": "team\\aseel.jpg"},
        {"name": "firas", "links": "https://github.com/", "image": "team\\firas.jpg"}
        ]

        def display_cards():
            x = 100  # Initial x-coordinate for the cards

            for data in card_data:
                # Load the image
                image = Image.open(data['image'])
                # Resize the image if necessary
                image = image.resize((120, 150))
                # Create a PhotoImage from the image
                photo = ImageTk.PhotoImage(image)

                # Create the label to display the image
                image_label = Label(homepage, image=photo, bg='#525561')
                image_label.image = photo  # Store a reference to the image
                image_label.place(x=x, y=300)

                # Create the label to display the name
                name_label = Label(homepage, text=data['name'], bg='#272A37', fg='white', font=("", 12))
                name_label.place(x=x, y=470)


                name_label = Label(homepage, text=data['links'], bg='#272A37', fg='white', font=("", 12))
                name_label.place(x=x, y=500)

                x += 200  # Increment the x-coordinate for the next card

        display_cards()

def page():
    window = Tk()
    FirstPage(window)
    window.mainloop()

if __name__ == '__main__':
    page()
