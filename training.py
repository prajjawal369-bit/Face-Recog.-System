from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os    #frfile accessing
import numpy as np



class Training:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train Data")


        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="white", fg="darkblue")
        title_lbl.place(x=0, y=0, width=1530, height=45)   
        img_top = Image.open(r'C:\Users\asus\Desktop\Attendance_rec_sys\Screenshot 2025-12-05 234302.png')
        img_top = img_top.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)


        first_lbl = Label(self.root, image=self.photoimg_top)
        first_lbl.place(x=0, y=55, width=1530, height=325)


        #button
        button_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2", font=("times new roman", 30, "bold"), bg="darkgreen", fg="white")
        button_1.place(x=0, y=380, width=1530, height=80)

        img_bottom = Image.open(r'C:\Users\asus\Desktop\Attendance_rec_sys\Screenshot 2025-12-05 234223.png')
        img_bottom = img_bottom.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=460, width=1530, height=325)


     #usage for lbph algo fr face recognition  local binaryy patterns histograms used fr recognize face and give output accordingly 

    def train_classifier(self):
        data_dir = ("data")    #data directory se images /data agya h 
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]  #using list comprehension to get all file paths


        faces = []     #empty list creation
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  #Gray scale image
            imageNp = np.array(img, 'uint8')      #convert image into numpy array so installl numpy as it increases performance for array handling
            id = int(os.path.split(image)[1].split('.')[1])  #3split user1.1iamgejpg into index and extract the image

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)  #diasplay image while training
            cv2.waitKey(1)==13   #13 is enter key fr closing window
        ids = np.array(ids)   #conerting ids into np arrays  

        #=================train the classifier and save========================
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!", parent=self.root)









if __name__ == "__main__":
    root = Tk()         
    obj = Training(root)
    root.mainloop()        