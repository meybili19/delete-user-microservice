from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

# Create SQLAlchemy instance
db = SQLAlchemy()

#UserModel
class User(db.Model):
 __tablename__ = 'Users'
 id = db.Column(db.Integer, primary_key=True)
 name = db.Column(db.String(50), nullable=False)
 email = db.Column(db.String(100), unique=True, nullable=False)
 password = db.Column(db.String(255), nullable=False)
 created_in = db.Column(db.DateTime, default=text('GETDATE()'), nullable=False)