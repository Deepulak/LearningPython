import numpy as np
import cv2
from skimage import data, filters

cap = cv.VideoCapture("output.mp4")

# Randomly selected 25 frames
frameIds = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=25)

# Store selcted frames in an array
frames = []
for fid in frameIds:
	cap.set(cv2.CAP_PROP_POS_FRAMES, fid)
	ret, frame = cap.read()
	frames.append(frame)

# Calculate the median along the time axis
medianFrame = np.median(frames, axis=0).astype(dtype=np.uint8)

# Display median frame
cv2.imshow("frame", medianFrame)
cv2.WaitKey(0)
