from matplotlib import colors
import matplotlib.pyplot as plt
import cv2
 


"""
This function compares the image histograms against each other, including the different bin sizes.  
The user will be asked which image they would like to compare against other images from the middle 
and the bottom of the orginal image.
"""

def compare(inputImage):
	# Load the sliced image and RGB Graph folders
	sliceImage = '../../Documents/ImageAnalysis.nosync/sliceImage/'
	graphImage = '../../Documents/ImageAnalysis.nosync/RGBGraphs/'

	# Choose the middle and bottom images
	midImage = 80
	bottomImage = 160

	# Read in the users image and the corresponding graphs
	img = cv2.imread(sliceImage + inputImage +".bmp",1)
	img1 =cv2.imread(graphImage + "rgbGraph10_" + str(inputImage) + ".png",1)
	img2 =cv2.imread(graphImage + "rgbGraph20_" + str(inputImage) + ".png",1)
	img3 =cv2.imread(graphImage + "rgbGraph40_" + str(inputImage) + ".png",1)
	img4 =cv2.imread(graphImage + "rgbGraph60_" + str(inputImage) + ".png",1)

	# Read in the middle image and the corresponding graphs
	Midimg = cv2.imread(sliceImage + str(midImage) +".bmp",1)
	Midimg1 =cv2.imread(graphImage + "rgbGraph10_" + str(midImage) + ".png",1)
	Midimg2 =cv2.imread(graphImage + "rgbGraph20_" + str(midImage) + ".png",1)
	Midimg3 =cv2.imread(graphImage + "rgbGraph40_" + str(midImage) + ".png",1)
	Midimg4 =cv2.imread(graphImage + "rgbGraph60_" + str(midImage) + ".png",1)

	# Read in the bottom image and the corresponding graphs
	Bimg = cv2.imread(sliceImage + str(bottomImage) +".bmp",1)
	Bimg1 =cv2.imread(graphImage + "rgbGraph10_" + str(bottomImage) + ".png",1)
	Bimg2 =cv2.imread(graphImage + "rgbGraph20_" + str(bottomImage) + ".png",1)
	Bimg3 =cv2.imread(graphImage + "rgbGraph40_" + str(bottomImage) + ".png",1)
	Bimg4 =cv2.imread(graphImage + "rgbGraph60_" + str(bottomImage) + ".png",1)

	# Convert the image from BGR to RGB as matplotlib deals in RGB spectrum 
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	Midimg = cv2.cvtColor(Midimg, cv2.COLOR_BGR2RGB)
	Bimg = cv2.cvtColor(Bimg, cv2.COLOR_BGR2RGB)

	# Create the matplot figure
	fig = plt.figure(figsize = (15,8))
	# Top level depth
	fig.add_subplot(3,5,1)
	plt.imshow(img),plt.title("Current Sliced image"),plt.xticks([]),plt.yticks([])
	fig.add_subplot(3,5,2)
	plt.imshow(img1),plt.title("Graph - Bin size 10"),plt.xticks([]),plt.yticks([])
	fig.add_subplot(3,5,3)
	plt.imshow(img2),plt.title("Graph - Bin size 20"),plt.xticks([]),plt.yticks([])
	fig.add_subplot(3,5,4)
	plt.imshow(img3),plt.title("Graph - Bin size 40"),plt.xticks([]),plt.yticks([])
	fig.add_subplot(3,5,5)
	plt.imshow(img4),plt.title("Graph - Bin size 60"),plt.xticks([]),plt.yticks([])
	# Middle image depth 
	fig.add_subplot(3,5,6)
	plt.imshow(Midimg),plt.xticks([]),plt.yticks([])
	fig.add_subplot(3,5,7)
	plt.imshow(Midimg1),plt.xticks([]),plt.yticks([])
	fig.add_subplot(3,5,8)
	plt.imshow(Midimg2),plt.xticks([]),plt.yticks([])
	fig.add_subplot(3,5,9)
	plt.imshow(Midimg3),plt.xticks([]),plt.yticks([])
	fig.add_subplot(3,5,10)
	plt.imshow(Midimg4),plt.xticks([]),plt.yticks([])
	# Bottom image depth
	fig.add_subplot(3,5,11)
	plt.imshow(Bimg),plt.xticks([]),plt.yticks([])
	fig.add_subplot(3,5,12)
	plt.imshow(Bimg1),plt.xticks([]),plt.yticks([])
	fig.add_subplot(3,5,13)
	plt.imshow(Bimg2),plt.xticks([]),plt.yticks([])
	fig.add_subplot(3,5,14)
	plt.imshow(Bimg3),plt.xticks([]),plt.yticks([])
	fig.add_subplot(3,5,15)
	plt.imshow(Bimg4),plt.xticks([]),plt.yticks([])
	plt.show()