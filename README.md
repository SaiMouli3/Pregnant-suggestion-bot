# 🤰 MamaCare Assistant

A personalized pregnancy support chatbot that provides helpful information, daily tips, and emotional support for expecting mothers.

## ✨ Features

- 🤔 Answer pregnancy-related questions
- 📅 Provide trimester-specific advice
- 🥗 Offer dietary recommendations based on preferences (veg/non-veg)
- 😊 Mood-based emotional support
- 🔔 Helpful reminders and daily tips
- 🌈 Beautiful and responsive UI

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd mamacare
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the project root with your API keys:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

## 🖥️ Running the Application

1. Start the Flask development server:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## 🛠️ Project Structure

```
mamacare/
├── static/                 # Static files (CSS, JS, images)
│   ├── script.js           # Frontend JavaScript
│   └── style.css           # Stylesheet
├── templates/              # HTML templates
│   ├── index.html          # Main page
│   └── response_template.md# Response template
├── agents/                 # AI agent implementations
├── .env                    # Environment variables
├── app.py                  # Flask application
├── config.py               # Configuration settings
├── graph.py                # LangGraph implementation
├── main.py                 # CLI version
├── requirements.txt        # Python dependencies
└── scheduler.py            # Task scheduler
```

## 🌟 Features in Detail

### 🤔 Ask Questions
Get answers to common pregnancy-related questions, from symptoms to delivery preparation.

### 📅 Trimester-Specific Advice
Receive personalized advice based on your current trimester.

### 🥗 Dietary Recommendations
Get food suggestions tailored to your dietary preferences (vegetarian/non-vegetarian).

### 😊 Emotional Support
Mood-based emotional support and stress-relief tips.

### 🔔 Daily Tips & Reminders
Helpful reminders for appointments, tests, and self-care.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to all the expecting mothers who provided valuable feedback
- Built with ❤️ using Python, Flask, and LangChain
- Icons by Twemoji
