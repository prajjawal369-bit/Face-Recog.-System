from tkinter import *
from tkinter import messagebox
import mysql.connector

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.state("zoomed")   # Full screen
        self.root.configure(bg="#dfe9f3")

        self.username = StringVar()
        self.password = StringVar()

        # ---------------- LOGIN FRAME ----------------
        frame = Frame(self.root, bg="white", bd=2, relief=SOLID)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=400, height=350)

        Label(frame, text="LOGIN", font=("Arial", 24, "bold"),
              bg="white", fg="#333").pack(pady=20)

        Label(frame, text="Username", font=("Arial", 13, "bold"),
              bg="white").pack(anchor=W, padx=40)
        Entry(frame, textvariable=self.username, font=("Arial", 14),
              bd=1, relief=SOLID).pack(pady=5, padx=40, fill=X)

        Label(frame, text="Password", font=("Arial", 13, "bold"),
              bg="white").pack(anchor=W, padx=40, pady=(10, 0))
        Entry(frame, textvariable=self.password, font=("Arial", 14),
              bd=1, relief=SOLID, show="*").pack(pady=5, padx=40, fill=X)

        Button(frame, text="LOGIN", font=("Arial", 15, "bold"),
               bg="#0078D7", fg="white", cursor="hand2",
               command=self.login).pack(pady=25)

    # ---------------- LOGIN FUNCTION ----------------
    def login(self):
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
            cur.execute("SELECT * FROM users WHERE username=%s AND password=%s",
                        (self.username.get(), self.password.get()))
            row = cur.fetchone()
            conn.close()

            if row is None:
                messagebox.showerror("Error", "Invalid Username or Password")
            else:
                messagebox.showinfo("Success", "Login Successful!")
                self.open_main_page()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ---------------- OPEN MAIN PAGE ----------------
    def open_main_page(self):
        self.root.destroy()

       
        import mian  # File name of your main page
        root = Tk()
        mian.Face_Recognition_System(root)   # Main class
        root.mainloop()


if __name__ == "__main__":
    root = Tk()
    Login(root)
    root.mainloop()
