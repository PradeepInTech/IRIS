# IRIS: Intelligent Voice Assistant

IRIS is an intelligent voice assistant project developed in Python. It leverages speech recognition and text-to-speech libraries to provide an interactive experience. IRIS can perform tasks such as fetching weather updates, telling the current time, opening applications, recognizing voice commands, and providing news updates.

---

## Features
- **Voice Recognition:** Uses speech recognition to interpret voice commands
- **Text-to-Speech:** Provides voice responses using pyttsx3
- **Weather Updates:** Can fetch and report weather information
- **Time Reporting:** Tells current time when asked
- **Application Control:** Can open specified applications
- **News Updates:** Retrieves and reports news headlines

---

## Installation
### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Setup Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/PradeepInTech/Iris.git
   cd Iris
   ```
2. **Create a virtual environment:**
   ```bash
   python -m venv iris-env
   source iris-env/bin/activate  # Linux/MacOS
   iris-env\Scripts\activate  # Windows
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the application:**
   ```bash
   python main.py
   ```

---

## Technologies Used
- **Programming Language:** Python
- **Libraries:**
   - `SpeechRecognition` for voice input
   - `pyttsx3` for text-to-speech
   - `requests` for making HTTP requests
   - `beautifulsoup4` for web scraping

---

## Usage
1. Launch the application using `python main.py`.
2. Use voice commands to interact with IRIS. Some examples include:
   - "What is the weather in [city]?"
   - "What time is it?"
   - "Open [application name]"
   - "What is the news?"

---

## Roadmap
Future updates may include:
- Integration with more APIs (e.g., news, finance, calendar events).
- Support for multiple languages.
- Enhanced Natural Language Processing (NLP) capabilities.
- Desktop GUI for broader accessibility.

---

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature name'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments
- Inspiration: The project draws inspiration from virtual assistants like Siri and Alexa.
- Special Thanks: To all contributors and users supporting the project.

---

