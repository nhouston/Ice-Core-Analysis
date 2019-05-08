import cv2

"""
Function that compares/shows the comaprison of birghtnesses after differnet uses of equalisation
methods.  Comparing against CLAHE and Histogram equalisation, this comparison is carried out
between a top level image, middle level image and a bottom level image.
"""

def brightness():
	# Read the sliced image folder
	sliceImage = '../../Documents/ImageAnalysis.nosync/sliceImage/'
	# Get the top image 
	img = cv2.imread(sliceImage + str(1) +".bmp",1)
	# Get the middle image 
	midImage = 80
	# Get the bottom image 
	bottomImage = 160
	# Take the image and slipt it into the HSV colour spectrem 
	h,s,v= cv2.split(cv2.cvtColor(img, cv2.COLOR_BGR2HSV))	
	# Threshold the V value the equalised V
	ret1,th1 = cv2.threshold(v,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	# Equalise the histogram of v and the threshold
	histE = cv2.equalizeHist(v)
	hist = cv2.equalizeHist(th1)
	# Apply CLAHE equalisation 
	clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(4,4))
	cl1 = clahe.apply(v)
	# Read in the middle image 
	Midimg = cv2.imread(sliceImage + str(midImage) +".bmp",1)
	# Take the image and slipt it into the HSV colour spectrem
	H,S,V= cv2.split(cv2.cvtColor(Midimg, cv2.COLOR_BGR2HSV))	
	# Threshold the V value the equalised V
	ret1,th2 = cv2.threshold(V,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	# Equalise the histogram of v and the threshold
	histE1 = cv2.equalizeHist(V)
	hist1 = cv2.equalizeHist(th2)
	# Apply CLAHE equalisation
	clahe1 = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(4,4))
	cl11 = clahe.apply(V)
	# Read the bottom image
	Bimg = cv2.imread(sliceImage + str(bottomImage) +".bmp",1)
	# Split into HSV
	R,G,B = cv2.split(cv2.cvtColor(Midimg, cv2.COLOR_BGR2HSV))	
	# Threshold the V value the equalised V
	ret1,th3 = cv2.threshold(B,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	# Equalise the histogram of v and the threshold
	histE3 = cv2.equalizeHist(B)
	hist3 = cv2.equalizeHist(th3)
	# Apply CLAHE equalisation
	clahe3 = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(4,4))
	cl13 = clahe.apply(B)
	# Convert from BGR to RGB for matplotlib
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	threshold = cv2.cvtColor(th1,cv2.COLOR_BGR2RGB)
	imageEq = cv2.cvtColor(cv2.merge([h,s,histE]),cv2.COLOR_HSV2RGB)
	histogram = cv2.cvtColor(hist,cv2.COLOR_BGR2RGB)
	clahe = cv2.cvtColor(cv2.merge([h,s,cl1]),cv2.COLOR_HSV2RGB)
	Midimg = cv2.cvtColor(Midimg, cv2.COLOR_BGR2RGB)
	threshold1 = cv2.cvtColor(th2,cv2.COLOR_BGR2RGB)
	imageEq1 = cv2.cvtColor(cv2.merge([h,s,histE1]),cv2.COLOR_HSV2RGB)
	histogram1 = cv2.cvtColor(hist1,cv2.COLOR_BGR2RGB)
	clahe1 = cv2.cvtColor(cv2.merge([h,s,cl11]),cv2.COLOR_HSV2RGB)
	Bimg = cv2.cvtColor(Bimg, cv2.COLOR_BGR2RGB)
	threshold3 = cv2.cvtColor(th3,cv2.COLOR_BGR2RGB)
	imageEq3 = cv2.cvtColor(cv2.merge([h,s,histE3]),cv2.COLOR_HSV2RGB)
	histogram3 = cv2.cvtColor(hist3,cv2.COLOR_BGR2RGB)
	clahe3 = cv2.cvtColor(cv2.merge([h,s,cl13]),cv2.COLOR_HSV2RGB)
	# Plot the figure for maptplot
	fig = plt.figure(figsize = (20,8))
	# Add the images via subplots
	fig.add_subplot(3,5,1)
	plt.imshow(img),plt.title("Current Sliced image"),plt.xticks([]),plt.yticks([])
	fig.add_subplot(3,5,2)
	plt.imshow(threshold),plt.title("Threshold"),plt.xticks([]),plt.yticks([])
	fig.add_subplot(3,5,3)
	plt.imshow(imageEq),plt.title("Equalised Histogram Image"),plt.xticks([]),plt.yticks([])
	fig.add_subplot(3,5,4)
	plt.imshow(histogram),plt.title("Equalised Histogram Threshold"),plt.xticks([]),plt.yticks([])
	fig.add_subplot(3,5,5)
	plt.imshow(clahe),plt.title("CLAHE equalisation"),plt.xticks([]),plt.yticks([])

	fig.add_subplot(3,5,6)
	plt.imshow(Midimg),plt.xticks([]),plt.yticks([])
	fig.add_subplot(3,5,7)
	plt.imshow(threshold1),plt.xticks([]),plt.yticks([])
	fig.add_subplot(3,5,8)
	plt.imshow(imageEq1),plt.xticks([]),plt.yticks([])
	fig.add_subplot(3,5,9)
	plt.imshow(histogram1),plt.xticks([]),plt.yticks([])
	fig.add_subplot(3,5,10)
	plt.imshow(clahe1),plt.xticks([]),plt.yticks([])

	fig.add_subplot(3,5,11)
	plt.imshow(Bimg),plt.xticks([]),plt.yticks([])
	fig.add_subplot(3,5,12)
	plt.imshow(threshold3),plt.xticks([]),plt.yticks([])
	fig.add_subplot(3,5,13)
	plt.imshow(imageEq3),plt.xticks([]),plt.yticks([])
	fig.add_subplot(3,5,14)
	plt.imshow(histogram3),plt.xticks([]),plt.yticks([])
	fig.add_subplot(3,5,15)
	plt.imshow(clahe3),plt.xticks([]),plt.yticks([])

	plt.show()