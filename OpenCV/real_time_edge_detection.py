import cv2
import numpy as np

# Capture frames from a camera
cap = cv2.VideoCapture(0)

# Loops runs if capturing has been initialized
while(1):
	# Reads frame from a camera
	ret, frame = cap.read()
	# Converting BGR to HSV
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	# Define range of red color in HSV
	lower_red = np.array([30,150,50])
	upper_red = np.array([255,255,180])
	# Create a red HSV color boundary and
	# threshold HSV image
	mask = cv2.inRange(hsv, lower_red, upper_red)
	# Bitwise and Mask and original image
	res = cv2.bitwise_and(frame, frame, mask=mask)
	# Display an original image
	cv2.imshow('Original, frame')
	# Finds edges in the input image and 
	# marks them in the output map edges
	edges = cv2.canny(frame, 100, 200)
	# Display edges in a frame
	cv2.imshow('Edges', edges)
	# Wait for ESC key to stop
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()