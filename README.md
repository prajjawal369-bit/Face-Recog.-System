# Face-Recog.-System
This project is an advanced Face Recognition System developed in Python, designed to bridge the gap between computer vision theory and practical application. The system is engineered to detect, track, and identify human faces within live video streams  with high precision.

AI-Powered Face Recognition Attendance System
This is a comprehensive Real-Time Face Recognition System developed in Python. The application provides a complete end-to-end workflow, from secure user authentication to automated dataset generation and live facial identification.

🚀 Project Workflow
To ensure the system functions correctly, please follow the operational sequence below:

User Authentication: Users must first register via signup.py to store their credentials in the MySQL database. Once registered, they can access the dashboard through the login.py interface.

Student Enrollment & Data Collection: From the main dashboard (mian.py), navigate to the Student Details section (students.py). After entering the student's information, use the "Take Photo Sample" button to capture 100 high-quality facial images via webcam for the dataset.

Model Training: Once the images are collected, proceed to the Train Data module (training.py). Clicking the "Train Data" button initiates the LBPH (Local Binary Patterns Histograms) algorithm, which processes the images and generates a classifier.xml file.

Real-Time Recognition: Finally, launch the Face Detector (face_recog.py). The system will open a live camera feed, detect faces using the Haarcascade classifier, and match them against the trained database to display the student's name and details on the screen.

🛠️ Tech Stack
Programming Language: Python.

GUI Framework: Tkinter (for a responsive and user-friendly interface).

Computer Vision: * OpenCV: Utilized for image processing, frame capturing, and video handling.

Haarcascade: Used for frontal face detection.

LBPH Algorithm: The core algorithm used for recognizing faces and matching histograms.

Database Management: MySQL Workbench (used to store user login data and detailed student records).

Key Libraries: Pillow (PIL) for image manipulation, NumPy for high-performance array processing, and mysql-connector-python for database integration.


###File,Primary Function

signup.py,Handles new user registration and database entry.

login.py,Validates user credentials to grant access to the system.

mian.py,"The central dashboard connecting all modules (Students, Training, Detection)."

students.py,Manages student profiles and automates the facial image capture process.

training.py,Trains the AI model on the captured dataset and saves the classifier.

face_recog.py,Performs real-time facial recognition and displays student info from the database.


HOW TO RUN:-

⚙️ Installation and Setup Guide
Follow these steps to set up the environment and run the project on your local system.

1. Prerequisites
Before starting, ensure you have the following software installed:

Python (v3.10 or higher): The core language used for the project.

MySQL Workbench: Used for managing the student and user databases.

VS Code (Visual Studio Code): Recommended IDE for running and editing the Python scripts.

2. Step-by-Step Setup
Step 1: Clone or Download the Project
Download the project files to your local machine and open the folder using VS Code.

Step 2: Install Required Libraries
Open the terminal in VS Code and run the following command to install all necessary dependencies:

Bash

pip install opencv-python numpy pillow mysql-connector-python
Note: If you face issues with opencv, ensure your pip is up to date (python -m pip install --upgrade pip).

Step 3: Database Configuration
Open MySQL Workbench and log in to your local server.

Create a new database named face_recognizing:

SQL

CREATE DATABASE face_recognizing;
Create the following tables (referencing the code logic):

users table: To store signup/login credentials.

student table: To store student profiles and photo sample status.

Update Credentials: Open signup.py, login.py, face_recog.py, and students.py. Update the mysql.connector.connect parameters (host, user, password) to match your MySQL settings.

Step 4: File Path Adjustments
The project uses specific local paths for images and the Haarcascade XML file. Ensure you update the paths in mian.py, face_recog.py, and students.py to point to the correct locations on your computer.

3. How to Run the Application
Launch Login Page: Run the login.py file to start the application.

Bash

python login.py
User Registration: If it is your first time, go to the Signup page via signup.py to create an admin account.

Register Students: Log in and navigate to "Student Details" to add a new student and capture their face samples.

Train the AI: Go to the "Train Data" section and click the button to generate the classifier.xml file.

Start Recognition: Click on "Face Detector" to start the real-time recognition system.
