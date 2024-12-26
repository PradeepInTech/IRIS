import speech_recognition as sr
import sounddevice

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source: #Using the default microphone for audio
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=10)
            print("Recognizing...")
            query = r.recognize_google(audio) #Processing audio to text
            print(f'User : {query}\n')
            return query
        except Exception as e:
            print(f"Error: {e}")
            return "None"

