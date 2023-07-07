import tkinter as tk
from tkinter import messagebox
from tkinter import Tk, Button
from PIL import Image, ImageTk
import os

'''
Ibrahim
Mohammad 
Aseel
'''

# Define colors
BACKGROUND_COLOR = "#525561"   # Facebook blue
LISTBOX_COLOR = "black"      # White
ENTRY_COLOR = "black"        # Light blue-gray
SEND_BUTTON_COLOR = "#6f5383"  # Facebook blue

def send_message(event=None):  # Updated function with event parameter
    message = entry.get()
    if message:
        file_path = 'userinfo.txt'

        # Read the contents of the file
        with open(file_path, 'r') as file:
            str_userinfo = file.read()
            userinfo=str_userinfo.split(",")
            userId=userinfo[1]
        if userId:
        # Display user's message
            listbox.insert(tk.END, "You: " + message)
            
            # Process the user's message with the bot
            # Replace the code below with your bot's logic
            response = "Bot: Sorry, I am a basic bot and cannot respond."
            conn = psycopg2.connect("postgres://vfpgukpn:w4ArNUg7hh4GJkEt9Y6RK3jxzP_-ratk@ruby.db.elephantsql.com/vfpgukpn")
            cursor = conn.cursor()   
            query = "INSERT INTO search_history (user_id, question, answer) VALUES (%s, %s, %s)"
            cursor.execute(query, (userId,  message, response))
            conn.commit()
            conn.close()                   

            # Display bot's response
            listbox.insert(tk.END, response)
            entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a message.")

# Create the main window
import psycopg2

def history():
    file_path = 'userinfo.txt'

    # Read the contents of the file
    try:
        with open(file_path, 'r') as file:
            str_userinfo = file.read()
            userinfo=str_userinfo.split(",")
            username=userinfo[0]
        if username:
            # Connect to the PostgreSQL database
            conn = psycopg2.connect("postgres://vfpgukpn:w4ArNUg7hh4GJkEt9Y6RK3jxzP_-ratk@ruby.db.elephantsql.com/vfpgukpn")
            cursor = conn.cursor()

            # Retrieve the user's question and corresponding answer from the database
            query ="SELECT * FROM user_search_history WHERE username =  %s"
            cursor.execute(query, (username,))
            results = cursor.fetchall()

            # Display the user's question and the corresponding answer(s)

            if results:
                for username, question, answer, search_date in results:
                    listbox.insert(tk.END, f"User: {question}")
                    listbox.insert(tk.END, f"Bot: {answer}")
            else:
                listbox.insert(tk.END, "No history found.")


            # Close the database connection
            conn.close()

            # Clear the entry field
            entry.delete(0, tk.END)
    except:
        window.destroy()
def delet_info():
    window.destroy()  
    file_path = 'userinfo.txt'
    os.remove(file_path)
    os.system("python python/chat.py")
   
    
window = tk.Tk()
window.title("GuzelBot App")
window_width = 1340 # Set the desired width of the window
window_height = 690  # Set the desired height of the window
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.configure(bg="#525561")
window.geometry('1340x690')

image = Image.open("python\\assets\\image_1.png")

# Resize the image to 1430x690
resized_image = image.resize((1430, 690),)

# Convert the resized image to PhotoImage
Login_backgroundImage = ImageTk.PhotoImage(resized_image)

# Create the label with the resized image
bg_imageLogin = tk.Label(
    window,
    image=Login_backgroundImage,
    bg="#525561"
)
bg_imageLogin.place(x=-10, y=-7)

# Load the image file
image = Image.open("python\\images2/send-message.png")
image = image.resize((40, 40))  # Resize the image to 20x20 pixels
photo = ImageTk.PhotoImage(image)

image = Image.open("python\\images2/logout.png")
image = image.resize((40, 40))  # Resize the image to 20x20 pixels
photo1 = ImageTk.PhotoImage(image)


image = Image.open("python\\images2/mic.png")
image = image.resize((40, 40))  # Resize the image to 20x20 pixels
photo2 = ImageTk.PhotoImage(image)






# Create a listbox to display messages
listbox = tk.Listbox(window,bg='#272A37',fg='white',bd=10,borderwidth=9,font=("", 15, "bold"))
listbox.pack(padx=300, pady=40, fill="x", expand=True)


entry = tk.Entry(window, bg="#272A37",fg='white',width=6,bd=10,borderwidth=9,font=("", 15, "bold"))
entry.pack(padx=300, pady=10, fill="x",)
entry.bind("<Return>", send_message)  # Bind the Return key to send_message function
history()



# Create a frame for the buttons
button_frame = tk.Frame(window, bg="#272A37",bd=30,borderwidth=9)
button_frame.pack(padx=300,pady=50)

# Create a send button
send_button = tk.Button(button_frame, image=photo, command=send_message, height=40, width=40)
send_button.pack(side="left",pady=20,padx=20)

# Create a quit button

# Create a mic button
mic_button = tk.Button(button_frame, image=photo2, height=40, width=40)
mic_button.pack(side="left",  padx=20)

quit_button = tk.Button(button_frame, image=photo1, command=delet_info, height=40, width=40)
quit_button.pack(side="left", padx=50)

window.mainloop()