import os
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write

# Function to record audio from the microphone
def record_audio(duration, sample_rate=44100):
    print("Recording...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype='int16')
    sd.wait()  # Wait until the recording is finished
    print("Recording finished.")
    return audio, sample_rate

# Main code
input_value = int(input("Enter 0 or 1: "))

if input_value == 1:
    duration = int(input("Enter the duration of the recording in seconds: "))
    output_directory = r"C:\Users\harsh\Desktop\3rd year\Sem 5\SGP-2\WavFiles"
    file_name = input("Enter the name of the file: ")
    # Record audio from the microphone
    audio, sample_rate = record_audio(duration)
    # Save the audio file in .wav format
    output_path = os.path.join(output_directory, f"{file_name}.wav")
    write(output_path, sample_rate, audio)
    print(f"Audio saved to {output_path}")