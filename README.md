# OIBSIP_PythProg_Task-1
# Advanced Voice Assistant

A Python-based voice assistant that understands voice commands and performs tasks like telling time/date, sending emails, fetching weather, web searching, and playing YouTube videos.

# Project Structure

-> **main.py**: Entry point; greets user and listens for commands.
-> **speech.py**: Handles speech recognition and text-to-speech.
-> **commands.py**: Processes commands like time, weather, email, search, and play.
-> **email_utils.py**: Sends emails using SMTP.
-> **weather_utils.py**: Fetches weather data from OpenWeatherMap API.
-> **config.py**: Stores API keys and configuration.

# Technologies Used

-> **SpeechRecognition** for converting speech to text.
-> **pyttsx3** for text-to-speech output.
-> **smtplib** for sending emails.
-> **requests** for API calls.
-> **pywhatkit** for YouTube and web search.
-> **OpenWeatherMap API** for weather info.
-> **Python 3.x**

# How It Works

1. The assistant greets the user based on the time of day.
2. Listens to voice commands and converts them to text.
3. Processes commands to perform tasks (time, weather, email, search, play).
4. Responds verbally with results or confirmations.
5. Continues until the user says “stop” or “exit”.

# Usage

1. Install dependencies:

   ```bash
   pip install -r requirements.txt

# Voice Instructions Supported

You can interact with the assistant using the following voice commands:

# Time & Date
-> "What is the time?"
-> "Tell me the time."
-> "What time is it?"
-> "What is today's date?"
-> "Tell me the date."
-> "What day is it today?"

# Weather
-> "What is the weather in [city]?"
-> "Tell me the weather."
-> "How is the weather today?"
-> "Weather report for [city]."

# Email
-> "Send an email."
-> "I want to send an email."
-> "Email someone."

# Web Search & YouTube
-> "Search for [query]."
-> "Look up [topic]."
-> "Play [song name]."
-> "Play [video] on YouTube."

# Basic Conversation & Control
-> "Hello" / "Hi"
-> "How are you?"
-> "Who are you?"
-> "Stop"
-> "Exit"
-> "Quit"
-> "Goodbye"

