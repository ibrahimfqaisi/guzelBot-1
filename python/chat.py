import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import Tk, Button
from PIL import Image, ImageTk
from face_register import App
import os
from chatbot import chatbot1
# import run
from run import voice_text_qu, text_ans , say_ans
import psycopg2
import os
from dotenv import load_dotenv
from tkinter import Tk, Button, Listbox, Scrollbar

load_dotenv()
connectDatabase = os.getenv("conn")


def toggle_microphone():
    question =voice_text_qu()
    answer = text_ans(question)
    # Read the contents of the file
    file_path = 'userinfo.txt'
    with open(file_path, 'r') as file:
        str_userinfo = file.read()
        userinfo=str_userinfo.split(",")
        userId=userinfo[0]
        userName=userinfo[1]
   

    # Display the voice input and bot's response in the chat box
    receive_message(f"{question}", align="left")
    receive_message( answer, align="right")



    say_ans(answer)

    if userId:
        
        conn = psycopg2.connect(connectDatabase)
        cursor = conn.cursor()   
        query = "INSERT INTO search_history (user_id, question, answer) VALUES (%s, %s, %s)"
        cursor.execute(query, (userId,  question, answer))
        conn.commit()
        conn.close()  

# def exit_application():
#     # Add your code here to exit the application
#     # This can include closing any open resources or windows
#     window.destroy()

def send_message(event=None):  # Updated function with event parameter
    message = entry.get()
    if message:
        file_path = 'userinfo.txt'

        # Read the contents of the file
        with open(file_path, 'r') as file:
            str_userinfo = file.read()
            userinfo=str_userinfo.split(",")
            userId=userinfo[0]
            userName=userinfo[1]

        if userId:
        # Display user's message
            receive_message(f"{message}", align="left")

            answer = chatbot1(message)
            # Process the user's message with the bot
            # Replace the code below with your bot's logic
            response = answer 
            conn = psycopg2.connect(connectDatabase)
            cursor = conn.cursor()   
            query = "INSERT INTO search_history (user_id, question, answer) VALUES (%s, %s, %s)"
            cursor.execute(query, (userId,  message, response))
            conn.commit()
            conn.close()                   

            # Display bot's response
            receive_message( response, align="right")

            entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a message.")

# Create the main window
window = Tk()
window.title("Chat")
window_width = 1340
window_height = 690
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.configure(bg="#525561")
window.geometry('1340x690')

background_image = Image.open("python\\new\\Guzel (10).png")
background_image = background_image.resize((1340, 690))
background_photo = ImageTk.PhotoImage(background_image)

# Create a label to hold the background image
background_label = tk.Label(window, image=background_photo)
background_label.place(x=0, y=0)


home_bgImg1 = Image.open('python\\new\\homentn.png')
home_bgImg1= home_bgImg1.resize((130, 46))
photo2 = ImageTk.PhotoImage(home_bgImg1)
home_bg1 = Label(window, image=photo2, bg='#272A37')
home_bg1.image = photo2
      
home_bgImg2 = Image.open('python\\new\\chatbtn.png')
home_bgImg2= home_bgImg2.resize((130, 46))
photo3 = ImageTk.PhotoImage(home_bgImg2)
home_bg2 = Label(window, image=photo3, bg='#272A37')
home_bg2.image = photo3


home_bgImg3 = Image.open('python\\new\\facid.png')
home_bgImg2= home_bgImg2.resize((90,37))
photo4 = ImageTk.PhotoImage(home_bgImg3)
home_bg3 = Label(window, image=photo4, )
home_bg3.image = photo4
      
home_bgImg4 = Image.open('python\\new\\aboutbtn.png')
home_bgImg2= home_bgImg2.resize((90,37))
photo5 = ImageTk.PhotoImage(home_bgImg4)
home_bg4 = Label(window, image=photo5, )
home_bg4.image = photo5
       
home_bgImg5 = Image.open('python\\new\\logout.png')
home_bgImg2= home_bgImg2.resize((90, 37))
photo6 = ImageTk.PhotoImage(home_bgImg5)
home_bg5 = Label(window, image=photo6, )
home_bg5.image = photo6


        
def history():
    file_path = 'userinfo.txt'

    # Read the contents of the file
    try:
        with open(file_path, 'r') as file:
            str_userinfo = file.read()
            userinfo=str_userinfo.split(",")
            username=userinfo[1]
        if username:
            # Connect to the PostgreSQL database
            conn = psycopg2.connect(connectDatabase)
            cursor = conn.cursor()

            # Retrieve the user's question and corresponding answer from the database
            query ="SELECT * FROM user_search_history WHERE username =  %s"
            cursor.execute(query, (username,))
            results = cursor.fetchall()

            # Display the user's question and the corresponding answer(s)

            if results:
                for username, question, answer, search_date in results:
                    receive_message(f"{question}", align="left")

                     # Display bot's response
                    receive_message( answer, align="right")
            # else:
            #     receive_message( "No history found.", align="right")

            # Close the database connection
            conn.close()

            # Clear the entry field
            entry.delete(0, tk.END)
    except:
        window.destroy()        
       
        
