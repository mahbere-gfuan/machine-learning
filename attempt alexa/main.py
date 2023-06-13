#this part is the speach recoginzer part of the alexa project that ai have begun
import speech_recognition as sr


listener =sr.Recognizer()
try:
    with sr.Microphone() as source:
        print('listen...')
        voice = listener.listen(source)
        command =listener.recognize_google(voice)
        print(command)
except:
    pass