import cv2
from deepface import DeepFace
import random
import pygame
import tkinter as tk
import pyttsx3

# Initialize Pygame for music playback
pygame.init()
# Initialize pyttsx3 for text-to-speech
engine = pyttsx3.init()
# Load face cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Define music paths
HAPPY = ["/home/keerthireddy/face/face/music_pro/happy/1.mp3","/home/keerthireddy/face/face/music_pro/happy/2.mp3","/home/keerthireddy/face/face/music_pro/happy/3.mp3",
         "/home/keerthireddy/face/face/music_pro/happy/4.mp3","/home/keerthireddy/face/face/music_pro/happy/5.mp3","/home/keerthireddy/face/face/music_pro/happy/6.mp3",
         "/home/keerthireddy/face/face/music_pro/happy/7.mp3","/home/keerthireddy/face/face/music_pro/happy/8.mp3","/home/keerthireddy/face/face/music_pro/happy/9.mp3",
         "/home/keerthireddy/face/face/music_pro/happy/10.mp3","/home/keerthireddy/face/face/music_pro/happy/11.mp3","/home/keerthireddy/face/face/music_pro/happy/12.mp3",
         "/home/keerthireddy/face/face/music_pro/happy/16.mp3","/home/keerthireddy/face/face/music_pro/happy/15.mp3","/home/keerthireddy/face/face/music_pro/happy/14.mp3",
         "/home/keerthireddy/face/face/music_pro/happy/17.mp3","/home/keerthireddy/face/face/music_pro/happy/18.mp3","/home/keerthireddy/face/face/music_pro/happy/13.mp3"]

FEAR = ["/home/keerthireddy/face/face/music_pro/fear/1.mp3","/home/keerthireddy/face/face/music_pro/fear/2.mp3","/home/keerthireddy/face/face/music_pro/fear/3.mp3"
        "/home/keerthireddy/face/face/music_pro/fear/4.mp3","/home/keerthireddy/face/face/music_pro/fear/5.mp3","/home/keerthireddy/face/face/music_pro/fear/6.mp3"
        "/home/keerthireddy/face/face/music_pro/fear/7.mp3","/home/keerthireddy/face/face/music_pro/fear/8.mp3","/home/keerthireddy/face/face/music_pro/fear/9.mp3",
        "/home/keerthireddy/face/face/music_pro/fear/10.mp3","/home/keerthireddy/face/face/music_pro/fear/11.mp3","/home/keerthireddy/face/face/music_pro/fear/14.mp3"
        "/home/keerthireddy/face/face/music_pro/fear/12.mp3","/home/keerthireddy/face/face/music_pro/fear/13.mp3"]
        

SAD = ["/home/keerthireddy/face/face/music_pro/sad/1.mp3", "/home/keerthireddy/face/face/music_pro/sad/2.mp3", "/home/keerthireddy/face/face/music_pro/sad/3.mp3", 
       "/home/keerthireddy/face/face/music_pro/sad/4.mp3", "/home/keerthireddy/face/face/music_pro/sad/8.mp3", "/home/keerthireddy/face/face/music_pro/sad/12.mp3", 
       "/home/keerthireddy/face/face/music_pro/sad/5.mp3", "/home/keerthireddy/face/face/music_pro/sad/9.mp3", "/home/keerthireddy/face/face/music_pro/sad/13.mp3", 
       "/home/keerthireddy/face/face/music_pro/sad/6.mp3", "/home/keerthireddy/face/face/music_pro/sad/10.mp3", "/home/keerthireddy/face/face/music_pro/sad/14.mp3", 
       "/home/keerthireddy/face/face/music_pro/sad/7.mp3", "/home/keerthireddy/face/face/music_pro/sad/11.mp3"]

