from utils.database import get_db

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def save(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (self.username, self.password))
        db.commit()
        cursor.close()

    @staticmethod
    def get_user_by_username(username):
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()
        cursor.close()
        return user
