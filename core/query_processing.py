from modules import open_App,close_App, weather_detail, headlines

# Map commands to different ways users might say them
command_synonym = {             
    "news":["news", "headlines"],
    "weather":['"weather', "forecast"], 
    "open": ["open", "launch"],
    "close": ["close", "exit"]
}

# Map commands to their actual functions
commands = {
    "news" : headlines,     
    "weather": weather_detail,
    "open": open_App,      
    "close": close_App     
}

def command_identify(token):
    # Check if any word in user's input matches our known commands
    command = None
    for key, synonym in command_synonym.items():
        if any(word in token for word in synonym):
            command = key
            return command

def process_query(query):
    # Convert user's speech to lowercase words and split into tokens
    token = query.lower().split()
    
    # Identify the command from the user's input
    command = command_identify(token)
    
    if command in commands:
        if command in ["open", "close"]:
            # For app commands, get the app name (e.g., "firefox" from "open firefox")
            app_name = " ".join(token[1:])
            commands[command](app_name)
        else:
            # Run simple commands without arguments
            commands[command]()
