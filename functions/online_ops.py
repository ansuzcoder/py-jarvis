"""
Allow JARVIS to perform online operation
"""

import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config

def find_my_ip():
    """
    Find ip of user's device
    """
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address['ip']


def search_on_wiki(query):
    """
    Search given query through Wikipedia
    """
    results = wikipedia.summary(query, sentences=2)


def play_on_youtube(video):
    """
    Play given video on YouTube
    """
    kit.playonyt(video)


def search_on_google(query):
    """
    Search given query on Google
    """
    kit.search(query)
