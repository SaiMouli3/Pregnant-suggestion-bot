"""
MamaCare Assistant - A personalized pregnancy support chatbot.

This package provides a web-based interface for expecting mothers to get
personalized advice, tips, and support during their pregnancy journey.
"""

__version__ = '1.0.0'
__author__ = 'Your Name <your.email@example.com>'
__license__ = 'MIT'

# Import main components
from .app import app  # noqa: F401
from .graph import app as graph_app  # noqa: F401

# Initialize logging
import logging
from logging.handlers import RotatingFileHandler
import os

# Create logs directory if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        RotatingFileHandler(
            'logs/mamacare.log',
            maxBytes=1024*1024,  # 1MB
            backupCount=5
        ),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def get_version():
    """Return the current version of the package."""
    return __version__

def create_app(config_name=None):
    """Application factory function.
    
    Args:
        config_name (str, optional): The configuration to use. Defaults to None.
        
    Returns:
        Flask: The configured Flask application instance.
    """
    from flask import Flask
    from .config import get_config
    
    # Create and configure the app
    app = Flask(__name__)
    
    # Apply configuration
    app.config.from_object(get_config(config_name))
    
    # Initialize extensions
    from flask_cors import CORS
    CORS(app)
    
    # Register blueprints
    from .api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')
    
    # Register error handlers
    from .errors import init_error_handlers
    init_error_handlers(app)
    
    # Initialize database
    from .extensions import db
    db.init_app(app)
    
    # Add CLI commands
    from .commands import init_commands
    init_commands(app)
    
    return app
