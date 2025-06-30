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

# Project Structure & Code Overview

# `main.py`
-> **Entry point** of the assistant.
-> Listens to voice commands using `speech_recognition`.
-> Converts speech to text and determines what action to take.
-> Routes commands to appropriate functions (weather, email, search, etc.).
-> Uses `pyttsx3` for text-to-speech responses.

# `speak.py`
--> Contains the `speak()` function that:
  -> Uses the `pyttsx3` library to convert text into speech.
  -> Handles assistant's voice output for all responses.

# `listen.py`
-> Contains the `take_command()` function that:
  -> Listens via the microphone using the `speech_recognition` library.
  -> Returns the recognized speech as text.
  -> Handles "I didn't catch that" errors gracefully.

# `tasks.py`
--> Contains task-specific functions:
  -> `tell_time()` – announces current time.
  -> `tell_date()` – announces today’s date.
  -> `get_weather(city)` – fetches weather info using OpenWeatherMap API.
  -> `send_email(to, subject, message)` – sends email via SMTP.
  -> `search_web(query)` – performs a web search.
  -> `play_youtube(query)` – opens YouTube video.

# `config.py`
--> Stores sensitive configurations and API keys like:
  -> Your **OpenWeatherMap API key**.
  -> Your **email address and app password** (used to send emails).
-> Not pushed to GitHub; should be added to `.gitignore`.

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

