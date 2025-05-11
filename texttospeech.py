import pyttsx3

engine = pyttsx3.init()

# Optional: slow down the speech rate
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 80)

# Get available voices
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

with open("amit.txt", "r") as file:
   content = file.read()
   engine.say(f'{content}')
   engine.save_to_file(content, 'test.mp3')
   engine.runAndWait()
