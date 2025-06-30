"""
Database models for the MamaCare Assistant application.
"""
from datetime import datetime
from ..extensions import db

class Question(db.Model):
    """Database model for storing user questions."""
    __tablename__ = 'questions'
    
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    trimester = db.Column(db.String(20))
    diet = db.Column(db.String(20))
    mood = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    responses = db.relationship('Response', backref='question', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        """Convert the model to a dictionary."""
        return {
            'id': self.id,
            'text': self.text,
            'trimester': self.trimester,
            'diet': self.diet,
            'mood': self.mood,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'response_count': len(self.responses)
        }

class Response(db.Model):
    """Database model for storing AI responses."""
    __tablename__ = 'responses'
    
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    answer = db.Column(db.Text, nullable=False)
    daily_tip = db.Column(db.Text)
    mood_response = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        """Convert the model to a dictionary."""
        return {
            'id': self.id,
            'question_id': self.question_id,
            'answer': self.answer,
            'daily_tip': self.daily_tip,
            'mood_response': self.mood_response,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class Reminder(db.Model):
    """Database model for user reminders."""
    __tablename__ = 'reminders'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    text = db.Column(db.String(200), nullable=False)
    due_date = db.Column(db.DateTime)
    is_completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        """Convert the model to a dictionary."""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'text': self.text,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'is_completed': self.is_completed,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
