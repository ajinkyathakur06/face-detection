from utils.database import get_db

class Session:
    def __init__(self, session_name, session_date):
        self.session_name = session_name
        self.session_date = session_date

    def save(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO sessions (session_name, session_date) VALUES (%s, %s)', (self.session_name, self.session_date))
        db.commit()
        cursor.close()

    @staticmethod
    def get_all_sessions():
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute('SELECT * FROM sessions')
        sessions = cursor.fetchall()
        cursor.close()
        return sessions
