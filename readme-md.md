# Gemini Desktop AI Assistant

A simple desktop AI assistant using Google's Gemini API with a tkinter GUI.

## Prerequisites

- Python 3.8+
- Google Gemini API Key (get one from [Google AI Studio](https://makersuite.google.com/app/apikey))

## Setup

1. Clone the repository
```bash
git clone https://github.com/yourusername/gemini-desktop-assistant.git
cd gemini-desktop-assistant
```

2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the application
```bash
python main.py
```

## Usage

- When you first run the app, you'll be prompted to enter your Google Gemini API key
- The API key is saved in a `config.json` file for future use
- Type your message in the input box and press Enter or click Send
- Use the "New Chat" button to start a fresh conversation

## Features

- Text-based AI chat interface
- Persistent API key storage
- Simple, clean tkinter GUI
- Conversation history tracking

## Notes

- Ensure you have a stable internet connection
- Keep your API key confidential
