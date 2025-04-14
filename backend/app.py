from flask import Flask
from flask_cors import CORS
from routes.auth_routes import auth_bp
from routes.face_recognition_routes import face_bp
from routes.session_routes import session_bp
from routes.report_routes import report_bp
from utils.database import close_db

app = Flask(__name__)

CORS(app)

# Application Configuration
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a strong secret key

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(face_bp, url_prefix='/face')
app.register_blueprint(session_bp, url_prefix='/session')
app.register_blueprint(report_bp, url_prefix='/report')

# Register the teardown function
@app.teardown_appcontext
def teardown_db(exception):
    close_db(exception)

@app.route('/')
def home():
    return "Face Attendance System Backend is Running!"

if __name__ == '__main__':
    app.run(debug=True)
