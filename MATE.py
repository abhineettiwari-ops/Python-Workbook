import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    print(f"Speaking: {audio}")
    for line in audio.split('. '):
        engine.say(line)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Abhineet!, I am your mate. Please tell me how may I help you")
    elif 12 <= hour < 18:
        speak("Good Afternoon Abhineet!, I am your mate. Please tell me how may I help you")
    else:
        speak("Good Evening Abhineet! I am your mate. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'exit' in query or 'quit' in query:
            speak("Goodbye Abhineet! Have a great day.")
            break
        else:
            speak("Thank you for using me. Please give a valid command.")
            
# ----------------------------------------------------------------------------------------
# This code is still under development. More features will be added soon.
# ----------------------------------------------------------------------------------------             
