import os
import requests
from flask import request, jsonify
from src.models.models import db, User
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get the microservice URL from environment variables
QUERY_MICROSERVICE_URL = os.getenv('QUERY_MICROSERVICE_URL')

# Route to delete user
def delete_user(id):
    try:
        # Make a request to the microservice to get the user by their ID
        response = requests.get(f'{QUERY_MICROSERVICE_URL}/{id}')
        
        # Check if the user exists
        if response.status_code != 200:
            return jsonify({'error': 'User not found'}), 404

        user = User.query.get(id)
        
        # Check if the user exists in the database
        if not user:
            return jsonify({'error': 'User not found in local database'}), 404

        # Delete the user
        db.session.delete(user)
        db.session.commit()
        
        return jsonify({'message': 'User deleted successfully'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400
