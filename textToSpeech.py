from gtts import gTTS
import os
from datetime import datetime
import random

def textToSpeech(text):
    # Ensure the "static" folder exists (Flask uses this folder to serve static files)
    if not os.path.exists("static"):
        os.makedirs("static")
    
    try:
        # Create speech from the text
        tts = gTTS(text=text, lang='en', slow=False)
        
        # Generate a unique filename based on current time and random number
        current_time = str(datetime.now()) + str(random.randint(1, 1000))
        current_time = current_time.replace(' ', '_').replace(':', '_').replace('.', '_')
        
        file_path = os.path.join("static", f"output-{current_time}.mp3")
        tts.save(file_path)
        
        # Return the file path if the file is saved successfully (relative path for static folder)
        return file_path
    
    except Exception as e:
        print(f"Error during text-to-speech conversion: {e}")
        return None  # Indicate an error if something went wrong
