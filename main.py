from datetime import datetime

import speech_recognition as sr
import pyttsx3
import pyaudio
import pywhatkit
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except Exception as e:
        print('error:', e)
        return ""
    return command


def run_alexa():
    while True:
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play'+'')
            talk('playing' + song)
            print('playing')
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %P')
            talk('current time is'+time)
        elif 'wikipedia' in command:
            thing = command.replace('what is'+'')
            info = wikipedia.summary(thing, 10)
            print(info)
            talk(info)
        elif 'date' in command:
            print('I am an AI')

        elif 'alexa are you single' in command:
            print('I am in a relationship with wifi')
        elif 'joke' in command:
            talk('pyjokes.get_joke()')

while True:
    run_alexa()
