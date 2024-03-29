import threading

import cv2

from deepface import DeepFace

class FaceRecognition:

    def __init__(self):
        self.name = 'Face Recognition module'

        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
        self.counter = 0

        self.face_match = False

        self.reference_img = cv2.imread('reference.jpg')

    def check_face(self, frame):

        try:
            if DeepFace.verify(frame, self.reference_img.copy())['verified']:
                
                self.face_match = True
            
            else:
                self.face_match = False
            
        except ValueError:

            self.face_match = False

    def main_job(self):


        while True:
            ret, frame = self.cap.read()

            if ret:
                if self.counter % 30 == 0:
                    
                    try:
                        threading.Thread(target=self.check_face, args=(frame.copy(), )).start()
                    
                    except ValueError:
                        pass

                self.counter += 1

                if face_match:
                    cv2.putText(frame, "MATCH", (20, 450), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (0, 255, 0), 3)

                else:

                    cv2.putText(frame, "NO MATCH", (20, 450), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (0, 0, 255), 3)

                cv2.imshow("video", frame)


            key = cv2.waitKey(1)

            if key == ord("q"):
                break
        
        cv2.destroyAllWindows()