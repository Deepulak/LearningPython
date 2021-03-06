# Impoting necessary packages
import cv2
import datetime
import tkinter as tk
from tkinter import *
from pytube import YouTube
from PIL import Image,ImageTk
from tkinter import messagebox, filedialog


# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
	linkLabel = Label(root,text="YOUTUBE LINK : ",bg="tan4")
	linkLabel.grid(row=1,column=0,pady=5,padx=5)

	root.linText = Entry(root,width=57,textvariable=videoLink)
	root.linkText.grid(row=1,column=1,pady=5,padx=5,columnspan=2)

	destinationLabel = label(root, text="DESTINATION : ",bg="tan4")
	destinationLabel.grid(row=2,column=0,pady=5,padx=5)

	root.destinationText = Entry(root,width=40,textvariable=downloadPath)
	root.destinationText.grid(row=2,column=1,pady=5,padx=5)

	browseButton = Button(root,text="BROWSE",command=Browse,width=15)
	browseButton.grid(row=2,column=2,pady=5,padx=5)

	downButton = Button(root,text="DOWNLOAD",command=Download,width=30)
	downButton.grid(row=3,column=1,pady=5,padx=5)

	root.videoLabel = Label(root,bg="tan4")
	root.videoLabel.grid(row=4,column=0,columnspan=3,pady=5,padx=5)


# Defining Browse() to select a distination folder to save the video
def Browse():
	# Presentiong user with a pop-up for directory selection, initialdir argument is optional
	# Retrieving the user-input destination directory and storing it in DownloadDirectory
	downloadDirectory = filedialog.askdirectory(initialdir="path")
	# Displaying the directory int he directory textbox
	downloadPath.set(downloadDirectoryn)

# Defining Download() to download the video
def Download():
	# Fetching the user input Youtube link and storing it in yt_link variable
	yt_link = videoLink.get()
	# Fetching the destination directory and storing it in downFolder variable
	downFolder = downloadPath.get()
	# Creating object of Youtube() with the yt_liink variable as the argument
	getVideo = YouTube(yt_link)
	# Getting all the variable streams of the youtube video and selecting the first from
	# the filtered streams using first()
	videoStream = getVideo.streams.first()
	# Storing the name for the download video in the videoName variable
	videoName = str(datetime.datetime.now().srtftime('%d%m%y%H%M%S'))
	# Storing the current datetime value as start_time
	start_time = datetime.datetime.now()
	# Downloading the video to the user-input destination directory
	videoStream.download(downFolder, filename=videoName)
	# Storing thrr current datetime value as end_time
	end_time = datetime.datetime.now()
	# Calculating and storing the difference between the start_time and end_time as total_time
	total_time = (end_time - start_time).seconds
	# Display the message
	messagebox.showinfo("SUCCESS", "VIDEO DOWNLOADED AND SAVED IN\n" + downFolder + "\nDOWNLOAD TIME : ", str(total_time) + "SECONDS : ")
	# Creating object of class VideoCapture with webcam index
	root.cap = cv2.VideoCapture(downFolder + '/' + videoName + '.mp4')
	# Calling the PlayVideo() function to play the current video
	PlayVideo()

def PlayVideo():
	# Capturing frame by frame
	ret1, frame1, = root.cap.read()
	# Fetching the width and height of the video frames
	width = root.cap.get(3)
	height = root.cap.get(4)
	resize_width = int(width)
	resize_height = int(height)
	# Resizing the video frame
	video = cv2.resize(frame1,(resize_width,resize_height), fx=0, fy=0, interpolation=cv.INTER_CUBIC)
	# Converting the frame from BGR to original RGBA
	video = cv2.cvtColor(video,cv2.COLOR_BGR2RGBA)
	# Creating an image memory fromthe above frame exporting arra interface
	videoImg = Image.fromarray(video)
	# Creating object of PhotoImage() class to display the frame
	imagetk = ImageTk.PhotoImage(image=videoImg)
	# Configuring the label to display the frame
	root.videoLabel.configure(image=imagetk)
	# Keeping a reference
	root.videoLabel.imagetk = imagetk
	# Calling the function after 10 milliseconds
	root.videoLabel.after(32, PlayVideo)

# Creating object of tk class
root = tk.Tk()

# Setting the title, background color and size of the tkinter window
# and disabling the resizing property of the tkinter window
root.geometry("665x490")
root.title("PyYouTubeDownloader")
root.config(background="tan4")
root.resizable(False, False)

# Creating the tkinter variables
videoLink = StringVar()
downloadPath = StringVar()

# Calling the CreateWidgets() function
CreateWidgets()

# Defining the infinite loop to run application
root.mainloop()

