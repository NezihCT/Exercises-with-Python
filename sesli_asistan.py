import speech_recognition as sp
import time
from asistan_komutlar import command

speech = sp.Recognizer()

while True:
    with sp.Microphone() as source:
        print("Yeap, I'm listening to you...")
        audio = speech.listen(source)
    
    data = ""

    try :
        data = speech.recognize_google(audio, language='İng-İng')
        print(data)
        commands = command(data)
        commands.find_command()
        

