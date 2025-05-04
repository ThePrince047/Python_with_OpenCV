# import cv2
# import tkinter as tk
# from PIL import Image, ImageTk
# import cvzone
# from cvzone.HandTrackingModule import HandDetector

# root = tk.Tk()
# root.title("Webcam Preview with Hand Landmark Detection")

# video_label = tk.Label(root)
# video_label.pack()

# exit_button = tk.Button(root, text="Exit", command=root.destroy)
# exit_button.pack(pady=10)
# exit_button.config(font=("Arial", 12))

# cap = cv2.VideoCapture(0) 

# # Check if webcam is opened correctly
# if not cap.isOpened():
#     print("Error: Could not access the webcam.")
#     exit()

# detector = HandDetector()

# def update_frame():
#     ret, frame = cap.read() 
#     if ret:        
#         frame = cv2.flip(frame, 1)
#         hands, frame = detector.findHands(frame)
#         if hands:
#             hand = hands[0] 
#             landmarks = hand['lmList']

#             for lm in landmarks:
#                 x, y = lm[0], lm[1]
#                 cv2.circle(frame, (x, y), 5, (0, 255, 0), cv2.FILLED)

#         frame = cv2.resize(frame, (700, 500))
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         img = Image.fromarray(frame)
#         imgtk = ImageTk.PhotoImage(image=img)

#         video_label.imgtk = imgtk
#         video_label.configure(image=imgtk)
#     video_label.after(10, update_frame)

# update_frame()
# root.mainloop()

# cap.release()
# cv2.destroyAllWindows()

import cv2
import tkinter as tk
from PIL import Image, ImageTk
from cvzone.HandTrackingModule import HandDetector

# Initialize main window
root = tk.Tk()
root.title("Hand Landmark Detection")

# Video display label
video_label = tk.Label(root)
video_label.pack()

# Exit button
exit_button = tk.Button(root, text="Exit", font=("Arial", 12), command=root.destroy)
exit_button.pack(pady=10)

# Webcam capture
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not access the webcam.")
    root.destroy()

# Hand detector
detector = HandDetector()

# Update video frame
def update_frame():
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 1)
        hands, frame = detector.findHands(frame)

        if hands:
            for lm in hands[0]['lmList']:
                cv2.circle(frame, (lm[0], lm[1]), 5, (0, 255, 0), cv2.FILLED)

        frame = cv2.resize(frame, (700, 500))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        imgtk = ImageTk.PhotoImage(Image.fromarray(frame))
        video_label.imgtk = imgtk
        video_label.configure(image=imgtk)

    video_label.after(10, update_frame)

# Handle closing properly
def on_close():
    cap.release()
    cv2.destroyAllWindows()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)
update_frame()
root.mainloop()
cap.release()
cv2.destroyAllWindows()