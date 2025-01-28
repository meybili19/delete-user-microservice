from flask import Flask
from flask_cors import CORS
from src.config.config import Config
from src.models.models import db
from src.routes.routes import delete_user

# Create the application
app = Flask(__name__)

CORS(app)
# Application configuration
app.config.from_object(Config)

# Initialize the database
db.init_app(app)

# Register the delete user route
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user_route(id):
    return delete_user(id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
