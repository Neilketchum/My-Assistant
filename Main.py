import pyttsx3
import wikipedia
import speech_recognition as sr
import datetime 
import webbrowser as wb
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
#print(voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if(hour>= 0 and hour < 12):
        speak("Good Morning")
    elif(hour> 12 and hour < 18):
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hi Neil ") #.This is Jarvis . You are the best Iron Man
def takeComand():
    """Takes microphone input from  user and returns it in string"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ....")
        r.pause_threshold = 1 #press controll  to and click.This is done to increase the time for a speech to be complete
        audio = r.listen(source)
    try:
        print("Recogonizing.....")
        query = r.recognize_google(audio,language='en-in')
        print("User said : ",query)
    except Exception as e:
        #print(e) #if i want to se the error
        print("Pardon Neil")
        return "None"
    return  query
if __name__ == "__main__":
    wishme()
    while(1):
        query =  takeComand().lower()
    # logic for executing task based on query
        if 'wikipedia' in query:
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            print(results)
            speak("According to Wikipedia")
            speak(results)
        elif 'open youtube' in query:
            wb.open('Youtube.com')
        elif 'open Browser' in query:
            wb.open('Google.com')
        elif 'Cricket Score' in query:
            wb.open('https://www.cricbuzz.com')
        elif 'open google' in  query:
            wb.open('Google.com')
        elif 'open stackoverflow'in query:
            wb.open('https://stackoverflow.com/')
        elif 'play music' in query:
            wb.open('https://gaana.com')
        elif'exit' in query:
            speak("Good Bye!!")
            break
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(strTime)
        elif 'open code ' in query:
            codepath = "C:\\Users\\Daipayan Hati\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)