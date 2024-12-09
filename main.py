import pyttsx3
import pyaudio
import SpeechRecognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    elif hour >= 18 and hour < 20:
        speak("Good Evening")
    else:
        speak("Good Night")
    speak("Hello, I am Alex. Please tell me how may I help you.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Say something!")
        r.pause_threshold = 2
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return "None"
    except sr.RequestError:
        print("Could not request results; check your network connection.")
        return "None"
    except Exception as e:
        print(f"Error: {e}")
        return "None"
    return query

def chooseBrowser():
    speak("Which browser would you like to use? You can choose Chrome or Edge.")
    browser_choice = takeCommand().lower()
    if 'chrome' in browser_choice or 'open chrome' in browser_choice:
        return 'chrome'
    elif 'edge' in browser_choice or 'open microsoft edge' in browser_choice:
        return 'edge'
    else:
        speak("Sorry, I didn't get that. Using default browser.")
        return 'default'

def openWithBrowser(url):
    browser = chooseBrowser()
    speak("Opening browser...")
    try:
        if browser == 'chrome':
            webbrowser.get('chrome').open(url)
        elif browser == 'edge':
            webbrowser.get('edge').open(url)
        else:
            webbrowser.open(url)
    except Exception as e:
        speak("Sorry, I couldn't open the browser.")
        print(e)

def tell_joke():
    jokes = [
        'Why did the math book look sad? Because it had too many problems.',
        'Why was the stadium so cool because it was filled with fans.',
        'What did 20 do when it was hungry? Twenty-eight.'
    ]
    joke = random.choice(jokes)
    speak(joke)

def set_speaking_rate(rate):
    engine.setProperty('rate', rate)

if __name__ == "__main__":
    set_speaking_rate(150)

    # Register browsers
    try:
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
        webbrowser.register('edge', None, webbrowser.BackgroundBrowser(r"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"))
    except Exception as e:
        print(f"Error during registering browsers: {e}")

    wishMe()

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                result = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(result)
                speak(result)
            except Exception as e:
                speak("Sorry, I couldn't find any information on that topic.")
                print(e)

        elif 'show trending news' in query:
            openWithBrowser("https://timesofindia.indiatimes.com/")

        elif 'open google' in query:
            openWithBrowser("https://www.google.com")

        elif 'open youtube' in query:
            openWithBrowser("https://www.youtube.com")

        elif 'open' in query:
            openWithBrowser(query.replace("open", "").strip())

        elif 'what' in query and 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'tell me a joke' in query or 'joke' in query:
            tell_joke()

        elif 'exit' in query or 'quit' in query:
            speak("Goodbye!")
            break

        elif 'play music' in query or 'play song' in query:
            music_path = "C:\\Users\\ASUS\\OneDrive\\Desktop\\nikita dance.mp3"
            os.startfile(music_path)
            speak("Playing music")

        elif 'open files' in query or 'show my files' in query:
            my_files = "C:\\Program Files"
            os.startfile(my_files)
            speak("Opening files")

        elif 'thank you' in query:
            speak("You're welcome. Feel free to ask anything...")
