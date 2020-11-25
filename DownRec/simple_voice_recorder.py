import sounddevice as sd
import soundfile as sf

def voice_rec():
	fs = 48000
	# seconds
	duration = 5
	print("Recording...")
	myrecording = sd.rec(int(duration * fs), samplerate=fs, channel=2)
	sd.wait()

	# Save as Flac file at correct rate
	return sf.write("my_audio_file1.flac", myrecording, fs)
	print("Recorded..")

voice_rec()