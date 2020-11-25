# Python code to convert video to audio
import moviepy.editor as mp

# Inser video file path
clip = mp.VideoFileClip(r"name of the video file")

# Insert a name of the video file
clip.audio.write_audiofile(r"audio.mp3")