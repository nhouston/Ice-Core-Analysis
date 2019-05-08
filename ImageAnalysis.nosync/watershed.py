import matplotlib.pyplot as plt
import cv2


"""
Function to carry out watershed segmentation.  Used to carry out the process for watershed
and to show its effects on the images.  An experimenation method which may or may not be
utalised in the final image analysis process
"""

def watershed():
	# Read the image to carry out watershed on
	img = cv2.imread("1.bmp")
	# Split the BGR values
	b,g,r = cv2.split(img)
	# Merge the image back together in RGB for matplotlib
	rgb_img = cv2.merge([r,g,b])
	# Convert the image to grayscale
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
	# Noise removal
	kernel = np.ones((2,2),np.uint8)
	closing = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel, iterations = 2)
	# Find sure background area
	sure_bg = cv2.dilate(closing,kernel,iterations=10)#3
	# Finding sure foreground area
	dist_transform = cv2.distanceTransform(sure_bg,cv2.DIST_L2,3)
	# Threshold
	ret, sure_fg = cv2.threshold(dist_transform,0.1*dist_transform.max(),255,0)
	# Find the unknown region of image
	sure_fg = np.uint8(sure_fg)
	unknown = cv2.subtract(sure_bg,sure_fg)
	# label the markers
	ret, markers = cv2.connectedComponents(sure_fg)
	# Add one to all labels so that sure background is not 0, but 1
	markers = markers+1
	# Mark the region of unknown with zeros
	markers[unknown==255] = 0
	# Carry out watershed segmentation
	markers = cv2.watershed(img,markers)
	img[markers == -1] = [0,0,0]
	# Convert from BGR to RGB 
	img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
	# Plot figure
	fig = plt.figure(figsize = (15,8))
	# Add subplots
	fig.add_subplot(2,4,1),plt.imshow(rgb_img)
	plt.title('Input Image'), plt.xticks([]), plt.yticks([])
	fig.add_subplot(2,4,2),plt.imshow(thresh, 'gray')
	plt.title("Otsu's binary threshold"), plt.xticks([]), plt.yticks([])
	fig.add_subplot(2,4,3),plt.imshow(closing, 'gray')
	plt.title("morphologyEx:Closing:2x2"), plt.xticks([]), plt.yticks([])
	fig.add_subplot(2,4,4),plt.imshow(sure_bg, 'gray')
	plt.title("Dilation"), plt.xticks([]), plt.yticks([])
	fig.add_subplot(2,4,5),plt.imshow(dist_transform, 'gray')
	plt.title("Distance Transform"), plt.xticks([]), plt.yticks([])
	fig.add_subplot(2,4,6),plt.imshow(sure_fg, 'gray')
	plt.title("Thresholding"), plt.xticks([]), plt.yticks([])
	fig.add_subplot(2,4,7),plt.imshow(unknown, 'gray')
	plt.title("Unknown"), plt.xticks([]), plt.yticks([])
	fig.add_subplot(2,4,8),plt.imshow(img, 'gray')
	plt.title("Result from Watershed"), plt.xticks([]), plt.yticks([])
	plt.tight_layout()
	plt.show()