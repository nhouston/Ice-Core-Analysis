import matplotlib.pyplot as plt
import cv2
import numpy as np

"""
This function detects the bigger vertical illuminationlines in the image.  The images are resized
to make the bigger lines, small so a similar technique to finding fine lines can be used.
The lines are drawn onto the image. From this it is anticipated that these detected lines 
will be able to be removed from the image, removing artefacts from the image.  Function 
will return an image with no vertical illumination lines. 
"""
def bigLines():
	# Read an image
	img = cv2.imread('43.bmp')
	# Get the original size of the image
	height, width, depth = img.shape
	# Resize the image to 120,120
	newimg = cv2.resize(img,(120,120))
	# Apply Gaussain Blur
	newimg = cv2.GaussianBlur(newimg,(5,5),0)
	# Apply sobel 'x' edge detection 
	sobelx = cv2.Sobel(newimg,cv2.CV_64F,1,0,ksize=5)  # x
	# Threshold the image
	_, th1 = cv2.threshold(sobelx,250,255,cv2.THRESH_BINARY)
	# Resize the image back to original size
	back = cv2.resize(img,(height,width))

	# Plot the results 
	plt.subplot(1,5,1),plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
	plt.title('Original'), plt.xticks([]), plt.yticks([])

	plt.subplot(1,5,2),plt.imshow(cv2.cvtColor(newimg, cv2.COLOR_BGR2RGB))
	plt.title('Resize'), plt.xticks([]), plt.yticks([])

	plt.subplot(1,5,3),plt.imshow(sobelx, cmap = 'gray')
	plt.title('Sobel'), plt.xticks([]), plt.yticks([])

	plt.subplot(1,5,4),plt.imshow(th1, cmap = 'gray')
	plt.title('Threshold'), plt.xticks([]), plt.yticks([])

	plt.subplot(1,5,5),plt.imshow(cv2.cvtColor(back, cv2.COLOR_BGR2RGB))
	plt.title('Orginal size'), plt.xticks([]), plt.yticks([])

	plt.show()