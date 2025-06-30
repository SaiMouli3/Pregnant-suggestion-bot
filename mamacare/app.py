"""
MamaCare Assistant - Flask Application

This module initializes the Flask application and defines the API endpoints.
"""
import os
import logging
from datetime import datetime
from functools import wraps
from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_cors import CORS
from graph import app as graph_app
from config import get_config, model

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('mamacare.log')
    ]
)
logger = logging.getLogger(__name__)

# Initialize Flask application
app = Flask(__name__)
app.config.from_object(get_config())

# Enable CORS if needed
CORS(app, resources={r"/*": {"origins": "*"}})

# Error handlers
@app.errorhandler(400)
def bad_request(error):
    """Handle 400 errors."""
    return jsonify({
        'status': 'error',
        'message': 'Bad request',
        'error': str(error)
    }), 400

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({
        'status': 'error',
        'message': 'Resource not found',
        'error': str(error)
    }), 404

@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors."""
    logger.error(f"Server error: {str(error)}", exc_info=True)
    return jsonify({
        'status': 'error',
        'message': 'Internal server error',
        'error': str(error) if app.debug else 'An internal error occurred.'
    }), 500

# Helper functions
def validate_request_data(data, required_fields):
    """Validate that all required fields are present in the request data."""
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")
    return True

# Routes
@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    """Handle chat requests."""
    try:
        # Validate request
        data = request.get_json()
        if not data:
            return jsonify({
                'status': 'error',
                'message': 'No data provided'
            }), 400
            
        # Validate required fields
        required_fields = ['question', 'trimester', 'diet', 'mood']
        try:
            validate_request_data(data, required_fields)
        except ValueError as e:
            return jsonify({
                'status': 'error',
                'message': str(e)
            }), 400
        
        # Log the request
        logger.info(f"New question received: {data['question']}")
        logger.info(f"Context - Trimester: {data['trimester']}, "
                   f"Diet: {data['diet']}, Mood: {data['mood']}")
        
        # Process with the graph app
        result = graph_app.invoke({
            "user_input": data['question'],
            "trimester": data['trimester'],
            "diet": data['diet'],
            "mood": data['mood']
        })
        
        # Log successful response
        logger.info("Successfully generated response")
        
        # Return the response
        return jsonify({
            'status': 'success',
            'response': {
                'qa_answer': result.get('qa_answer', ''),
                'daily_tip': result.get('daily_tip', ''),
                'reminders': result.get('reminders', []),
                'mood_response': result.get('mood_response', '')
            }
        })
        
    except Exception as e:
        # Log the error
        logger.error(f"Error processing request: {str(e)}", exc_info=True)
        
        # Return error response
        return jsonify({
            'status': 'error',
            'message': str(e) if app.debug else 'An error occurred while processing your request.'
        }), 500

# Health check endpoint
@app.route('/health')
def health_check():
    """Health check endpoint for monitoring."""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'version': app.config.get('VERSION', '1.0.0')
    })

# API documentation
@app.route('/api/docs')
def api_docs():
    """API documentation page."""
    return redirect('https://documenter.getpostman.com/view/your-api-docs', code=302)

if __name__ == '__main__':
    # Create uploads directory if it doesn't exist
    upload_dir = app.config.get('UPLOAD_FOLDER', 'uploads')
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    
    # Run the application
    app.run(
        host=os.getenv('FLASK_RUN_HOST', '0.0.0.0'),
        port=int(os.getenv('FLASK_RUN_PORT', 5000)),
        debug=app.config.get('DEBUG', False)
    )
