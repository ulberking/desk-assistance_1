import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(5 <= hour and hour < 12):
        speak('good morning Minho')
    elif(12 <= hour and hour < 17):
        speak('good after noon Minho')
    elif(17 <= hour and hour <= 21):
        speak('good evening Minho')
    speak("Hi I'm your desk support. How may i help you today?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('recognizing')
        query = r.recognize_google(audio, language='en-in')
        print('user said ' + query)
    except:
        print("I didn't understand. Tell me a new time")


if(__name__ == '__main__'):
    wishMe()
    takeCommand()
