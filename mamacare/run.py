#!/usr/bin/env python3
"""
MamaCare Assistant - Run Script
"""
import os
import webbrowser
from threading import Timer
from app import app as flask_app

def open_browser():
    """Open the default web browser to the app's URL."""
    url = 'http://127.0.0.1:5000'
    webbrowser.open_new(url)

def main():
    """Run the application."""
    print("🚀 Starting MamaCare Assistant...")
    print(f"🌐 Server running at http://127.0.0.1:5000")
    print("🖥️  Opening in your default web browser...")
    print("🛑 Press Ctrl+C to stop the server")
    
    # Open the browser after a short delay
    Timer(1.5, open_browser).start()
    
    # Run the Flask app
    flask_app.run(debug=True, use_reloader=False)

if __name__ == '__main__':
    main()
