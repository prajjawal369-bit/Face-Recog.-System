from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

import cv2
import os   #directtotry



class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #======= varaibles=====
        self.var_stud_name = StringVar()
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_std_id = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_radio1 = StringVar()
        

  # FIRST IMAGE
        try:
            img = Image.open(r'C:\Users\asus\Desktop\Attendance_rec_sys\stu55.jpg')
            img = img.resize((500, 130), Image.LANCZOS)
            self.photoimg = ImageTk.PhotoImage(img)
            Label(self.root, image=self.photoimg).place(x=0, y=0, width=500, height=150)
        except Exception as e:
            print("Error in img1:", e)

        # SECOND IMAGE
        try:
            img1 = Image.open(r'C:\Users\asus\Desktop\Attendance_rec_sys\stu3.png')
            img1 = img1.resize((500, 130), Image.LANCZOS)
            self.photoimg1 = ImageTk.PhotoImage(img1)
            Label(self.root, image=self.photoimg1).place(x=500, y=0, width=500, height=150)
        except Exception as e:
            print("Error in img2:", e)

        # THIRD IMAGE
        try:
            img2 = Image.open(r'C:\Users\asus\Desktop\Attendance_rec_sys\stu2.png')
            img2 = img2.resize((500, 130), Image.LANCZOS)
            self.photoimg2 = ImageTk.PhotoImage(img2)
            Label(self.root, image=self.photoimg2).place(x=1000, y=0, width=500, height=150)
        except Exception as e:
            print("Error in img3:", e)



       # BACKGROUND
        try:
            img3 = Image.open(r'C:\Users\asus\Desktop\Attendance_rec_sys\bg1.jpg')
            img3 = img3.resize((1530, 710), Image.LANCZOS)
            self.photoimg3 = ImageTk.PhotoImage(img3)

            self.bg_img = Label(self.root, image=self.photoimg3)
            self.bg_img.place(x=0, y=130, width=1530, height=710)

            Label(self.bg_img, text="Student Management System",
                  font=("times new roman", 35, "bold"),
                  bg="white", fg="red").place(x=0, y=0, width=1530, height=100)

        except Exception as e:
            print("Error in background:", e)




        main_frame = Frame(self.bg_img, bd=2, bg="white")
        main_frame.place(x=30, y=130, width=1485, height=600)

        #left frame

        left_frames = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                     text="Student Details",
                                     font=("times new roman", 12, "bold"))
        left_frames.place(x=10, y=10, width=730, height=580)

        imgleft = Image.open(r'C:\Users\asus\Desktop\Attendance_rec_sys\happy-students-holding-books-in-row-photo.jpg')
        imgleft = imgleft.resize((500, 130), Image.LANCZOS)
        self.photoimgleft = ImageTk.PhotoImage(imgleft)
        Label(self.root, image=self.photoimgleft).place(x=130, y=290, width=500, height=150)

        

        #current subect info
        currentcourses_frames = LabelFrame(left_frames, bd=2, bg="white", relief=RIDGE,
                                     text="Course Information",
                                     font=("times new roman", 12, "bold"))
        currentcourses_frames.place(x=5, y=160, width=710, height=100)


        #departments
        dep_label= Label(currentcourses_frames,text="Department:",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0 , column= 0 , padx= 10)

        dep_combo=ttk.Combobox(currentcourses_frames,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=20)
        dep_combo.grid(row=0, column=1, padx=2, pady=5, sticky=W)
        dep_combo["values"]=("Select Department","Computer","IT","Civil","MCA")
        dep_combo.current(0)    #combobox used frmultiple opiton


        #course
        course_label= Label(currentcourses_frames,text="Course:",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0 , column= 2, padx= 1)

        course_combo=ttk.Combobox(currentcourses_frames,textvariable= self.var_course,font=("times new roman",12,"bold"),state="readonly",width=20)
        course_combo.grid(row=0, column=3, padx=2, pady=5, sticky=W)
        course_combo["values"]=("Select Course","FE","EE","CC","CA","SPM")
        course_combo.current(0) 

        #YEAR

        # year_label= Label(currentcourses_frames,text="Year:",font=("times new roman",12,"bold"),bg="white")
        # year_label.grid(row=1 , column= 0 , padx= 1)
        # self.var_year.set("Select Year")
        # year_combo=ttk.Combobox(currentcourses_frames,textvariable= self.var_year,font=("times new roman",12,"bold"),state="readonly",width=20)
        # year_combo.grid(row=1, column=1, padx=2, pady=5, sticky=W)
        # year_combo["values"]=("Select Year","1st","2nd","3rd","4th")
        # year_combo.current(0) 

        # #sems

        # sem_label= Label(currentcourses_frames, text="Sem:",font=("times new roman",12,"bold"),bg="white")
        # sem_label.grid(row=1 , column= 2, padx= 1)

        # sem_combo=ttk.Combobox(currentcourses_frames,textvariable=self.var_sem,font=("times new roman",12,"bold"),state="readonly",width=20)
        # sem_combo.grid(row=1, column=3, padx=2, pady=5, sticky=W)
        # sem_combo["values"]=("Select Sem","1st","2nd","3rd","4th","5th",
        #                      "6th","7th","8th")
        # sem_combo.current(0) 


        # YEAR
        year_label = Label(currentcourses_frames, text="Year:", font=("times new roman",12,"bold"), bg="white")
        year_label.grid(row=1, column=0, padx=1)

        self.var_year.set("Select Year")
        year_combo = ttk.Combobox(currentcourses_frames, textvariable=self.var_year, 
                                font=("times new roman",12,"bold"), state="readonly", width=20)
        year_combo.grid(row=1, column=1, padx=2, pady=5, sticky=W)
        year_combo["values"] = ("Select Year", "1st", "2nd", "3rd", "4th")
        year_combo.current(0)

        # SEM
        sem_label = Label(currentcourses_frames, text="Sem:", font=("times new roman",12,"bold"), bg="white")
        sem_label.grid(row=1, column=2, padx=1)

        sem_combo = ttk.Combobox(currentcourses_frames, textvariable=self.var_sem,
                                font=("times new roman",12,"bold"), state="readonly", width=20)
        sem_combo.grid(row=1, column=3, padx=2, pady=5, sticky=W)
        sem_combo["values"] = ("Select Sem", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th")
        sem_combo.current(0)


        #classstudent info

        classstud_frames = LabelFrame(left_frames, bd=2, bg="white", relief=RIDGE,
                                     text="Class Student Info.",
                                     font=("times new roman", 12, "bold"))
        classstud_frames.place(x=5, y=250, width=710, height=300)

        #studentid

        stud_id_Label = Label(classstud_frames , text="StudentID:", font = ("times new roman" , 13, "bold"),bg="white")
        stud_id_Label.grid(row=0 , column=0 , padx=10 , pady=5 , sticky=W)
        stud_id_entry = ttk.Entry(classstud_frames , width=20 ,textvariable= self.var_std_id, font = ("times new roman" , 13, "bold"))
        stud_id_entry.grid(row=0 , column=1 , padx=10 , pady=5 , sticky=W)   #ttk fr style


        stud_name_Label = Label(classstud_frames , text="StudentName:", font = ("times new roman" , 13, "bold"),bg="white")
        stud_name_Label.grid(row=0 , column=2 , padx=10 , pady=5 , sticky=W)
        stud_name_entry = ttk.Entry(classstud_frames ,textvariable=self.var_stud_name, width=20 , font = ("times new roman" , 13, "bold"))
        stud_name_entry.grid(row=0 , column=3 , padx=10 , pady=5 , sticky=W)

        # SECTION
        class_div_Label = Label(classstud_frames, text="Section:", 
                                font=("times new roman",13,"bold"), bg="white")
        class_div_Label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        div_combo = ttk.Combobox(classstud_frames, textvariable=self.var_div,
                                font=("times new roman",12,"bold"), state="readonly", width=20)
        div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        div_combo["values"] = ("Select Div", "A", "B", "C", "D")
        div_combo.current(0)

        

        roll_no_Label = Label(classstud_frames , text="Roll No:", font = ("times new roman" , 13, "bold"),bg="white")
        roll_no_Label.grid(row=1 , column=2 , padx=10 , pady=5 , sticky=W)
        roll_no_entry = ttk.Entry(classstud_frames ,textvariable= self.var_roll, width=20 , font = ("times new roman" , 13, "bold")) 
        roll_no_entry.grid(row=1 , column=3 , padx=10 , pady=5 , sticky=W)
        #gender

       # GENDER
        gender_Label = Label(classstud_frames, text="Gender:", 
                            font=("times new roman",13,"bold"), bg="white")
        gender_Label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(classstud_frames,
                                    textvariable=self.var_gender,
                                    font=("times new roman",12,"bold"),
                                    state="readonly",
                                    width=20)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        gender_combo["values"] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)



        #dob
        dob_Label = Label(classstud_frames ,  text="D.O.B:", font = ("times new roman" , 13, "bold"),bg="white")
        dob_Label.grid(row=2 , column=2 , padx=10 , pady=5 , sticky=W)
        dob_entry = ttk.Entry(classstud_frames ,textvariable= self.var_dob , width=20 , font = ("times new  roman" , 13, "bold"))       
        dob_entry.grid(row=2 , column=3 , padx=10 , pady=5 , sticky=W)                                                  

        #email
        email_Label = Label(classstud_frames ,text="Email:", font = ("times new roman" , 13, "bold"),bg="white")       
        email_Label.grid(row=3 , column=0 , padx=10 , pady=5 , sticky=W)
        email_entry = ttk.Entry(classstud_frames , textvariable=self.var_email, width=20 , font = ("times new roman" , 13, "bold"))          
        email_entry.grid(row=3 , column=1 , padx=10 , pady=5 , sticky=W) 
        #phone       

        phone_Label = Label(classstud_frames ,  text="Phone No:", font = ("times new roman" , 13, "bold"),bg="white")       
        phone_Label.grid(row=3 , column=2 , padx=10 , pady=5 , sticky=W)
        phone_entry = ttk.Entry(classstud_frames ,textvariable=self.var_phone , width=20 , font = ("times new roman" , 13, "bold"))          
        phone_entry.grid(row=3 , column=3 , padx=10 , pady=5 , sticky=W) 

        #teacher

        teacher_Label = Label(classstud_frames , text="Teacher Name:", font = ("times new roman" , 13, "bold"),bg="white")       
        teacher_Label.grid(row=4 , column=0 , padx=10 , pady=5 , sticky=W)
        teacher_entry = ttk.Entry(classstud_frames ,textvariable= self.var_teacher, width=20 , font = ("times new roman" , 13, "bold")) 
        teacher_entry.grid(row=4 , column=1 , padx=10 , pady=5 , sticky=W)

        
       #radio buttons

        self.var_radio1 = StringVar()
        radiobtn1=ttk.Radiobutton(classstud_frames,variable=self.var_radio1, text="Take Pics Sample", value="yes")
        radiobtn1.grid(row=5, column=0 , padx=10, pady=5) 

        radiobtn2=ttk.Radiobutton(classstud_frames,variable=self.var_radio1, text="No Pics Sample", value="no")
        radiobtn2.grid(row=5, column=1 , padx=10, pady=5)
        #butframe

        buttonframe = Frame(classstud_frames, bd=2, relief=RIDGE, bg="white")
        buttonframe.place(x=0, y=200, width=705, height=35)

        save_btn=Button(buttonframe,text="Save", command= self.add_data,width=17,font=("times new roman",13,"bold"),bg="red",fg="white")
        save_btn.grid(row=0,column=0)


        update_btn=Button(buttonframe,text="Update", command= self.update_data ,width=17,font=("times new roman",13,"bold"),bg="red",fg="white")  
        update_btn.grid(row=0,column=1)


        delete_btn=Button(buttonframe,text="Delete",command = self.delete_data,width=17,font=("times new roman",13,"bold"),bg="red",fg="white")  
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(buttonframe,text="Reset",command =  self.reset_data,width=17,font=("times new roman",13,"bold"),bg="red",fg="white")  
        reset_btn.grid(row=0,column=3)  

        #btnframe2

        btnframe2 = Frame(classstud_frames, bd=2, relief=RIDGE, bg="white")
        btnframe2.place(x=0, y=235, width=705, height=35)
        takepic_btn=Button(btnframe2,text="Take Photo Sample", command=self.generate_dataset,width=35,font=("times new roman",13,"bold"),bg="red",fg="white")
        takepic_btn.grid(row=0,column=0)  

        updatepic_btn=Button(btnframe2,text="Update Photo Sample",width=35,font=("times new roman",13,"bold"),bg="red",fg="white")      
        updatepic_btn.grid(row=0,column=1)  



        #rightframe

        right_frames = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                     text="Student Details",
                                     font=("times new roman", 12, "bold"))
        right_frames.place(x=750, y=10, width=720, height=580)

        imgright = Image.open(r'C:\Users\asus\Desktop\Attendance_rec_sys\istockphoto-962475722-612x612.jpg')
        imgright = imgright.resize((500, 130), Image.LANCZOS)
        self.photoimgright = ImageTk.PhotoImage(imgright)
        Label(self.root, image=self.photoimgright).place(x=900, y=290, width=500, height=150)


        search_frames = LabelFrame(right_frames, bd=2, bg="white", relief=RIDGE,
                                     text="Search System.",
                                     font=("times new roman", 12, "bold"))
        search_frames.place(x=5, y=160, width=700, height=100)

        search_Label = Label(search_frames , text="Search Here:", font = ("times new roman" , 13, "bold"),bg="white",fg="red")
        search_Label.grid(row=0 , column=0 , padx=10 , pady=5 , sticky=W)
        search_entry = ttk.Entry(search_frames , width=20 , font = ("times new  roman" , 13, "bold"))       
        search_entry.grid(row=0 , column=3 , padx=10 , pady=5 , sticky=W)          

        search_combo=ttk.Combobox(search_frames,font=("times new roman",12,"bold"),state="readonly",width=10)
        search_combo.grid(row=0, column=2, padx=2, pady=5, sticky=W)
        search_combo["values"]=("Select ","Rollno.","PhoneNO.","Class")
        search_combo.current(0) 

        search_btn=Button(search_frames,text="Search:",width=10,font=("times new roman",10,"bold"),bg="red",fg="white")
        search_btn.grid(row=0,column=5,padx= 4)

        searchall_btn=Button(search_frames,text="Search All:",width=10,font=("times new roman",10,"bold"),bg="red",fg="white")
        searchall_btn.grid(row=0,column=6)
            
        #table framess
        table_frames = LabelFrame(right_frames, bd=2, bg="white", relief=RIDGE,
                                     text="View Details and Search System.",
                                     font=("times new roman", 12, "bold"))
        table_frames.place(x=5, y=270, width=700, height=270)
        scroll_x = ttk.Scrollbar(table_frames, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frames, orient=VERTICAL)

        self.student_table = ttk.Treeview(
        table_frames,
        columns=("dep","course","year","sem","id","name","div","roll", "gender","dob","email","phone","address","teacher","photos"),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Sem")
        self.student_table.heading("id", text="StudentID")
        self.student_table.heading("name", text="StudentName")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")  
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone No")
        self.student_table.heading("address", text="Address")   
        self.student_table.heading("teacher", text="Teacher Name")
        self.student_table.heading("photos", text="PhotoSampleStatus")

      

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)    
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photos", width=100)

        self.student_table["show"] = "headings"
        self.fetch_data()
        self.student_table.bind("<ButtonRelease>", self.get_cursor) 

        #==== ffunction dec.=====
    def add_data(self):

        if (self.var_stud_name.get() == "" or 
            self.var_std_id.get() == "" or 
            self.var_dep.get() == "Select Department" or 
            self.var_course.get() == "" or 
            self.var_year.get() == "" or 
            self.var_sem.get() == ""):

            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Sarvesh@123",
                database="face_recognizing"
            )
            my_cursor = conn.cursor()

            query = """
            INSERT INTO student
            (Dep, Course, Year, Semester, Student_id, Student_name, Divison, Roll, Gender, DOB, Email, Phone, Address, Teacher, PhotoSampleStatus)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            values = (
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_sem.get(),
                self.var_std_id.get(),
                self.var_stud_name.get(),
                self.var_div.get(),
                self.var_roll.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_teacher.get(),
                self.var_radio1.get()   # PhotoSample
            )

            my_cursor.execute(query, values)
            conn.commit()
            conn.close()

            self.fetch_data()
            messagebox.showinfo("Success", "Student details added successfully!", parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

                #====fetching the data
    def fetch_data(self):
                conn= mysql.connector.connect(host="localhost", user="root", password="Sarvesh@123", database="face_recognizing") #databse name same a stable name 
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                data=my_cursor.fetchall() #frvfetching the data

                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END, values=i)  #insert the data in student table
                    conn.commit()

                conn.close()


             #====get cursor=====
    def get_cursor(self, event=""):
                cursor_focus=self.student_table.focus()  #focusing on student table
                content=self.student_table.item(cursor_focus)   #cursor focus on student table
                data=content["values"]

                if(len(data) < 12 ):
                    print("Row data incomplete:", data)
                    return

                self.var_dep.set(data[0])
                self.var_course.set(data[1])
                self.var_year.set(data[2])
                self.var_sem.set(data[3])
                self.var_std_id.set(data[4])
                self.var_stud_name.set(data[5])
                self.var_div.set(data[6])
                self.var_roll.set(data[7])  
                self.var_gender.set(data[8])
                self.var_dob.set(data[9])
                self.var_email.set(data[10])
                self.var_phone.set(data[11])
                self.var_address.set(data[12])
                self.var_teacher.set(data[13])
                self.var_radio1.set(data[14])



#update function
    def update_data(self):
        if self.var_stud_name.get() == "" or self.var_std_id.get() == "" or self.var_dep.get() == "" or self.var_course.get() == "" or self.var_year.get() == "" or self.var_sem.get() == "":
           messagebox.showerror("Error", "All fields are required", parent=self.root)

        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost  ", user="root", password="Sarvesh@123", database="face_recognizing")  
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set dep=%s, Course=%s, Year=%s, Semester=%s, name=%s, Divison=%s, DOB=%s, Email=%s, PhoneNo=%s, Teacher=%s, PhotoSampleStatus=%s where Student_Id=%s", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_stud_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()   #last valUE
                    ))

                else:
                    if not Update:
                        return

                messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)   
                conn.commit()   
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)   



                #delete btn function

    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to delete this student details", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="Sarvesh@123", database="face_recognizing")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"  #qury of delete sql query
                    value = (self.var_std_id.get(),)   #fr errror , single value
                    my_cursor.execute(sql, value)

                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Student details successfully deleted", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)  



    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Sem")
        self.var_std_id.set("")
        self.var_stud_name.set("")
        self.var_div.set("Select Div")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("") 
        
#======== generate data set or take photo sample

    def generate_dataset(self):
                
        

        # if self.var_stud_name.get() == "" or self.var_std_id.get() == "" or self.var_dep.get() == "" or self.var_course.get() == "" or self.var_year.get() == "" or self.var_sem.get() == "":
        #     messagebox.showerror("Error", "All fields are required", parent=self.root)
        # else:
        #     try:
        #         conn = mysql.connector.connect(host="localhost", user="root", password="Sarvesh@123", database="face_recognizing")
        #         my_cursor = conn.cursor()
        #         my_cursor.execute("select * from student")  #table name student for fech data
        #         myresult = my_cursor.fetchall()
        #         for i in myresult:
        #             print(i)
        #         # id = 0
                # for x in myresult:
                #     id += 1
                # my_cursor.execute("update student set dep=%s, course=%s, year=%s, sem=%s, name=%s, div=%s, roll=%s, gender=%s ,dob=%s, email=%s, phone=%s, address=%s, teacher=%s, photosample=%s where id=%s", (
                #     self.var_dep.get(),
                #     self.var_course.get(),
                #     self.var_year.get(),
                #     self.var_sem.get(),
                #     self.var_stud_name.get(),
                #     self.var_div.get(),
                #     self.var_roll.get(),
                #     self.var_gender.get(),
                #     self.var_dob.get(),
                #     self.var_email.get(),
                #     self.var_phone.get(), 
                #     self.var_address.get(),
                #     self.var_teacher.get(),
                #     self.var_radio1.get(),
                #     self.var_std_id.get()== id+1  #last vLUE
                # ))
                # conn.commit()
                # self.fetch_data()
                # self.reset_data()
                # conn.close()

                # ======== Load predefined data on face frontals from opencv ========
                #face_classifier = cv2.CascadeClassifier("C:\\Users\\asus\\Desktop\\Attendance_rec_sys\\haarcascade_frontalface_default.xml")

        # def face_cropped(img):
        #     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #     faces = face_classifier.detectMultiScale(gray, 1.3, 5)
        #             # scaling factor=1.3 (by default)
        #             # Minimum neighbor=5   

        #             for (x, y, w, h) in faces:
        #                 face_cropped = img[y:y + h, x:x + w]
        #                 return face_cropped
             
        #         cap = cv2.VideoCapture(0)
        #         img_id = 0
        #         while True:
        #             ret, my_frame = cap.read()
        #             if face_cropped(my_frame) is not None:
        #                 img_id += 1
        #                 face = cv2.resize(face_cropped(my_frame), (450, 450))
        #                 face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        #                 file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
        #                 cv2.imwrite(file_name_path, face)
        #                 cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
        #                 cv2.imshow("Cropped Face", face)
        #                 if cv2.waitKey(1) == 13 or int(img_id) == 100:
        #                     break
        #         cap.release()
        #         cv2.destroyAllWindows()
        #         messagebox.showinfo("Result", "Generating data sets completed!!!")
        #     except Exception as es:
        #         messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)


        if self.var_std_id.get() == "" or self.var_stud_name.get() == "":
            messagebox.showerror("Error", "Student ID and Name are required", parent=self.root)
            return    

        # Database update for photo sample
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Sarvesh@123",
                database="face_recognizing"
            )
            my_cursor = conn.cursor()
            my_cursor.execute(
                "SELECT * FROM student WHERE student_id=%s",
                (self.var_std_id.get(),)
            )
            result = my_cursor.fetchone()

            id = self.var_std_id.get()
            name = self.var_stud_name.get()

            # Haarcascade path
            classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            def face_crop(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = classifier.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    face = img[y:y+h, x:x+w]
                    return face
                return None

            cam = cv2.VideoCapture(0)
            img_id = 0

            while True:
                ret, frame = cam.read()
                if face_crop(frame) is not None:
                    img_id += 1
                    face = cv2.resize(face_crop(frame), (450, 450))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                    file_path = f"data/user.{id}.{img_id}.jpg"
                    cv2.imwrite(file_path, face)

                    cv2.putText(face, str(img_id), (50, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
                    cv2.imshow("Face Cropper", face)

                if cv2.waitKey(1) == 13 or img_id == 100:
                    break

            cam.release()
            cv2.destroyAllWindows()

            messagebox.showinfo("Result", "Generating data set completed", parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)










                     








        

if __name__ == "__main__":
     root = Tk()
     obj = Student(root)
     root.mainloop()

