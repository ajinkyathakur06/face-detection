import cv2
import face_recognition

def capture_image():
    video_capture = cv2.VideoCapture(0)
    
    if not video_capture.isOpened():
        print("Could not open webcam")
        return None
    
    ret, frame = video_capture.read()
    video_capture.release()

    if ret:
        filename = "captured_image.jpg"
        cv2.imwrite(filename, frame)
        return filename
    return None

def recognize_face(image_path):
    # Load the image
    image = face_recognition.load_image_file(image_path)
    face_encodings = face_recognition.face_encodings(image)
    
    if face_encodings:
        # Here you should compare the face encodings with the ones in the database
        return {"student_name": "John Doe"}  # Just a mock response
    return None
