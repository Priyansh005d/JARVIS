import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "Enter ur news api"

def speak(text):
    engine.say(text)
    engine.runAndWait()
def processCommand(c):
    if("open google") in c.lower():
        webbrowser.open("https://google.com")
    elif("open youtube") in c.lower():
        webbrowser.open("https://youtube.com")
    elif("open github") in c.lower():
        webbrowser.open("https://github.com")
    elif("open mail") in c.lower():
        webbrowser.open("https://gmail.com")
    elif("open grok") in c.lower():
        webbrowser.open("https://grok.com/")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)   
    elif "news" in c.lower():
        url = "newsapilink"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            
            # Extract the list of articles
            articles = data.get("articles", [])
            
            # Print the outlines (titles) of the articles
            for index, article in enumerate(articles, start=1):
                speak(f"{index}. {article.get('title')}")
        else:
            speak("Failed to fetch news:", response.status_code)




    


if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        #Listen for the wake word Jarvis
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            audio = r.listen(source,timeout=5 )
        print("Recognizing.....")    

        # recognize speech 
        try:
            word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("ya")
                #listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
       
        except Exception as e:
            print(" error; {0}".format(e))
