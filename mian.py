import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from students import Student
from training import Training
from face_recog import Face_recognition




class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # FIRST IMAGE
        try:
            img = Image.open(r'C:\Users\asus\Desktop\Attendance_rec_sys\frg1.jpg')
            img = img.resize((500, 130), Image.LANCZOS)
            self.photoimg = ImageTk.PhotoImage(img)
            Label(self.root, image=self.photoimg).place(x=0, y=0, width=500, height=130)
        except Exception as e:
            print("Error in img1:", e)

        # SECOND IMAGE
        try:
            img1 = Image.open(r'C:\Users\asus\Desktop\Attendance_rec_sys\Screenshot 2025-11-27 003339.png')
            img1 = img1.resize((500, 130), Image.LANCZOS)
            self.photoimg1 = ImageTk.PhotoImage(img1)
            Label(self.root, image=self.photoimg1).place(x=500, y=0, width=500, height=130)
        except Exception as e:
            print("Error in img2:", e)

        # THIRD IMAGE
        try:
            img2 = Image.open(r'C:\Users\asus\Desktop\Attendance_rec_sys\Screenshot 2025-11-27 002932.png')
            img2 = img2.resize((500, 130), Image.LANCZOS)
            self.photoimg2 = ImageTk.PhotoImage(img2)
            Label(self.root, image=self.photoimg2).place(x=1000, y=0, width=500, height=130)
        except Exception as e:
            print("Error in img3:", e)

        # BACKGROUND
        try:
            img3 = Image.open(r'C:\Users\asus\Desktop\Attendance_rec_sys\bg1.jpg')
            img3 = img3.resize((1530, 710), Image.LANCZOS)
            self.photoimg3 = ImageTk.PhotoImage(img3)

            self.bg_img = Label(self.root, image=self.photoimg3)
            self.bg_img.place(x=0, y=130, width=1530, height=710)

            Label(self.bg_img, text="FACE RECOG. ATTENDANCE SOFTWARE",
                  font=("times new roman", 35, "bold"),
                  bg="white", fg="darkblue").place(x=0, y=0, width=1530, height=50)

        except Exception as e:
            print("Error in background:", e)

        # ======================================
        # NOW BUTTON (COMPLETELY OUTSIDE)
        # ======================================
        try:
            img4 = Image.open(r'C:\Users\asus\Desktop\Attendance_rec_sys\Screenshot 2025-11-27 014848.png')
            img4 = img4.resize((220, 220), Image.LANCZOS)
            self.ph4 = ImageTk.PhotoImage(img4)

            stud_btn = Button(self.bg_img,
                              image= self.ph4, 
                              command = self.students_details,
                              compound="top",
                              font=("times new roman", 18, "bold"),
                              bg="darkblue", fg="white",
                              cursor="hand2")
            stud_btn.place(x=200, y=100, width=220, height=220)



            stud_btn1 = Button(self.bg_img,
                              text="Students Details",
                              command=self.students_details,
                              compound="top",
                              font=("times new roman", 18, "bold"),
                              bg="darkblue", fg="white",
                              cursor="hand2")
            stud_btn1.place(x=200, y=300, width=220, height=20)

          #DETECTION OF FACE BUTTON
            img5 = Image.open(r'C:\Users\asus\Desktop\Attendance_rec_sys\detimg1.ong.webp')
            img5 = img5.resize((220, 220), Image.LANCZOS)
            self.ph5 = ImageTk.PhotoImage(img5)

            stud_btn = Button(self.bg_img,
                              image= self.ph5,
                              command=self.face_data,
                              compound="top",
                              font=("times new roman", 18, "bold"),
                              bg="darkblue", fg="white",
                              cursor="hand2")
            stud_btn.place(x=500, y=100, width=220, height=220)



            stud_btn = Button(self.bg_img,
                              text="Face Detector",
                              compound="top",
                              command=self.face_data,
                              font=("times new roman", 18, "bold"),
                              bg="darkblue", fg="white",
                              cursor="hand2")
            stud_btn.place(x=500, y=300, width=220, height=20)



            img6 = Image.open(r'C:\Users\asus\Desktop\Attendance_rec_sys\att2.png')
            img6 = img6.resize((220, 220), Image.LANCZOS)
            self.ph6 = ImageTk.PhotoImage(img6)

            stud_btn = Button(self.bg_img,
                              image= self.ph6,
                             
                              compound="top",
                              font=("times new roman", 18, "bold"),
                              bg="darkblue", fg="white",
                              cursor="hand2")
            stud_btn.place(x=800, y=100, width=220, height=220)



            stud_btn = Button(self.bg_img,
                              text="Attendance Button",
                              compound="top",
                              font=("times new roman", 18, "bold"),
                              bg="darkblue", fg="white",
                              cursor="hand2")
            stud_btn.place(x=800, y=300, width=220, height=20)


            #fr help desk
            img7 = Image.open(r'C:\Users\asus\Desktop\Attendance_rec_sys\helpdsk.png')
            img7 = img7.resize((220, 220), Image.LANCZOS)
            self.ph7 = ImageTk.PhotoImage(img7)

            stud_btn = Button(self.bg_img,
                              image= self.ph7,
                             
                              compound="top",
                              font=("times new roman", 18, "bold"),
                              bg="darkblue", fg="white",
                              cursor="hand2")
            stud_btn.place(x=1100, y=100, width=220, height=220)



            stud_btn = Button(self.bg_img,
                              text="Help Desk",
                              compound="top",
                              font=("times new roman", 18, "bold"),
                              bg="darkblue", fg="white",
                              cursor="hand2")
            stud_btn.place(x=1100, y=300, width=220, height=20)


            #fr training fce button

            img8 = Image.open(r'C:\Users\asus\Desktop\Attendance_rec_sys\0_jmmltxTToDU0tucv.webp')
            img8 = img8.resize((220, 220), Image.LANCZOS)
            self.ph8 = ImageTk.PhotoImage(img8)

            stud_btn = Button(self.bg_img,
                              image= self.ph8,
                             
                              compound="top",command=self.train_data,
                              font=("times new roman", 18, "bold"),
                              bg="darkblue", fg="white",
                              cursor="hand2")
            stud_btn.place(x=200, y=400, width=220, height=220)



            stud_btn = Button(self.bg_img,
                              text="Train Button",
                              compound="top", command=self.train_data,
                              font=("times new roman", 18, "bold"),
                              bg="darkblue", fg="white",
                              cursor="hand2")
            stud_btn.place(x=200, y=600, width=220, height=20)



           #face  pics 
            img9 = Image.open(r'C:\Users\asus\Desktop\Attendance_rec_sys\group.png')
            img9 = img9.resize((220, 220), Image.LANCZOS)
            self.ph9 = ImageTk.PhotoImage(img9)

            stud_btn = Button(self.bg_img,
                              image= self.ph9,
                             
                              compound="top",
                              font=("times new roman", 18, "bold"),
                              bg="darkblue", fg="white",
                              cursor="hand2",command=self.open_img)
            stud_btn.place(x=500, y=400, width=220, height=220)



            stud_btn = Button(self.bg_img,
                              text="Face Photos",
                              compound="top",
                              font=("times new roman", 18, "bold"),
                              bg="darkblue", fg="white",
                              cursor="hand2",command=self.open_img)
            stud_btn.place(x=500, y=600, width=220, height=20)


            #developers face
            img10 = Image.open(r'C:\Users\asus\Desktop\Attendance_rec_sys\dev.llpng.jpg')
            img10 = img10.resize((220, 220), Image.LANCZOS)
            self.ph10 = ImageTk.PhotoImage(img10)

            stud_btn = Button(self.bg_img,
                              image= self.ph10,
                             
                              compound="top",
                              font=("times new roman", 18, "bold"),
                              bg="darkblue", fg="white",
                              cursor="hand2")
            stud_btn.place(x=800, y=400, width=220, height=220)


           
            stud_btn = Button(self.bg_img,
                              text="Developer Button",
                              compound="top",
                              font=("times new roman", 18, "bold"),
                              bg="darkblue", fg="white",
                              cursor="hand2")
            stud_btn.place(x=800, y=600, width=220, height=20)

 #exit button

            img11 = Image.open(r'C:\Users\asus\Desktop\Attendance_rec_sys\exit.jpg')
            img11= img11.resize((220, 220), Image.LANCZOS)
            self.ph11 = ImageTk.PhotoImage(img11)

            stud_btn = Button(self.bg_img,
                              image= self.ph11,
                             
                              compound="top",
                              font=("times new roman", 18, "bold"),
                              bg="darkblue", fg="white",
                              cursor="hand2")
            stud_btn.place(x=1100, y=400, width=220, height=220)



            stud_btn = Button(self.bg_img,
                              text="EXIT",
                              compound="top",
                              font=("times new roman", 18, "bold"),
                              bg="darkblue", fg="white",
                              cursor="hand2")
            stud_btn.place(x=1100, y=600, width=220, height=20)

        except Exception as e:
                print("Error in button:", e)
 


    def open_img(self):
        os.startfile("data")  #open directory named data bymaking button functional 
        
            #======================================functon button========================== fr iother window


     




    def students_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)    


    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Training(self.new_window)    


    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognition(self.new_window)    


        

   


        
        
        




if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
