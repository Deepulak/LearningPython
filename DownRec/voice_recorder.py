# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

# pip install wavio
# pip install scipy

# Sampling frequency
freq = 44100
# Recording duration
duration = 5
# Start recorder with the given values
# of duration and simple frequency
recording = sd.rec(int(duration * freq), samplerate=freq, channel=2)
# Record audio for the given number of seconds
sd.wait()
# This will convert the numpy array to an audio
# file with given sampling frequency
write("recording0.wav", freq, recording)
# Convert the numpy array to audio file
wv.write("recording1.wav", recording, freq, sampwidth=2)