ANGRY = ["/home/keerthireddy/face/face/music_pro/anger/1.mp3","/home/keerthireddy/face/face/music_pro/anger/5.mp3","/home/keerthireddy/face/face/music_pro/anger/8.mp3",
         "/home/keerthireddy/face/face/music_pro/anger/2.mp3","/home/keerthireddy/face/face/music_pro/anger/6.mp3","/home/keerthireddy/face/face/music_pro/anger/9.mp3",
         "/home/keerthireddy/face/face/music_pro/anger/3.mp3","/home/keerthireddy/face/face/music_pro/anger/7.mp3","/home/keerthireddy/face/face/music_pro/anger/10.mp3",
         "/home/keerthireddy/face/face/music_pro/anger/4.mp3",]

         

DISGUST = ["/home/keerthireddy/face/face/music_pro/disgust/1.mp3","/home/keerthireddy/face/face/music_pro/disgust/4.mp3","/home/keerthireddy/face/face/music_pro/disgust/6.mp3",
           "/home/keerthireddy/face/face/music_pro/disgust/2.mp3","/home/keerthireddy/face/face/music_pro/disgust/5.mp3","/home/keerthireddy/face/face/music_pro/disgust/3.mp3"]


SURPRISE = ["/home/keerthireddy/face/face/music_pro/surprise/1.mp3","/home/keerthireddy/face/face/music_pro/surprise/2.mp3","/home/keerthireddy/face/face/music_pro/surprise/3.mp3"]
            

NEUTRAL = ["/home/keerthireddy/face/face/music_pro/neutral/1.mp3","/home/keerthireddy/face/face/music_pro/neutral/5.mp3","/home/keerthireddy/face/face/music_pro/neutral/9.mp3",
           "/home/keerthireddy/face/face/music_pro/neutral/2.mp3","/home/keerthireddy/face/face/music_pro/neutral/6.mp3","/home/keerthireddy/face/face/music_pro/neutral/10.mp3",
           "/home/keerthireddy/face/face/music_pro/neutral/3.mp3","/home/keerthireddy/face/face/music_pro/neutral/7.mp3","/home/keerthireddy/face/face/music_pro/neutral/11.mp3",
           "/home/keerthireddy/face/face/music_pro/neutral/4.mp3","/home/keerthireddy/face/face/music_pro/neutral/8.mp3",]
           

# Function to detect emotions
def detect_emotion():
    # Start capturing video
    cap = cv2.VideoCapture(0)
    emotion = None

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Convert frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Convert grayscale frame to RGB format
        rgb_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2RGB)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            # Extract the face ROI (Region of Interest)
            face_roi = rgb_frame[y:y + h, x:x + w]

            # Perform emotion analysis on the face ROI
            result = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)

            # Determine the dominant emotion
            emotion = result[0]['dominant_emotion']

            # Draw rectangle around face and label with predicted emotion
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, f"Emotion: {emotion}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

        # Display the resulting frame
        cv2.imshow('Real-time Emotion Detection', frame)

        # Press 'q' to exit and play music
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close all windows
    cap.release()
    cv2.destroyAllWindows()

    # Speak out the detected emotion
    speak_emotion(emotion)

    # Play music based on detected emotion
    play_music(emotion)

# Function to speak out the detected emotion
def speak_emotion(emotion):
    engine.say(f"The detected emotion is {emotion}")
    engine.runAndWait()

# Function to play music based on emotion
def play_music(emotion):
    # Dictionary to map emotions to corresponding music lists
    emotions_music = {
        "happy": HAPPY,
        "fear": FEAR,
        "sad": SAD,
        "angry": ANGRY,
        "disgust": DISGUST,
        "surprise": SURPRISE,
        "neutral": NEUTRAL
    }

    if emotion in emotions_music:
        random_song = random.choice(emotions_music[emotion])
        pygame.mixer.music.load(random_song)
        pygame.mixer.music.play()

# Function to stop music playback
def stop_music():
    pygame.mixer.music.stop()

# Create the main Tkinter window
root = tk.Tk()
root.title("Emotion Detection and Music Player")

# Set the window size
root.geometry("500x200")

# Button to start emotion detection and music playback
start_detection_btn = tk.Button(root, text="Start Emotion Detection", command=detect_emotion)
start_detection_btn.pack(pady=10)

# Button to stop music playback
stop_music_btn = tk.Button(root, text="Stop Music", command=stop_music)
stop_music_btn.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
