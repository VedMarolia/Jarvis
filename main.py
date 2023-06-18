import speech_recognition as sr
import pyttsx3
import webbrowser

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en")
        print(f"You said: {query}")
        return query
    except Exception as e:
        print("Sorry, I didn't catch that. Could you please repeat?")
        return None

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()

# Main program loop
while True:
    command = listen()
    if command:
        if "hello" in command:
            speak("Hello, how can I assist you?")
        elif "goodbye" in command:
            speak("Goodbye!")
            break
        elif "open" in command:
            website = command.replace("open", "").strip()
            url = f"https://www.{website}.com"
            webbrowser.open(url)
        else:
            speak("I'm sorry, I can't perform that task.")
