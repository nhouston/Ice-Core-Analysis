import cv2


"""
classImage is a function that will take an image and the images ground truth and compare them pixel 
by pixel against each other.  This is done to decide which thresholding method will be the best to 
help indicate which areas of the image is ice and that is dirt.  Various thresholding methods will 
be used.  The function will return percentages for each thresholding method - these will be 
percetnage accuracy and percentage error.
"""

def classImage():
	# Read in an image
	img = cv2.imread('1.bmp')
	img2 = cv2.imread('../../Documents/ImageAnalysis.nosync/groundTruths/1-GT.bmp')
	# Get the size of the image
	h = img.shape[0]
	w = img.shape[1]

	# Give the image a gaussian blur
	img = cv2.GaussianBlur(img,(5,5),0)
	# Take the image and slipt it into the HSV colour spectrem 
	H, S, V = cv2.split(cv2.cvtColor(img, cv2.COLOR_BGR2HSV))
	# Equalise the histogram for the V value
	eq_V = cv2.equalizeHist(V)
	# Merge all the values back into one image 
	eq_image = cv2.cvtColor(cv2.merge([H, S, eq_V]), cv2.COLOR_HSV2BGR)

	# Convert the images into grayscale ready for thresholding 
	img = cv2.cvtColor(eq_image, cv2.COLOR_BGR2GRAY)
	img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

	# global thresholding
	ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
	# Otsu's thresholding
	ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	# Otsu's thresholding after Gaussian filtering
	blur = cv2.GaussianBlur(img,(5,5),0)
	ret3,th3 = cv2.threshold(blur,127,255,cv2.THRESH_OTSU)
	# Adapative Threshold
	th4 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,15,2)
	# Binary INV
	ret5,th5 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)

	# Global Thresholding Truths 
	matchesDirt = 0
	matchesIce = 0
	noMatchDirt = 0
	noMatchIce = 0  
	
	for i in range(0,h):
		for j in range(0,w):
			# True positive - Dirt is equal to dirt
			if th1[i,j] == 255 and img2[i,j] == 255:
				matchesDirt += 1
				# True Negative - Ice is equal to ice
			elif th1[i,j] == 0 and img2[i,j] == 0:
				matchesIce += 1
				# False  - Image says its dirt but is actually ice 
			elif th1[i,j] == 255 and img2[i,j] == 0:
				noMatchIce += 1
				# False - Image says its ice but its actually dirt
			elif th1[i,j] == 0 and img2[i,j] == 255:
				noMatchDirt += 1
	# Calculate the totals for all, accuracy and error
	total = matchesDirt + matchesIce + noMatchDirt + noMatchIce
	acc = matchesDirt + matchesIce
	error = noMatchDirt + noMatchIce
	# Calculate the percentages for accuracy and error
	percentAcc = acc // total * 100
	percentErr = error // total * 100

	# Otsu's Thresholding Matches
	matchesDirtOtsu = 0
	matchesIceOtsu = 0
	noMatchDirtOtsu = 0
	noMatchIceOtsu = 0  
	
	for i in range(0,h):
		for j in range(0,w):
			# True positive - Dirt is equal to dirt
			if th2[i,j] == 255 and img2[i,j] == 255:
				matchesDirtOtsu += 1
				# True Negative - Ice is equal to ice 
			elif th2[i,j] == 0 and img2[i,j] == 0:
				matchesIceOtsu += 1
				# False  - Image says its dirt but is actually ice 
			elif th2[i,j] == 255 and img2[i,j] == 0:
				noMatchIceOtsu += 1
				# False - Image says its ice but its actually dirt 
			elif th2[i,j] == 0 and img2[i,j] == 255:
				noMatchDirtOtsu += 1

	# Calculate the totals for all, accuracy and error
	totalOtsu = matchesDirtOtsu + matchesIceOtsu + noMatchDirtOtsu + noMatchIceOtsu
	accOtsu = matchesDirtOtsu + matchesIceOtsu
	errorOtsu = noMatchDirtOtsu + noMatchIceOtsu
	# Calculate the percentages for accuracy and error
	percentErrOtsu = errorOtsu // totalOtsu * 100
	percentAccOtsu = accOtsu // totalOtsu * 100

	# Otsu's Thresholding with Gaussian Matches
	matchesDirtOtsuG = 0
	matchesIceOtsuG = 0
	noMatchDirtOtsuG = 0
	noMatchIceOtsuG = 0  
	
	for i in range(0,h):
		for j in range(0,w):
			# True positive - Dirt is equal to dirt
			if th2[i,j] == 255 and img2[i,j] == 255:
				matchesDirtOtsuG += 1
				# True Negative - Ice is equal to ice 
			elif th2[i,j] == 0 and img2[i,j] == 0:
				matchesIceOtsuG += 1
				# False  - Image says its dirt but is actually ice
			elif th2[i,j] == 255 and img2[i,j] == 0:
				noMatchIceOtsuG += 1
				# False - Image says its ice but its actually dirt 
			elif th2[i,j] == 0 and img2[i,j] == 255:
				noMatchDirtOtsuG += 1

	# Calculate the totals for all, accuracy and error
	totalOtsuG = matchesDirtOtsuG + matchesIceOtsuG + noMatchDirtOtsuG + noMatchIceOtsuG
	accOtsuG = matchesDirtOtsuG + matchesIceOtsuG
	errorOtsuG = noMatchDirtOtsuG + noMatchIceOtsuG
	# Calculate the percentages for accuracy and error
	percentErrOtsuG = errorOtsuG // totalOtsuG * 100
	percentAccOtsuG = accOtsuG // totalOtsuG * 100

	# Adaptive Threshold
	matchesDirtAdap = 0
	matchesIceAdap = 0
	noMatchDirtAdap = 0
	noMatchIceAdap = 0  
	
	for i in range(0,h):
		for j in range(0,w):
			# True positive - Dirt is equal to dirt
			if th4[i,j] == 255 and img2[i,j] == 255:
				matchesDirtAdap += 1
				# True Negative - Ice is equal to ice
			elif th4[i,j] == 0 and img2[i,j] == 0:
				matchesIceAdap += 1
				# False  - Image says its dirt but is actually ice 
			elif th4[i,j] == 255 and img2[i,j] == 0:
				noMatchIceAdap += 1
				# False - Image says its ice but its actually dirt
			elif th4[i,j] == 0 and img2[i,j] == 255:
				noMatchDirtAdap += 1

	# Calculate the totals for all, accuracy and error
	totalAdap = matchesDirtAdap + matchesIceAdap + noMatchDirtAdap + noMatchIceAdap
	accAdap = matchesDirtAdap + matchesIceAdap
	errorAdap = noMatchDirtAdap + noMatchIceAdap
	# Calculate the percentages for accuracy and error
	percentErrAdap = errorAdap // totalAdap * 100
	percentAccAdap = accAdap // totalAdap * 100

	# Threshold INV
	matchesDirtINV = 0
	matchesIceINV = 0
	noMatchDirtINV = 0
	noMatchIceINV = 0  
	
	for i in range(0,h):
		for j in range(0,w):
			# True positive - Dirt is equal to dirt
			if th5[i,j] == 255 and img2[i,j] == 255:
				matchesDirtINV += 1
				# True Negative - Ice is equal to ice
			elif th5[i,j] == 0 and img2[i,j] == 0:
				matchesIceINV += 1
				# False  - Image says its dirt but is actually ice
			elif th5[i,j] == 255 and img2[i,j] == 0:
				noMatchIceINV += 1
				# False - Image says its ice but its actually dirt 
			elif th5[i,j] == 0 and img2[i,j] == 255:
				noMatchDirtINV += 1

	# Calculate the totals for all, accuracy and error
	totalINV = matchesDirtINV + matchesIceINV + noMatchDirtINV + noMatchIceINV
	accINV = matchesDirtINV + matchesIceINV
	errorINV = noMatchDirtINV + noMatchIceINV
	# Calculate the percentages for accuracy and error
	percentErrINV = errorINV // totalINV * 100
	percentAccINV = accINV // totalINV * 100

	# Print the results from the thresholding and confusion matrix 
	print("--------- Percentage Accuracy ----------")
	print("Global Thresholding - " + str(percentAcc))
	print("Otsu Thresholding - " + str(percentAccOtsu))
	print("Otsu Thresholding with Gaussian - " + str(percentAccOtsuG))
	print("Adaptive Thresholding - " + str(percentAccAdap))
	print("Thresholding INV - " + str(percentAccINV))
	print("----------- Percentage Error -----------")
	print("Global Thresholding - " + str(percentErr))
	print("Otsu Thresholding - " + str(percentErrOtsu))
	print("Otsu Thresholding with Gaussian - " + str(percentErrOtsuG))
	print("Adaptive Thresholding - " + str(percentErrAdap))
	print("Thresholding INV - " + str(percentErrINV))
	print("---------------------------------------- ")