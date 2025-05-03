# import cv2
# cap = cv2.VideoCapture(0)

# if not cap.isOpened():
#     print("Error: Could not open video device.")
#     exit()

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("Error: Could not read frame.")
#         break

#     mirror_frame=cv2.flip(frame, 1)  
#     small_frame = cv2.resize(mirror_frame, (680, 400))
#     cv2.imshow("Camera Preview",small_frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

import cv2
import tkinter as tk
from PIL import Image, ImageTk
#from cvzone import HandTrackingModule

#import cvzone

root = tk.Tk()
root.title("Webcam Preview")

video_label = tk.Label(root)
video_label.pack()

exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack(pady=15)
exit_button.sized = (10, 2)
exit_button.config(font=("Arial", 12))
cap = cv2.VideoCapture(0)

def update_frame():
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 1)
        frame = cv2.resize(frame, (700, 500))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)

        video_label.imgtk = imgtk
        video_label.configure(image=imgtk)
    video_label.after(10, update_frame)

update_frame()
root.mainloop()
cap.release()
cv2.destroyAllWindows()