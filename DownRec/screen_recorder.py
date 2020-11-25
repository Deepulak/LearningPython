import numpy as np
from PIL import ImageGrab
import cv2

fourcc = cv2.VideoWriter_fourcc(*"XVID")
size = (ImageGrab.grab()).size
output = cv2.VideoWriter("output.mp4",fourcc,5.0,size)

while True:
	img = np.array(ImageGrab.grab())
	frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	cv2.imshow(img)
	cv2.imwrite(img)
	if cv2.waitKey(1) == 27: # 27 -esc key
		break

	output.release()
	cv2.destroyAllWindows()