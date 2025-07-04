import datetime 
import pywhatkit
from email_utils import send_email
from weather_utils import get_weather
from speech import speak, listen
from config import OPENWEATHER_API_KEY

def process_command(query):
    if "time" in query:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")

    elif "date" in query:
        date = datetime.datetime.now().strftime("%A, %d %B %Y")
        speak(f"Today's date is {date}")

    elif "weather" in query:
        speak("Which city?")
        city = listen()
        if city:
            weather_report = get_weather(city, OPENWEATHER_API_KEY)
            speak(weather_report)

    elif "email" in query:
        speak("Enter your email ID:")
        sender_email = input("Sender Email: ")
        speak("Enter your email password:")
        sender_password = input("Sender Password: ")
        speak("Whom should I send it to?")
        receiver_email = input("Receiver Email: ")
        speak("What is the subject?")
        subject = listen()
        speak("What should I say?")
        content = listen()
        if send_email(receiver_email, subject, content, sender_email, sender_password):
            speak("Email has been sent.")
        else:
            speak("Failed to send email.")

    elif "search" in query:
        speak("What should I search for?")
        search_query = listen()
        pywhatkit.search(search_query)
        speak("Here are the results.")

    elif "play" in query:
        song = query.replace("play", "").strip()
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)

    else:
        speak("I'm still learning to understand that. Try another command.")
