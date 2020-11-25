from PIL import ImageGrab
import keyboard

print("press c to take screenshot")

while True:
	try:
		if keyboard.is_pressed('c'):
			image = ImageGrab.grab()

			name = str(input("\n Enter file name : "))
			image.save(name + ".png")
			break
		else:
			pass
	except:
		break