# This file serves as a modules to call TTS (Text to Voice) service
import requests
import os
from dotenv import load_dotenv
load_dotenv()

def convert_text_to_voice(text: str, speed: int): # return a file containing reference to the generated audio file
    audio = b""

    # sending a request to the server with text and and speed intented
    res = requests.post(
        "https://app.coqui.ai/api/v2/samples/xtts/stream",
        json={"text": text, 
              "language": "en", 
              "speed": speed,
              "voice_id": "28c696b6-b9c6-4e6f-a3a6-1b7f3a283c52"
            },
        headers={"Authorization": f"Bearer LJQWBdjCtYzYO8zkfjygveufkoOev8jxBuM7nq9KUYaq71vnsCKtd6XYU33cA7TV"},
        stream=True,
    )

    # Receive the audio file and save it to local and name as "audio.wav"
    for chunk in res.iter_content(chunk_size=None):
        if chunk is not None:
            audio += chunk
    
    f = open("audio.wav", "wb")
    f.write(audio)