# from pip import main
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)



def speak(audio): 
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning!") 

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
            
    else:
        speak("Good evening!")

    speak("I am Mr Intense  . Sir Please tell me how may i help you")

def takeCommand():
    # it takes microphone input from user and returns string output 

    r= sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=8,phrase_time_limit=8)
    

    

    try:
        print("Recognizing...")   
        query= r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None"
    return query 

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rishitsetiainsan@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ =="__main__":
    wishMe()
    # while True:
    if 1:
     query = takeCommand().lower()

     if 'wikipedia' in query:
        speak('searching wikipedia')
        query=query.replace("wikipedia","")
        results= wikipedia.summary(query,sentences=2)
        speak("according to wikipedia")
        print(results)
        speak(results)

     elif'open youtube' in query:
        webbrowser.open('youtube.com')

     elif'open google' in query:
        webbrowser.open('google.com')
        
     elif'open Stackoverflow' in query:
        webbrowser.open('stackoverflow.com')
    
   
     elif 'play music' in query:
         music_dir = 'C:\songs'
         songs = os.listdir(music_dir)
         print(songs)    
         os.startfile(os.path.join(music_dir, songs[0]))

     elif 'the time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")    
         speak(f"Sir, the time is {strTime}")
     
     elif 'open code' in query:
         codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
         os.startfile(codePath)

     elif 'email to Rishit' in query:
          try:
                speak("What should I say?")
                content = takeCommand()
                to = "rishitsetiainsan@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
          except Exception as e:
                print(e)
                speak("Sorry my friend Rishit bhai. I am not able to send this email")  