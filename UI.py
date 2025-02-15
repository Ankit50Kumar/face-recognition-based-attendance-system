import tkinter
import tkinter as tk
from tkinter import simpledialog, messagebox
import subprocess

import self as self


class FaceRecognitionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition GUI")

        self.student_names = []

        self.input_button = tk.Button(root, text="Input Student Name", command=self.input_student_name)
        self.input_button.pack(pady=20)

        self.scan_button = tk.Button(root, text="Scan Face", command=self.scan_face)
        self.scan_button.pack(pady=20)

    def input_student_name(self):
        student_name = simpledialog.askstring("Input Student Name", "Enter student name:")
        if student_name:
            self.student_names.append(student_name)
            messagebox.showinfo("Success", f"{student_name} added to the list.")

    def scan_face(self):
        if not self.student_names:
            messagebox.showwarning("Warning", "Please input student names first.")
        else:
            # Save student names to a temporary file
            with open("temp_student_names.txt", "w") as f:
                for name in self.student_names:
                    f.write(name + "\n")

            # Call the face recognition script
            subprocess.run(["python", "C:/Users/DELL/OneDrive/Desktop/face/f1.py"])

            # Optionally, you can read the attendance from the CSV file and display it to the user
            # Add your code here

if __name__ == "__main__":
    root = tk.Tk()
    app = FaceRecognitionGUI(root)
    root.mainloop()
