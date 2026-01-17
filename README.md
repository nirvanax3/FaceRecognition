# **FaceRecognition**

A simple face‑recognition application using Python.

## Description
This project provides a basic setup to:
1. Encode known faces from images.
2. Recognize faces in live camera feed or images.
3. Label recognized faces and optionally mark unknowns.

## Features
1. Face encoding generation.
2. Real‑time face detection and recognition.
3. Flexible to add new people by adding their images and regenerating encodings.
4. Minimal dependencies and simple workflow

## Requirements
1. Python 3.x
2. Libraries (install via pip):
   ```bash
   pip install opencv-python face_recognition numpy
  (and any others required by this code)
  
4. A working webcam (if using live feed) or sample images.
   
6. A folder structure roughly:
  * Images/ → holds sample images of people.
  * Resources/ → holds other required assets (if any).
  * EncodeGenerator.py → generates the face encodings.
  * main.py → runs the recognition process.

## Usage
1. Place images of known persons in the Images/ folder (one folder per person, or images named accordingly).
2. Run:
   ```bash
   python EncodeGenerator.py  
3. Run:
   ```bash
   python main.py  
  This will open the webcam (or process images) and attempt to recognize faces based on the encodings.
  
  4. When a known face is detected, their name will be shown. Unknown faces will be flagged accordingly.

## Folder Structure
    FaceRecognition/
    │  
    ├─ Images/  
    │   ├─ Person1/  
    │   │   ├─ img1.jpg  
    │   │   └─ …  
    │   ├─ Person2/  
    │   └─ …  
    │  
    ├─ Resources/  
    │   └─ …  
    │  
    ├─ EncodeGenerator.py  
    └─ main.py


## How It Works
1. EncodeGenerator.py loads each image, detects the face(s), computes face encodings using the face_recognition library, and stores them (e.g., in a pickle file).
2. main.py loads the encodings and then, via webcam or image input, captures frames, detects faces, computes encoding of each face, compares with known encodings, and if match found within threshold, labels the
   face with that person’s name; else marks as “Unknown”.
3. The process uses opencv-python for video capture and drawing annotations, and face_recognition for the heavy‑lifting of detection/encoding/comparison.

## Customization
1. Adjust recognition threshold to make matching more/less strict.
2. Add support for multiple faces in one frame.
3. Add logging, alerts, or storing of unrecognized faces.
4. Export annotated video or image results.
5. Deploy in a GUI, web app, or other interface.

## Limitations

1. Simple system—does not scale to thousands of people without modification and optimization.
2. Accuracy depends on lighting, pose, image quality of both known and unknown faces.
3. Privacy and ethical considerations must be respected (consent, storage of biometric data, etc.).
4. Not designed for robust security applications out‑of‑the‑box.
   
