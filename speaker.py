"""
Main speaking module
"""


from random import choice
from datetime import datetime

import speech_recognition as sr

from speech_engine import USERNAME, BOTNAME, engine
from util_options import opening_text


def speak(text):
    """
    Make JARVIS say the provided text
    """
    engine.say(text)
    engine.runAndWait()


def greet():
    """
    Greets the user
    """
    hour = datetime.now().hour

    if hour >= 6 and hour < 12:
        speak(f"Good morning, Master {USERNAME}")
    elif hour >= 12 and hour < 16:
        speak(f"Good afternoon, Master {USERNAME}")
    elif hour >= 16 and hour < 19:
        speak(f"Good evening, Master {USERNAME}")

    speak(f"I am {BOTNAME}, your personal assistant. How may I help you today?")


def take_user_input():
    """
    Take audio input from user
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-us")
        if "exit" in query or "stop" in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Goodnight sir, take care of yourself!")
            else:
                speak("Have a good day sir!")
            exit()
    except Exception:
        speak("Sorry, I failed to comprehend what you said. Could you please repeat your request?")
        query = 'None'
    return query