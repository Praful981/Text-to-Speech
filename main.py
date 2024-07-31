"""

import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.name}")



"""




import tkinter as tk
from tkinter import messagebox
import pyttsx3

def text_to_speech():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        engine = pyttsx3.init()
        # Set properties before adding anything to the speaking queue
        rate = engine.getProperty('rate')
        engine.setProperty('rate', 150)  # Speed percent (can go over 100)

        volume = engine.getProperty('volume')
        engine.setProperty('volume', 100.0)  # Volume 0-1

        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)  # Change the index to select a different voice
        engine.say(text)
        engine.runAndWait()
    else:
        messagebox.showwarning("Input Error", "Please enter some text")



# Create the main window
root = tk.Tk()
root.title("Text to Speech")

# Create a Text widget
text_entry = tk.Text(root, wrap=tk.WORD, width=50, height=10)
text_entry.pack(padx=10, pady=10)

# Create a Button to trigger text-to-speech
speak_button = tk.Button(root, text="Speak", command=text_to_speech)
speak_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
