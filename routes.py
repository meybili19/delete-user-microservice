585 / 5.000
from flask import jsonify
from models import db, User

# Route to delete user by ID
def delete_user(id):
    try:
    # Search for the user by its ID
        user = User.query.get(id)

        # Check if the user exists
        if not user:
            return jsonify({'error': 'User not found'}), 404

        # Delete the user
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400