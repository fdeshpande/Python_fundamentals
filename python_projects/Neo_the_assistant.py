from email.mime import audio
from unittest import result
import webbrowser
from numpy import source
import pyttsx3   # for voice
import datetime  # for analyzing time
import speech_recognition as sr  # for recognize the user's speech by microphone.
import wikipedia
import os
import smtplib # used to send email through gmail.



engine = pyttsx3.init('sapi5') #sapis is used to take voice which is inbuild voice of microsoft.
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!!!")

    elif hour>=12 and hour<18:
        speak("Good Evening !!!")
        speak("I am Neo ......Tell me how can I help you ma'am .") 

def takeCommand():
    #it takes microphone input from the user and returns string output.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language="en_in")
        print("User said : {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('deshpandefalguni7@gmail.com','findmyaccount')
    server.sendemail('deshpandefalguni7@@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

    #Logic for execution tasks based on query...

    if "wikipedia" in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipwdia","")
        results = wikipedia.summary(query ,sentence =2)
        speak("According to wikipedia")
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")   

    elif 'open google' in query:
        webbrowser.open("google.com")  

    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")     

    elif 'play music' in query:
        music_dir = 'D:\\Non Critical\\songs\\Favourite Songs2'
        songs = os.listdir(music)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'the time ' in query :
        strTime = datetime.datetime.now().strftime("%H : %M : %S") 
        speak(f"Ma'am , The time is {strTime}")   

    elif 'open code' in query:
        codePath = "C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"   
        os.startfile(codePath)

    elif 'send email to '  in query:
        try:
            speak("What should i say??")
            content = takeCommand()
            to = "deshpandefalguni2@gmail.com"
            sendEmail(to,content)
            speak("email has been send.")

        except Exception as e:
            print(e)
            speak("Sorry ma'am , i am not able to send an email.")     