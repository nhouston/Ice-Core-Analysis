from matplotlib import colors
import matplotlib.pyplot as plt
import glob
import cv2
import re

""" 
Function that creates all the RGB graphs for each individual sliced image.  For each image, graphs
of different bin sizes will be created - 10,20,40,60.  Each images corresponding graph will be saved
for usage later on for comparison against each other.
"""

def rgbGraphs():
	# Open the sliced images folder
	files = sorted(glob.glob('../../Documents/ImageAnalysis.nosync/sliceImage/*.bmp'),
		key=lambda x: tuple(map(int, re.findall(r'\d+', x))))
	# Read each individual image in the sliced image folder
	image = [cv2.imread(img) for img in files]

	# Histogram bin sizes
	bins = 10 
	bin20 = 20
	bin40 = 40
	bin60 = 60

	# Read the colours in this order to OpenCv standards
	color = ('b','g','r')

	count = 1

	# For each image in the folder of sliced images, create a RGB Graph with bins of 10
	for img in image:
	 	# Create the RGB graph for each image
	 	fig = plt.figure(figsize = (5,5))
	 	for channel,col in enumerate(color):
	 		histr = cv2.calcHist([img],[channel],None,[bins],[0,256]) # Calculate the image histogram
	 		plt.plot(histr,color = col)
	 		plt.xlim([0,bins])
	 		plt.title('RGB Histogram - Bin size 10')

	 	# Save the figure for the current image
	 	plt.savefig('../../Documents/ImageAnalysis.nosync/RGBGraphs/rgbGraph10_'+ str(count) + '.png')
	 	count += 1

	count = 1

	for img in image:
	 	# Create the RGB graph for each image
	 	fig = plt.figure(figsize = (5,5))
	 	for channel,col in enumerate(color):
	 		histr = cv2.calcHist([img],[channel],None,[bin20],[0,256]) # Calculate the image histogram
	 		plt.plot(histr,color = col)
	 		plt.xlim([0,20])
	 		plt.title('RGB Histogram - Bin size 20')

	 	# Save the figure for the current image
	 	plt.savefig('../../Documents/ImageAnalysis.nosync/RGBGraphs/rgbGraph20_'+ str(count) + '.png')
	 	count += 1

	count = 1

	for img in image:
	 	# Create the RGB graph for each image
	 	fig = plt.figure(figsize = (5,5))
	 	for channel,col in enumerate(color):
	 		histr = cv2.calcHist([img],[channel],None,[bin40],[0,256]) # Calculate the image histogram
	 		plt.plot(histr,color = col)
	 		plt.xlim([0,40])
	 		plt.title('RGB Histogram - Bin size 40')

	 	# Save the figure for the current image
	 	plt.savefig('../../Documents/ImageAnalysis.nosync/RGBGraphs/rgbGraph40_'+ str(count) + '.png')
	 	count += 1

	count = 1

	for img in image:
	 	# Create the RGB graph for each image
	 	fig = plt.figure(figsize = (5,5))
	 	for channel,col in enumerate(color):
	 		histr = cv2.calcHist([img],[channel],None,[bin60],[0,256]) # Calculate the image histogram
	 		plt.plot(histr,color = col)
	 		plt.xlim([0,60])
	 		plt.title('RGB Histogram - Bin size 60')

	 	# Save the figure for the current image
	 	plt.savefig('../../Documents/ImageAnalysis.nosync/RGBGraphs/rgbGraph60_'+ str(count) + '.png')
	 	count += 1