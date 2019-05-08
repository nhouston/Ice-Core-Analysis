import glob
import re
import cv2
import time
"""
This function is used to help reduce the appearance of the vertical lines in images.  
Reads in the equalised images from the Histogram matched images.  Images are thresholded
and then the OpenCv function inpaint is used to replace the stiped pixels in the image
"""

def verticalLines():
	start = time.time()
	# Open the sliced images folder
	files = sorted(glob.glob('../../Documents/ImageAnalysis.nosync/EqualisedImagesHistogram/*.bmp'),
		key=lambda x: tuple(map(int, re.findall(r'\d+', x))))
	# Read each individual image in the sliced image folder
	image = [cv2.imread(img) for img in files]

	count = 0 
	for img in image:
		# Split the image into HSV
		h,s,v= cv2.split(cv2.cvtColor(img, cv2.COLOR_BGR2HSV))
		# Apply global threshold
		ret1,th1 = cv2.threshold(v,250,255,cv2.THRESH_TOZERO)
		# Use the cv2.inpaint function to replace the pixels based on the threshold
		dst = cv2.inpaint(img,th1,60,cv2.INPAINT_TELEA)
		# Save the image to file
		count += 1
		cv2.imwrite('../../Documents/ImageAnalysis.nosync/removedVertical/'+ \
			str(count) + '.bmp', dst)
	end = time.time()
	print(end - start)