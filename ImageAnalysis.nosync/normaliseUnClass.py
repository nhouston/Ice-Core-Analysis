import glob
import cv2
import re


"""
This method normalises the images without being classifed before hand.  It will take all the images
in the sliced image folder and apply histogram equalisation.  Before  CLAHE Histogram equalisation 
the images will be converted from BGR to HSV.  The  CLAHE histogram equalisation will be 
applied to the 'V' value.  The images will then be saved.  
"""

def normailsiationWithoutClassification():
	# Open the sliced images folder
	files = sorted(glob.glob('../../Documents/ImageAnalysis.nosync/sliceImage/*.bmp'),
		key=lambda x: tuple(map(int, re.findall(r'\d+', x))))
	# Read each individual image in the sliced image folder
	image = [cv2.imread(img) for img in files]

	count = 0
	# For each image in the sliced image folder, split the image to HSV and apply CLAHE Histogram 
	# Equalisation
	for img in image:
		# Split the image into HSV
		H, S, V = cv2.split(cv2.cvtColor(img, cv2.COLOR_BGR2HSV))
		# Appy CLAHE equalisation 
		clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(4,4))
		cl1 = clahe.apply(V)
		# Merge the image back together
		eq_image = cv2.cvtColor(cv2.merge([H, S, cl1]), cv2.COLOR_HSV2BGR)
		count += 1
		# Save the figure for the current image	
		cv2.imwrite('../../Documents/ImageAnalysis.nosync/EqualisedImages/'+ str(count) + '.bmp', 
			eq_image)