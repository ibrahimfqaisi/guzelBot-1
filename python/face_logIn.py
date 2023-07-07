import os.path
import tkinter as tk
import cv2
import util
from face_emotion import emotion
import psycopg2
import os
from dotenv import load_dotenv
from tkinter import Tk, Button
from PIL import ImageTk, Image
load_dotenv()
connectDatabase = os.getenv("conn")


class App:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Face Login")
        self.main_window.geometry("1340x690")

        # Load the background image
        background_image = Image.open("python\\new\\Guzel.png")
        self.background_photo = ImageTk.PhotoImage(background_image)

        # Create a label to display the background photo
        self.background_label = tk.Label(
            self.main_window, image=self.background_photo
        )
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)



        self.login_button_main_window = util.get_button(
            self.main_window, "login", "turquoise1", self.login
        )
        self.login_button_main_window.place(x=900, y=300)

        self.webcam_label = util.get_img_label(self.main_window)
        self.webcam_label.place(x=50, y=80, width=600, height=450)

        self.add_webcam(self.webcam_label)

        self.db_dir = "./db"
        if not os.path.exists(self.db_dir):
            os.mkdir(self.db_dir)

    def add_webcam(self, label):
        if "cap" not in self.__dict__:

            self.cap = cv2.VideoCapture(0)

        self._label = label
        self.process_webcam()

    def des(self):
        cv2.destroyAllWindows()
        self.main_window.destroy()

    def process_webcam(self):
        global ret, frame

        ret, frame = self.cap.read()
        self.most_recent_capture_arr = frame
        img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)

        self.most_recent_capture_pil = Image.fromarray(img_)
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        self._label.imgtk = imgtk
        self._label.configure(image=imgtk)

        self._label.after(20, self.process_webcam)

    def saveData(self, get_email):
        # Implement the login functionality here
        email = get_email

        # Connect to the PostgreSQL database
        conn = psycopg2.connect(connectDatabase)
        cursor = conn.cursor()

        # Check if the email exists in the database
        query = "SELECT * FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()

        if user:
            file_path = "userinfo.txt"
            # Save the JSON data to a file
            with open(file_path, "w+") as json_file:
                json_file.write(f"{user[0]},{user[1]},{user[2]}")

    def login(self):
        emotion(self.cap)

        name = util.recognize(self.most_recent_capture_arr, self.db_dir)

        if name in ["unknown_person", "no_persons_found"]:
            pass
            # util.msg_box("Ups...", "Unknown user. Please register new user or try again.")
        else:
            get_email = name
            self.saveData(get_email)
            print("Welcome back !", "Welcome, {}.".format(name))
        self.des()

    def des(self):
        self.cap.release()  # Release the webcam capture
        cv2.destroyAllWindows()
        self.main_window.destroy()

    def start(self):
        self.main_window.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()
