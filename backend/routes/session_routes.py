from flask import Blueprint, request, jsonify
from models.session import Session
from models.attendance import Attendance

session_bp = Blueprint('session', __name__)

@session_bp.route('/create', methods=['POST'])
def create_session():
    data = request.get_json()
    session_name = data.get('session_name')
    session_date = data.get('session_date')

    session = Session(session_name, session_date)
    session.save()

    return jsonify({"message": "Session created successfully!"}), 201


@session_bp.route('/sessions', methods=['GET'])
def get_sessions():
    sessions = Session.get_all_sessions()
    return jsonify(sessions), 200


@session_bp.route('/mark_attendance', methods=['POST'])
def mark_attendance():
    data = request.get_json()
    session_id = data.get('session_id')
    user_id = data.get('user_id')

    attendance = Attendance(session_id, user_id)
    attendance.save()

    return jsonify({"message": "Attendance marked successfully!"}), 201
