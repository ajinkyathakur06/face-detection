import mysql.connector
from flask import g

def get_db():
    if not hasattr(g, 'db'):
        g.db = mysql.connector.connect(
        host="localhost",
        user="attendance_user",
        password="secure_password",
        database="attendance_system"
    )

    return g.db

def close_db(e=None):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