def faceId():
    window.destroy()
    app = App()
    app.start() 
    os.system("python python\\home.py")
                
def Dashboard():
    window.withdraw()
    file_path = 'userinfo.txt'
    os.remove(file_path)
    os.system("python python\\Dashboard.py")
    window.destroy()


def about():
    window.withdraw()
    os.system("python python\\about.py")
    window.destroy()
def chat():
    window.withdraw()
    os.system("python python\\chat.py")
    window.destroy()

def home():
    window.withdraw()
    os.system("python python\\home.py")
    window.destroy()
       

        # ========== HOME BUTTON =======
home_button = Button(
         window, 
            image=photo2, 
            borderwidth=0,
            highlightthickness=0,
            cursor='hand2',
            relief="flat",
            command= home,
            )
home_button.place(x=140, y=40)


        # ========== chat BUTTON =======
chat_button = Button(
            window, 
            image=photo3,
            borderwidth=0,
            highlightthickness=0,
            cursor='hand2',
            relief="flat" ,
                    )
chat_button.place(x=300, y=40)



         # ========== face  BUTTON =======
face_button = Button(window,image=photo4 , borderwidth=0,
            highlightthickness=0,
            cursor='hand2',
            relief="flat" ,
            command=faceId)
face_button.place(x=765, y=40)

        # ========== about  BUTTON =======
about_button = Button(
            window, 
            image=photo5,
            borderwidth=0,
            highlightthickness=0,
            cursor='hand2',
            relief="flat" ,         
            command=about)
about_button.place(x=460, y=40)
        
     
            
        # ========== LOG OUT =======
logout_button = Button(window,  image=photo6,
            borderwidth=0,
            highlightthickness=0,
            cursor='hand2',
            relief="flat" , 
            command=Dashboard)
logout_button.place(x=1000, y=40)









display = tk.Text(window, height=20, width=63,bg='#73609B', fg="black", wrap=tk.WORD,font=("yu gothic ui SemiBold", 12))
display.place(x=640, y=110)

# Create a frame to hold the image and entry widget
enter_img1=Image.open("python\\new\\label.png")
enter_img1=enter_img1.resize((430,60))
enter_photo1=ImageTk.PhotoImage(enter_img1)
image_label1 = tk.Label(window, image=enter_photo1,bg='#40508a')
image_label1.place(x=660, y=540)



entry = Entry(image_label1,width=35, font=("yu gothic ui SemiBold", 15),bg=("#6f6caa"))
entry.place(x=20, y=15)

image = Image.open("python\\new\\send.png")
image = image.resize((40, 40))
photo = ImageTk.PhotoImage(image)

image = Image.open("python\\new\\exit.png")
image = image.resize((40, 40))
photo1 = ImageTk.PhotoImage(image)

image = Image.open("python\\new\\mic.png")
image = image.resize((40, 40))
photo2 = ImageTk.PhotoImage(image)

# Create a send button to trigger the send_message function
send_button = tk.Button(window, image=photo, text="Send", command=send_message, height=40, width=40, bg='#40508a')
send_button.place(x=1100, y=550)

# Create a microphone button to trigger the toggle_microphone function
mic_button = tk.Button(window, image=photo2, text="Microphone", command=toggle_microphone, height=40, width=40, bg='#40508a')
mic_button.place(x=1150, y=550)

# Create an exit button to trigger the exit_application function
# exit_button = tk.Button(window, image=photo1, text="Exit", command=exit_application, height=40, width=40, bg='#424E83')
# exit_button.place(x=1050, y=550)

display.tag_configure("left", justify="left")
display.tag_configure("right", justify="right")

bot_image = Image.open("python\\new\\robot.png") 
bot_image = bot_image.resize((40, 40))
bot_photo = ImageTk.PhotoImage(bot_image)
def receive_message(message, align="left"):
    if align == "left":
        display.tag_configure("left", justify="left", foreground="snow",background="#5875BB")
        display.insert(tk.END, message + "\n", "right")
    else:
        display.image_create(tk.END, image=bot_photo)
        display.insert(tk.END, " ", "left")
        display.tag_configure("right", justify="right", foreground="snow")
        display.insert(tk.END, message + "\n", "left")

    # Scroll to the end of the display
    display.see(tk.END)

history()

# Run the main loop
window.mainloop()