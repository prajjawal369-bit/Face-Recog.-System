from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
import numpy as np


class Face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")

        # Top Title
        title_lbl = Label(self.root, text="FACE RECOGNITION", 
                          font=("times new roman", 35, "bold"),
                          bg="white", fg="darkred")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # ---------- IMAGE SIZES ----------
        img_width = 510
        img_height = 700
        y_pos = 55

        # ---------- LEFT IMAGE ----------
        img_left = Image.open(r'C:\Users\asus\Desktop\Attendance_rec_sys\Screenshot 2025-12-06 013816.png')
        img_left = img_left.resize((img_width, img_height), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        img_first = Label(self.root, image=self.photoimg_left).place(x=0, y=y_pos, width=img_width, height=img_height)

        # ---------- MID IMAGE ----------
        img_mid = Image.open(r'C:\Users\asus\Desktop\Attendance_rec_sys\Screenshot 2025-12-06 140641.png')
        img_mid = img_mid.resize((img_width, img_height), Image.Resampling.LANCZOS)
        self.photoimg_mid = ImageTk.PhotoImage(img_mid)
        img_second = Label(self.root, image=self.photoimg_mid).place(x=img_width, y=y_pos, width=img_width, height=img_height)

        # ---------- RIGHT IMAGE ----------
        img_right = Image.open(r'C:\Users\asus\Desktop\Attendance_rec_sys\Screenshot 2025-12-06 140212.png')
        img_right = img_right.resize((img_width, img_height), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        Label(self.root, image=self.photoimg_right).place(x=img_width*2, y=y_pos, width=img_width, height=img_height)



      



    
        # ---------- FACE RECOGNITION BUTTON ----------
        face_recog_btn = Button(self.root, text="FACE RECOGNITION", 
                            cursor="hand2",
                            command=self.face_recog,
                            font=("times new roman", 30, "bold"),
                            bg="lightblue", fg="white")


        face_recog_btn.place(x=530, y=720, width=450, height=50)
        #function for face recognition

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:    #fr maing rectangle around face
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)    #coordinates of rectangle or img
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))


                conn = mysql.connector.connect(host="localhost", username="root", password="Sarvesh@123", database="face_recognizing")
                my_cursor = conn.cursor()   
               # Fetch Student Name
                my_cursor.execute("SELECT Student_name FROM student WHERE Student_id=%s", (id,))
                result = my_cursor.fetchone()
                if result is None:
                    continue
                name = result[0]

                # Fetch Department
                my_cursor.execute("SELECT Dep FROM student WHERE Student_id=%s", (id,))
                d = my_cursor.fetchone()
                if d is None:
                    continue
                dep = d[0]

                # Fetch Roll Number
                my_cursor.execute("SELECT Roll FROM student WHERE Student_id=%s", (id,))
                r = my_cursor.fetchone()
                if r is None:
                    continue
                roll = r[0]

                










               

                if confidence > 78:
                    # Fetching details from database can be added here  fromm mysql if needed
                    cv2.putText(img, f"Name: {result}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)
                    cv2.putText(img, f"Roll: {r}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)
                    cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)
                    # cv2.putText(img, f"Confidence: {confidence}%", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 2)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)
                
               
                coord.append((x, y, w, h))
                conn.close()

            return coord
        

         #fr recognixing face image

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.3, 5, (255, 255, 255), "Face", clf)
            return img
        
        faceCascade = cv2.CascadeClassifier(r"C:\Users\asus\Desktop\Attendance_rec_sys\haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()  #algo creation as both r under cv2.face
        clf.read("classifier.xml")  #reading of file which we write while training

        video_cap = cv2.VideoCapture(0)
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)
            

            


            if cv2.waitKey(1) == 13:  #13 is enter key
                break


              # WINDOW CLOSE BUTTON (X) handling
            try:
                if cv2.getWindowProperty("Welcome to Face Recognition", cv2.WND_PROP_VISIBLE) < 1:
                    break
            except:
                break

        video_cap.release()
        cv2.destroyAllWindows()




if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()    
    
        