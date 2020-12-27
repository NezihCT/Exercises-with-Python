import json
import urllib.request
import os 
import sys
import requests
from random import choice
from lxml import html
from playsound import playsound
from gtts import gTTS

class command():
    def __init__(self, income_voice):
        self.voice = income_voice.upper()
        self.voice_blocks = self.voice.split()
        print(self.voice_blocks)
        self.commands = ["WEATHER","CLOSE","HOW","wHAT","UP","MONTH"]

    
