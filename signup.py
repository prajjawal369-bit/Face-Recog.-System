from tkinter import *
from tkinter import messagebox
import mysql.connector

class Signup:
    def __init__(self, root):
        self.root = root
        self.root.title("Signup Page")

     
        self.root.state('zoomed')  #for max window

        self.root.resizable(True, True)


        w = 500
        h = 450

        screen_w = root.winfo_screenwidth()
        screen_h = root.winfo_screenheight()

        x = int((screen_w/2) - (w/2))
        y = int((screen_h/2) - (h/2))

        self.root.geometry(f"{w}x{h}+{x}+{y}")
        self.root.resizable(False, False)
        self.root.configure(bg="#dfe9f3")   # Light stylish background

        self.username = StringVar()
        self.password = StringVar()

        # ================= Frame (Center Box) =================
        frame = Frame(self.root, bg="white", bd=2, relief=SOLID)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=380, height=360)

        title = Label(frame, text="Create Account",
                      font=("Arial", 22, "bold"), bg="white", fg="#333")
        title.pack(pady=15)

        # Username
        Label(frame, text="Username", font=("Arial", 12, "bold"),
              bg="white", fg="#555").pack(anchor=W, padx=40)
        Entry(frame, textvariable=self.username, font=("Arial", 14),
              bd=1, relief=SOLID).pack(pady=5, padx=40, fill=X)

        # Password
        Label(frame, text="Password", font=("Arial", 12, "bold"),
              bg="white", fg="#555").pack(anchor=W, padx=40, pady=(10, 0))
        Entry(frame, textvariable=self.password, font=("Arial", 14),
              bd=1, relief=SOLID, show="*").pack(pady=5, padx=40, fill=X)

        # Signup Button
        Button(frame, text="SIGN UP", font=("Arial", 15, "bold"),
               bg="#4CAF50", fg="white", cursor="hand2",
               command=self.create_account).pack(pady=25)

    # Create  A/c func.
    def create_account(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Sarvesh@123",
                database="face_recognizing"
            )
            cur = conn.cursor()

            cur.execute("INSERT INTO users(username, password) VALUES(%s, %s)",
                        (self.username.get(), self.password.get()))
            
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Account Created Successfully!")
            self.root.destroy()

            

            import login
            root = Tk()
            login.Login(root)
            root.mainloop()

        except mysql.connector.IntegrityError:
            messagebox.showerror("Error", "Username already exists!")

if __name__ == "__main__":
    root = Tk()
    Signup(root)
    root.mainloop()

  




