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

# Create the main Tkinter window
root = tk.Tk()
root.title("Webcam Preview")

# Create a label for the video frame
video_label = tk.Label(root)
video_label.pack()

# Exit button
exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack(pady=5)

# OpenCV video capture
cap = cv2.VideoCapture(0)

def update_frame():
    ret, frame = cap.read()
    if ret:
        # Mirror the frame
        frame = cv2.flip(frame, 1)

        # Resize the frame to 200x200
        frame = cv2.resize(frame, (680, 400))

        # Convert to RGB and then to ImageTk
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)

        # Show frame in label
        video_label.imgtk = imgtk
        video_label.configure(image=imgtk)

    # Repeat every 10 ms
    video_label.after(10, update_frame)

# Start updating frames
update_frame()

# Start the Tkinter event loop
root.mainloop()

# Release camera after GUI closes
cap.release()
cv2.destroyAllWindows()