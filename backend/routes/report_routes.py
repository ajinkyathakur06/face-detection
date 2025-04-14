from flask import Blueprint, request, jsonify
from models.attendance import Attendance

report_bp = Blueprint('report', __name__)

@report_bp.route('/attendance_report', methods=['GET'])
def generate_report():
    session_id = request.args.get('session_id')
    attendance = Attendance.get_attendance_by_session(session_id)
    return jsonify(attendance), 200
