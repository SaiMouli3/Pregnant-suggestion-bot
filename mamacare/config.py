"""
Configuration settings for the MamaCare Assistant application.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path(__file__).parent / '.env'
load_dotenv(env_path)

# Application settings
class Config:
    """Base configuration."""
    # Flask settings
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-change-in-production')
    FLASK_APP = 'app.py'
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    
    # API Keys
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    
    # Application settings
    APP_NAME = 'MamaCare Assistant'
    VERSION = '1.0.0'
    
    # Session settings
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # Upload settings
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload size
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    TESTING = True
    TEMPLATES_AUTO_RELOAD = True


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = True
    PREFERRED_URL_SCHEME = 'https'


class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    WTF_CSRF_ENABLED = False
    
    # Use in-memory SQLite database for tests
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

# Get the appropriate configuration based on environment
def get_config(env=None):
    """Retrieve environment configuration.
    
    Args:
        env (str): Environment name (development, production, testing)
        
    Returns:
        Config: Configuration class for the specified environment
    """
    if env is None:
        env = os.getenv('FLASK_ENV', 'development')
    return config.get(env.lower(), config['default'])


# Initialize Gemini AI model
try:
    import google.generativeai as genai
    if Config.GEMINI_API_KEY:
        genai.configure(api_key=Config.GEMINI_API_KEY)
        model = genai.GenerativeModel("gemini-2.0-flash")
    else:
        print("Warning: GEMINI_API_KEY not found. Some features may not work.")
        model = None
except ImportError:
    print("Warning: google-generativeai package not installed. AI features will be disabled.")
    model = None
