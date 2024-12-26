from core import listen, speak, process_query
import requests

def check_network():
    try:
        response = requests.get("http://google.com", timeout=3)
        return response.status_code == 200
    except Exception:
        return False

def handle_no_internet():
    message = "No internet connection."
    print(message)
    speak(message)

def greeting():
    # Display welcome message and introduce Iris voice assistant
    print("*"*50)
    print("\tIris: A Personal Voice Assistant")
    print("*"*50)
    print("\nIris: Hello, My name is Iris your personal voice assistant. How can I help you today?")
    speak("Hello, My name is Iris your personal voice assistant. How can I help you today?")

def user_commands():
    # Listen for user voice input and process the command
    if query := listen():
        process_query(query)

def handle_exit():
    # Display goodbye message when exiting the program
    print("\nSee you soon...")
    speak("\nSee you soon...")

def personal_assistant():
    # Main loop for running the voice assistant
    while True:
        try:
            # Check for internet connectivity
            if not check_network():
                print("\nInternet connection lost!")
                print("Please Reconnect to continue using Iris...")
                return

            user_commands()

        except KeyboardInterrupt:
            # Handle user interruption (Ctrl+C)
            handle_exit()
            break
        except Exception as e:
            # Handle any unexpected errors
            print(f"An error occurred: {str(e)}")

def main():
    # Entry point of the program
    if not check_network():
        handle_no_internet()
        return
    greeting()
    personal_assistant()

# Run the program if executed directly
if __name__ == "__main__":
    main()
