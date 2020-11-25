import pafy

url = input(f"youtube_video_url")
video = pafy.new(url)

audiostreams = video.audiostreams
for i in audiostreams:
	print(i.bitrate, i.extension, i.get_filesize())

audiostreams[3].download()

# to download best audio

url_ut = input("youtube_video_url ; ")
video_ut = pafy.new(url_ut)

#bestaudio = video_ut.getbestaudio()
#bestaudio.download()