from speech import speak, listen
from commands import process_command
import datetime

def greet():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your assistant. How can I help you?")

def main():
    greet()
    while True:
        query = listen()
        if "stop" in query or "exit" in query:
            speak("Goodbye!")
            break
        elif query:
            process_command(query)

if __name__ == "__main__":
    main()
