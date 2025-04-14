from flask import Blueprint, request, jsonify
import face_recognition
import cv2
from utils.face_recognition_utils import capture_image, recognize_face

face_bp = Blueprint('face', __name__)

@face_bp.route('/capture', methods=['POST'])
def capture():
    image_path = capture_image()
    return jsonify({"message": "Image captured successfully!", "image_path": image_path})


@face_bp.route('/recognize', methods=['POST'])
def recognize():
    data = request.get_json()
    image_path = data.get('image_path')
    
    recognition_result = recognize_face(image_path)
    
    if recognition_result:
        return jsonify({"message": "Face recognized!", "student": recognition_result}), 200
    else:
        return jsonify({"message": "No face recognized!"}), 400
