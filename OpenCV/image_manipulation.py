import cv2
# Read and display the image
img = cv2.imread("debicki.jpg", 1)
cv2.imshow("Image Window", img)

# Resize an image
resize_img = cv2.resize(img, (500, 500))
cv2.imshow("Image", resize_img)

# Get Height and Width
height, width = img.shape[0 : 2]
print(height, width)

# Rotate an image
height, width = resize_img.shape[0 : 2]
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 180, .75)
rotate_image = cv2.warpAffine(img, rotation_matrix, (width, height))
cv2.imshow("Rotate", rotate_image)

# Crop image
height, width = img.shape[0 : 2]
startRow = int(height*.30)
startCol = int(height*.30)
endRow = int(height*.85)
endCol = int(height*.85)

cropImage = img[startRow:endRow, startCol:endCol]
cv2.imshow("Cropped", cropImage)

# Save and Write Image
cv2.imshow("Save", img)
cv2.imwrite("new_debi.png", img)

cv2.waitKey(0)
cv2.destroyAllWindows()