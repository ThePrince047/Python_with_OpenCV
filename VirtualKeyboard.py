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
import cvzone
from cvzone.HandTrackingModule import HandDetector

root = tk.Tk()
root.title("Webcam Preview with Hand Landmark Detection")

video_label = tk.Label(root)
video_label.pack()

exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack(pady=10)
exit_button.config(font=("Arial", 12))

cap = cv2.VideoCapture(0)  # Capture video from webcam

# Check if webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not access the webcam.")
    exit()

detector = HandDetector(max_hands=1)  # Initialize the hand detector

def update_frame():
    ret, frame = cap.read()  # Read frame from webcam
    if ret:
        # Flip the frame horizontally (mirror effect)
        frame = cv2.flip(frame, 1)

        # Detect hands and landmarks
        hands, frame = detector.findHands(frame)

        # Draw hand landmarks
        if hands:
            hand = hands[0]  # Process the first hand (if detected)
            landmarks = hand['lmList']  # Get the list of landmarks

            # Draw circles on each hand landmark
            for lm in landmarks:
                x, y = lm[0], lm[1]
                cv2.circle(frame, (x, y), 5, (0, 255, 0), cv2.FILLED)

        # Resize frame for Tkinter
        frame = cv2.resize(frame, (700, 500))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)

        # Update the video label with the new frame
        video_label.imgtk = imgtk
        video_label.configure(image=imgtk)

    # Repeat this function every 10 milliseconds
    video_label.after(10, update_frame)

update_frame()
root.mainloop()

cap.release()  # Release the webcam when done
cv2.destroyAllWindows()  # Destroy all OpenCV windows








# import cv2
# import tkinter as tk
# from PIL import Image, ImageTk

# root = tk.Tk()
# root.title("Webcam Preview")

# video_label = tk.Label(root)
# video_label.pack()

# exit_button = tk.Button(root, text="Exit", command=root.destroy)
# exit_button.pack(pady=10)
# exit_button.config(font=("Arial", 12))
# cap = cv2.VideoCapture(0)

# def update_frame():
#     ret, frame = cap.read()
#     if ret:
#         frame = cv2.flip(frame, 1)
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