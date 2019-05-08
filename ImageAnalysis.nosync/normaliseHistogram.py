import glob
import re
import cv2
import numpy as np 
import histogramMatch
"""
normaliseImages will mormalise the images based on Histogram matching compared to that of
the method classification.  The function will use the hist_match function to carry out the 
histgram matching on the images.  The target image has been created manually through 
photoshop, it has been based on one of the images from the top of the original image.  The
images are saved to file after histogram matching and image sharpening and noise removal
takes place.
"""

def normaliseImages():
	# Open the sliced images folder
	files = sorted(glob.glob('../../Documents/ImageAnalysis.nosync/sliceImage/*.bmp'),
		key=lambda x: tuple(map(int, re.findall(r'\d+', x))))
	# Read each individual image in the sliced image folder"""
	image = [cv2.imread(img) for img in files]
	# Read the target image 
	target = cv2.imread('Target.png')

	count = 0
	for img in image:
		# Apply a gauusian blur to the image
		img = cv2.GaussianBlur(img,(5,5),0)
		# Take the image and slipt it into the HSV colour spectrem
		h,s,v= cv2.split(cv2.cvtColor(img, cv2.COLOR_BGR2HSV))
		# Equalise the histogram for the V value
		clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(4,4))
		cl1 = clahe.apply(v)
		# Convert and split that target image into HSV
		H,S,V= cv2.split(cv2.cvtColor(target, cv2.COLOR_BGR2HSV))
		# Carry out histogram mathcing on each channel of the image 
		matchingHistH = hist_match(h,H)
		matchingHistS = hist_match(s,S)
		matchingHist = hist_match(cl1,V)
		# Merge the back together with the histogram matched values 
		HistMatch = cv2.cvtColor(cv2.merge([matchingHistH,matchingHistS,matchingHist]),cv2.COLOR_HSV2BGR)
		# Apply sharpening to the image 
		kernel = np.array([[0,-1,-0], [-1,5,-1], [0,-1,0]])
		sharp = cv2.filter2D(HistMatch, -1, kernel)
		# Apply a morphology filter to the image
		kernel = np.ones((2,2),np.uint8)
		closing = cv2.morphologyEx(sharp,cv2.MORPH_CLOSE,kernel, iterations = 2)
		# Remove noise from the image
		denoise = np.ones(HistMatch.shape).astype(np.uint8)
		noise = cv2.fastNlMeansDenoisingColored(closing, denoise, 2,7,31)
		# Save the image to file
		count += 1
		cv2.imwrite('../../Documents/ImageAnalysis.nosync/EqualisedImagesHistogram/'+ \
			str(count) + '.bmp', noise)