import cv2
import speech_recognition as sr
from ultralytics import YOLO
from gtts import gTTS
import pygame
import time
import os
import threading

# ---- Initialize ----
recognizer = sr.Recognizer()
recognizer.energy_threshold = 150  # Sensitive to low voices
model = YOLO("yolov8x.pt")

def speak(text):
    """Convert text to speech using gTTS + pygame with unique filenames."""
    print("SpeakingPy:", text)
    tts = gTTS(text=text, lang='en')

    # Unique filename (avoids permission errors)
    filename = f"temp_{int(time.time() * 1000)}.mp3"
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.quit()

    # Delete after playback
    try:
        os.remove(filename)
    except:
        pass

def listen():
    """Listen for voice commands."""
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)
            return command
        except:
            return ""

def scan_surroundings(frame=None):
    """Detect objects and their positions (left/center/right)."""
    if frame is None:
        ret, frame = cap.read()
        if not ret:
            return []

    results = model.predict(frame, verbose=False)
    objects_data = []

    frame_width = frame.shape[1]

    for box in results[0].boxes:
        cls = int(box.cls[0])
        name = results[0].names[cls]
        x_center = (box.xyxy[0][0] + box.xyxy[0][2]) / 2

        if x_center < frame_width / 3:
            position = "left"
        elif x_center < (2 * frame_width / 3):
            position = "center"
        else:
            position = "right"

        objects_data.append((name, position))

    return sorted(objects_data)

def describe_surroundings(objects):
    """Describe detected objects."""
    if not objects:
        speak("I don't see anything right now.")
        return
    description = [f"a {obj} on the {pos}" for obj, pos in objects]
    speak("I can see " + ", ".join(description))

def describe_changes(old, new):
    """Announce appearance, disappearance, and movement."""
    old_dict = {obj: pos for obj, pos in old}
    new_dict = {obj: pos for obj, pos in new}

    messages = []

    # Appeared
    for obj, pos in new:
        if obj not in old_dict:
            messages.append(f"{obj} appeared on the {pos}")

    # Disappeared
    for obj, pos in old:
        if obj not in new_dict:
            messages.append(f"{obj} disappeared from the {pos}")

    # Moved
    for obj, pos in new:
        if obj in old_dict and old_dict[obj] != pos:
            messages.append(f"{obj} moved from {old_dict[obj]} to {pos}")

    if messages:
        speak(", ".join(messages))

# ---- Live Awareness Thread ----
def live_awareness():
    global previous_objects
    previous_objects = []
    while running:
        current_objects = scan_surroundings()
        if current_objects != previous_objects:
            describe_changes(previous_objects, current_objects)
            previous_objects = current_objects
        time.sleep(1)

# ---- Main ----
speak("Live awareness with movement tracking is ready.")
cap = cv2.VideoCapture(0)
running = True

# Start live awareness in a separate thread
thread = threading.Thread(target=live_awareness, daemon=True)
thread.start()

try:
    while True:
        command = listen()

        if "what do you see" in command:
            objs = scan_surroundings()
            describe_surroundings(objs)

        elif "is there" in command:
            word = command.replace("is there", "").strip()
            objs = scan_surroundings()
            if any(o[0] == word for o in objs):
                speak(f"Yes, I can see a {word}.")
            else:
                speak(f"No, I don't see any {word} right now.")

        elif "stop" in command or "bye" in command:
            speak("Stopping live awareness. Goodbye!")
            running = False
            break

except KeyboardInterrupt:
    speak("Stopping live awareness. Goodbye!")
    running = False

cap.release()

