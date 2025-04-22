import tkinter as tk
from tkinter import Label, Button, Entry, messagebox
from PIL import Image, ImageTk
import cv2
import backend


def start_attendance():
    global video_capture, course_name, teacher_name, f, lnwritter, filename, recorded_students
    course_name = course_entry.get()
    teacher_name = teacher_entry.get()
    if course_name and teacher_name:
        f, lnwritter, filename = backend.initialize_attendance_file(course_name, teacher_name)
        recorded_students = set()
        messagebox.showinfo("Attendance System", f"Attendance started for {course_name} by {teacher_name}")
        update_frame()
    else:
        messagebox.showerror("Error", "Please enter course name and teacher name")


def update_frame():
    global video_capture
    _, frame = video_capture.read()
    name = backend.recognize_faces(frame, known_face_encodings, known_face_names, recorded_students, lnwritter,
                                   course_name, teacher_name)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, f"{name} Present", (10, 100), font, 1.5, (255, 0, 0), 3, cv2.LINE_AA)

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=img)
    video_label.imgtk = imgtk
    video_label.configure(image=imgtk)
    video_label.after(10, update_frame)


def close_application():
    video_capture.release()
    cv2.destroyAllWindows()
    f.close()
    root.destroy()
    messagebox.showinfo("Attendance System", "Attendance session closed.")


# Initialize components
video_capture = cv2.VideoCapture(0)
known_face_encodings, known_face_names = backend.load_known_faces()
recorded_students = set()
course_name = ""
teacher_name = ""

# Create GUI
root = tk.Tk()
root.title("Attendance System")
root.geometry("500x400")
root.configure(bg="#f0f0f0")

label = Label(root, text="Face Recognition Attendance System", font=("Arial", 16, "bold"), bg="#f0f0f0")
label.pack(pady=10)

course_label = Label(root, text="Course Name:", font=("Arial", 12), bg="#f0f0f0")
course_label.pack()
course_entry = Entry(root, font=("Arial", 12), justify="center")
course_entry.pack(pady=5)

teacher_label = Label(root, text="Teacher Name:", font=("Arial", 12), bg="#f0f0f0")
teacher_label.pack()
teacher_entry = Entry(root, font=("Arial", 12), justify="center")
teacher_entry.pack(pady=5)

start_button = Button(root, text="Start Attendance", command=start_attendance, font=("Arial", 12, "bold"), bg="green",
                      fg="white", width=20)
start_button.pack(pady=10)

video_label = Label(root, bg="#f0f0f0")
video_label.pack()

exit_button = Button(root, text="Stop Attendance", command=close_application, font=("Arial", 12, "bold"), bg="red", fg="white",
                     width=20)
exit_button.pack(pady=10)

root.mainloop()

print(f"Attendance saved in {filename}")
