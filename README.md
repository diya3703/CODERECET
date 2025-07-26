# CODERECET

## Project Repository

### Team Name :Twync
### Team Members :Ann Joy and Diya Baby
### Project Description
EchoEyes is a wearable AI-powered smart assistant designed to enhance the mobility and independence of visually impaired individuals. Combining obstacle detection, object recognition, and voice feedback, the system offers real-time environmental awareness through sound.

The device senses nearby obstacles using ultrasonic sensor and alerts the user through a buzzer or voice prompts. A camera module captures visual information, which is processed using AI models to recognize objects, text, or signs. The results are then converted to speech using a text-to-speech engine, enabling the user to hear what’s around them in real time.

While this prototype currently runs on a laptop, the same AI code can be seamlessly ported to a mobile app or a Raspberry Pi–based embedded system for real-world deployment. In a full-fledged product, the user would simply wear a small smart camera, such as one mounted on glasses connected to a pocket-sized processor or their smartphone, making the device compact, wearable, and suitable for daily use without relying on bulky equipment.

By transforming visual cues into sound, EchoEyes empowers the visually impaired to explore their surroundings with greater confidence, independence, and dignity.

## Technical Details

### Technologies/Components Used

## For Software:
Languages used
Python : Main programming language for AI, computer vision, and text-to-speech 
C/C++ : Used in Arduino code for controlling ultrasonic sensor and buzzer 

Frameworks used
PyTorch  Deep learning framework used to run YOLOv8 models 
Ultralytics YOLO High-level wrapper over PyTorch to simplify object detection 
Libraries used

Libraries Used
 opencv-python Access webcam, process image frames 
 ultralytics For running YOLOv8 object detection 
torch, torchvision, torchaudio Core PyTorch packages for deep learning 
 pyttsx3 Text-to-speech engine to read detected objects aloud 
pytesseract OCR (text reading) from images 
 Pillow (PIL) For image manipulation in OCR module 
numpy Numerical operations on image arrays 

Tools Used
 Python 3.x Programming environment for all AI modules 
Arduino IDE  Writing and uploading code to Arduino UNO 
Jupyter Notebook  For quick testing and visualization of detection 
Tesseract OCR Engine  Backend engine for text recognition 
VS Code / PyCharm   For writing and testing Python code efficiently 
Command Prompt / Terminal To install packages, run scripts, and interact with Git 
Git Version control and uploading project to GitHub 
 GitHub Hosting and sharing your codebase with others 

## For Hardware:
Arduino UNO       :Controls ultrasonic & buzzer    
HC-SR04 Sensor    :Measures obstacle distance      
Buzzer            : Gives physical proximity alerts 
USB Webcam        :Captures visual data            
Laptop or Pi      : Runs AI code                    
Breadboard        : For connecting sensors          
Jumper Wires      : For connections                 
## Implementation

## For Software:

### Installation
pip install opencv-python numpy pyttsx3
pip install torch torchvision torchaudio 
pip install ultralytics
pip install easyocr

### Run
python filename.py :to run the program
Ctrl +C to exit the program

### Project Documentation

### Screenshots (Add at least 3)
<img width="1897" height="1107" alt="image" src="https://github.com/user-attachments/assets/85264716-ec5a-48c6-9eca-cb47b896658f" /><img width="1907" height="1104" alt="image" src="https://github.com/user-attachments/assets/df38a286-9c5f-479c-96e2-078e5e6579f3" /><img width="1913" height="1109" alt="image" src="https://github.com/user-attachments/assets/d8aed3d4-7a1e-4f7e-b50d-2553e181a7b3" /><img width="1918" height="1111" alt="image" src="https://github.com/user-attachments/assets/48b2861c-022b-4c35-821c-7423a104e25e" /><img width="1823" height="792" alt="image" src="https://github.com/user-attachments/assets/9b2d1c75-0252-4463-9382-fc6ca83e2085" /><img width="1844" height="839" alt="image" src="https://github.com/user-attachments/assets/ee7b0729-0e4b-44b7-9b8e-8272d82f352e" />










### Diagrams
Workflow(Add your workflow/architecture diagram here) Add caption explaining your workflow

## For Hardware:

### Schematic & Circuit
Circuit(Add your circuit diagram here) Add caption explaining connections
Schematic(Add your schematic diagram here) Add caption explaining the schematic

### Build Photos

Arduino UNO,HC-SR04 Sensor,Buzzer,USB Webcam,Laptop,Breadboard ,Jumper Wires  
<img width="618" height="822" alt="image" src="https://github.com/user-attachments/assets/d038a585-6fb4-4949-a4d8-dad633d6d1c4" />
Arduino Build Steps
1. Place Components. Insert HC-SR04 sensor and buzzer onto the breadboard.

2. Connect HC-SR04 Sensor to Arduino

VCC → Arduino 5V
GND → Arduino GND
TRIG → Arduino Digital Pin 9
ECHO → Arduino Digital Pin 10

3. Connect Buzzer to Arduino

Positive (+) → Arduino Digital Pin 8
Negative (–) → Arduino GND (via breadboard)

4. Power the Arduino. Connect the Arduino to your laptop using a USB cable.

5. Open Arduino IDE. Launch the Arduino IDE on your computer.

6. Write or Paste Code. Write or paste the distance detection + buzzer alert code.

 7. Select Board and Port

 Go to Tools > Board > Arduino Uno
Go to Tools > Port > COMx (select the right port)

8. Upload the Code
Click the Upload button (right arrow icon).

9. Test the Setup
Place an object in front of the sensor and verify:
 The buzzer beeps when the object is too close.

10. Stop Execution (if needed)
Press the reset button on Arduino or unplug the USB.

<img width="371" height="438" alt="image" src="https://github.com/user-attachments/assets/7c6b0505-bf9c-4ca2-bf27-45c781015cab" />

The final build of EchoEyes is a compact, wearable smart assistant designed to aid visually impaired individuals by converting visual and spatial information into sound. It integrates two main systems: a software module running on a laptop that uses a camera and AI-based object detection (YOLOv8) to identify objects and read them aloud using text-to-speech, and a hardware module built on Arduino that uses an ultrasonic sensor (HC-SR04) to detect nearby obstacles and alert the user through a buzzer. Together, these systems provide real-time awareness of surroundings, enabling users to safely and independently navigate environments with enhanced confidence and dignity.

### Project Demo

### Video
[Add your demo video link here] Explain what the video demonstrates

## Team Contributions
Ann Joy:Library Setup and Dependency Management.Object Detection Module,Voice Feedback
Diya Baby:Arduino Setup,Breadboard wiring,software Hardware integration,Audio Testing.
Joint Responsibilities:Documentation and Github upload,demo video and presentation.
