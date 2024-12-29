# IRIS: Intelligent Voice Assistant

IRIS is an intelligent voice assistant project developed in Python. It leverages speech recognition and text-to-speech libraries to provide an interactive experience. IRIS can perform tasks such as fetching weather update, opening applications, recognizing voice commands, and provide latest news headlines updates.

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
   python3 Iris.py
   ```

---

## Technologies Used
- **Programming Language:** Python
- **Libraries:**
   - `SpeechRecognition` for voice input
   - `pyttsx3` for text-to-speech on Windows and Mac
   - `requests` for making HTTP requests
   - `beautifulsoup4` for web scraping
   - `gtts` for text-to-speech on Linux(with internet)
- **System dependencies:**
   - `espeak` for text-to-speech on Linux(without internet)
---

## Usage
1. Launch the application using `python3 Iris.py`.
2. Use voice commands to interact with IRIS. Some examples include:
   - "What is the weather and temperature now?"
   - "Open [application name]"
   - "What are the current headlines?"

---

## Roadmap
Future updates may include:
- Integration with more APIs (e.g., finance, calendar events, and many more).
- Support for multiple languages.
- Enhanced Natural Language Processing (NLP) capabilities for better command recognition and processing.
- Desktop GUI for broader accessibility.
- More tools integration like calculator and more.
- Automation 
- And any thing new I have learned will be integrated with it.

---

## Contributing
Contributions are welcome if you want to! To contribute:
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
- Inspiration: The project draws inspiration from virtual assistants like Siri and Alexa even though I can't make such big project and one big motivation was to try creating a big projects which I can use to gather or contain everything I have learnt.
- Special Thanks: Big Thanks to all contributors and users supporting the project. It will be very helpful to gain knowledge from you all and let's help others learn.

---

