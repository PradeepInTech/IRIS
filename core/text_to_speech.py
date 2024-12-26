import platform
import os
import socket
from gtts import gTTS
import pyttsx3
from playsound import playsound

# Define audio storage path
AUDIO_DIR = os.path.join(os.path.dirname(__file__), 'audio')

# Create audio directory if it doesn't exist
if not os.path.exists(AUDIO_DIR):
    os.makedirs(AUDIO_DIR)

def internet_available():
    try:
        # Create a socket connection to test internet connectivity
        socket.create_connection(("8.8.8.8", 53), timeout=1)
        return True
    except OSError:
        return False

def generate_audio_file(text, lang='en'):
    # Generate audio file using gTTS
    try:
        tts = gTTS(text=text, lang=lang)
        audio_file = os.path.join(AUDIO_DIR, 'speech.mp3')
        tts.save(audio_file)
        return audio_file
    except Exception as e:
        print(f"Error generating audio: {e}")
        return None

def play_audio(audio_file):
    # Play the generated audio file
    try:
        playsound(audio_file)
        return True
    except Exception as e:
        print(f"Error playing audio: {e}")
        return False

def cleanup_audio(audio_file):
    # Remove temporary audio file
    try:
        os.remove(audio_file)
    except Exception as e:
        print(f"Error removing audio file: {e}")

def use_pyttsx3(text):
    # Use pyttsx3 for Windows TTS
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        return True
    except Exception as e:
        print(f"Error with pyttsx3: {e}")
        return False

def use_espeak(text):
    # Use espeak as fallback
    try:
        os.system(f'espeak "{text}"')
        return True
    except Exception as e:
        print(f"Error with espeak: {e}")
        return False

def speak(text):
    '''
    Multi-platform text-to-speech function that handles speech synthesis across different systems:
    - Windows: Utilizes pyttsx3 for native speech synthesis
    - Linux/Mac with internet: Leverages Google's Text-to-Speech (gTTS) service
    - Linux/Mac without internet: Falls back to espeak for offline synthesis
    '''
    system = platform.system() 
    
    if system == "Windows":
        use_pyttsx3(text)
    else:
        if internet_available():
            audio_file = generate_audio_file(text)
            if audio_file:
                if play_audio(audio_file):
                    cleanup_audio(audio_file)
                    return
                
        # Fallback to espeak if gTTS fails or no internet
        if not use_espeak(text):
            print("Error: No text-to-speech engine available")
