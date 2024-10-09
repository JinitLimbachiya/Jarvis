# INSTALL NECESSARY MODULES FOR THIS PROJECT
# 1. SPEECH RECOGNITION - For recognizing voice commands
# 2. WEBBROWSER - To open websites (In some cases, VSC has built-in support)
# 3. PYTTSX3 - For text-to-speech functionality

import speech_recognition as sr
import webbrowser
import pyttsx3


jarvis = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    jarvis.say(text)
    jarvis.runAndWait()

def processCommand(command):
    command = command.lower()   

    if "open" in command:
        openWebsite(command)

    elif "play" in command:
        playSong(command)

    elif "stop" in command or "exit" in command:
        speak("Shutting off")
        print("Shutting Off")
        exit()

    else:
        speak("Sorry. I don't know this.")

def openWebsite(command):   
    try:
        siteName = command.split("open", 1)[1].strip()
        url = f"https://www.{siteName}.com"
        speak(f"Launching {siteName}")
        webbrowser.open(url)

    except Exception as e:
        print(f"Error: {e}")
        speak("Sorry, I couldn't open the website.")

def playSong(command):
    try:
        if command.startswith("play"):
            song = command.split("play", 1)[1].strip()
            if song:
                searchSong(song)
            else:
                speak("Please specify a song to play.")
                
        else:
            speak("I can only play songs if you say 'play'")

    except Exception as e:
        print(f"Error: {e}")
        peak("There was an error trying to play the song.")

def searchSong(song):
    try:
        query = song.replace(' ', '+')
        url = f"https://www.youtube.com/results?search_query={query}"
        webbrowser.open(url)
        speak(f"Searching for {song} on youtube")

    except Exception as e:
        print(f"Error: {e}")
        

def recognize():
    with sr.Microphone() as source:
        audio = recognizer.listen(source, timeout = 5, phrase_time_limit = 3)

    try:
        return recognizer.recognize_google(audio)   

    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return None

if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        try:
            word = recognize()
            if word and "jarvis" in word.lower():
                speak("Yes, How can i help?")

                command = recognize()
                if command:
                    processCommand(command)
        
        except Exception as e:
            print(f"Unexpected Error: {e}")
            speak("An error occurred. Please try again.")