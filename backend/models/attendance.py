from utils.database import get_db

class Attendance:
    def __init__(self, session_id, user_id):
        self.session_id = session_id
        self.user_id = user_id

    def save(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO attendance (session_id, user_id) VALUES (%s, %s)', (self.session_id, self.user_id))
        db.commit()
        cursor.close()

    @staticmethod
    def get_attendance_by_session(session_id):
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute('SELECT users.username, attendance.attendance_time FROM attendance JOIN users ON attendance.user_id = users.id WHERE attendance.session_id = %s', (session_id,))
        attendance = cursor.fetchall()
        cursor.close()
        return attendance
