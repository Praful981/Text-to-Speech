# Text to Speech Application

This is a simple Text to Speech (TTS) application built using Python and Tkinter for the GUI and pyttsx3 for text-to-speech conversion. The application allows users to input text and convert it to speech with customizable voice options.

## Features

- Text input via a user-friendly GUI.
- Convert the input text to speech.
- Select different voices for the speech output.
- Handle errors such as empty text input or invalid voice selection.

## Prerequisites

- Python 3.11.3
- `tkinter` (usually comes pre-installed with Python)
- `pyttsx3` library

## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/your-username/text-to-speech.git
    cd text-to-speech
    ```

2. **Install the required Python packages**:

    ```sh
    pip install pyttsx3
    ```

## Usage

1. **Run the application**:

    ```sh
    python main.py
    ```

2. **Enter text** in the provided text area.

3. **Click the "Speak" button** to convert the text to speech.

## Customizing Voices

To customize the voice used for the speech output, you need to find out the available voices on your system. You can run the following script to list all available voices:

```python
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.name}")
