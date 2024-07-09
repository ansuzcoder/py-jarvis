"""
Speech engine configuration
"""

import pyttsx3
from decouple import config

USERNAME = config("USER")
BOTNAME = config("BOTNAME")

engine = pyttsx3.init("sapi5")

engine.setProperty("rate", 190)
engine.setProperty("volume", 1.0)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
