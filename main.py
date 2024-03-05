import threading

import cv2

from deepface import DeepFace

from face_recognition_service import FaceRecognition


def main():
    
    face_rec = FaceRecognition()

    face_rec.main_job()
   

if __name__ == "__main__":
    main()
