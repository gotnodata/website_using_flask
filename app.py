# Main application file to set up and run the Flask app.
from flask import Flask
from models import db
from config import Config
from blueprints.auth import auth_bp
from blueprints.main import main_bp

app = Flask(__name__)
app.config.from_object(Config)

# Initialize database with app
db.init_app(app)

# Register blueprints
app.register_blueprint(main_bp)
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

    