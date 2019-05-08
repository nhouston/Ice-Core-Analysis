import glob
import re
import cv2

"""
normaliseByClass is a function that will be used to normalise the images based on their
prior classification.  This function will read in the images from the sliced image folder
and apply certain steps onto these images. Images will undergo thresholding from which 
operations using OpenCv bitwise operators will be used to adjust the brightness values, 
based on the thresholded image.  The images before being saved to file will undergo sharpening
and noise removal.
"""

def normaliseByClass():
	# Open the sliced images folder
	files = sorted(glob.glob('../../Documents/ImageAnalysis.nosync/sliceImage/*.bmp'),
		key=lambda x: tuple(map(int, re.findall(r'\d+', x))))
	# Read each individual image in the sliced image folder
	image = [cv2.imread(img) for img in files]

	count = 0

	for img in image:
		# Apply image with a Gaussian blur using a 5x5 kernel
		img = cv2.GaussianBlur(img,(5,5),0)
		# Take the image and slipt it into the HSV colour spectrem
		h,s,v= cv2.split(cv2.cvtColor(img, cv2.COLOR_BGR2HSV))
		# Equalise the histogram for the V value
		clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(4,4))
		cl1 = clahe.apply(v)
		# Apply a threshold to the equalised V channel
		ret1,th1 = cv2.threshold(cl1,127,255,cv2.THRESH_BINARY)
		# Carry out bitwise operation on the white pixels of the threshold
		th_v_up = (cv2.bitwise_and(cl1, th1) + cv2.bitwise_and(np.ones(cl1.shape).astype(np.uint8) \
			* np.where((cl1 - 55) > 200,cl1+75,255), th1))
		# Invert the threshold to get the blacks 
		th1_n = cv2.bitwise_not(th1)
		# Carry out bitwise operation on the black pixels of the threshold		 
		th_v_down = (cv2.bitwise_and(cl1, th1_n) - cv2.bitwise_and(np.ones(cl1.shape).astype(np.uint8)\
		 * np.where((cl1 - 215) < 40,cl1-75,255) , th1_n))
		# Combine the results of the white and black pixel adjustments
		result = cv2.add(th_v_up,th_v_down)
		# Merge the image back together replacing the adjusted V channel with 'result'
		mergeColour = cv2.cvtColor(cv2.merge([h,s,result]),cv2.COLOR_HSV2BGR)
		# Apply sharpening to the image 
		kernel = np.array([[0,-1,-0], [-1,5,-1], [0,-1,0]])
		sharp = cv2.filter2D(mergeColour, -1, kernel)
		# Apply a morphology filter to the image
		kernel = np.ones((2,2),np.uint8)
		closing = cv2.morphologyEx(sharp,cv2.MORPH_CLOSE,kernel, iterations = 2)
		# Remove noise from the image
		denoise = np.ones(mergeColour.shape).astype(np.uint8)
		noise = cv2.fastNlMeansDenoisingColored(closing, denoise, 2,7,31)
		# Save the image to file
		count += 1
		cv2.imwrite('../../Documents/ImageAnalysis.nosync/EqualisedImagesClassified/'+ \
			str(count) + '.bmp', noise)