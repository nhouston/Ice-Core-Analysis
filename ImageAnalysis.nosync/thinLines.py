import matplotlib.pyplot as plt
import cv2
import numpy as np

"""
This function detects the fine vertical lines in the image.  The lines are drawn onto the image. 
From this it is anticipated that these detected lines will be able to be removed from the image,
removing artefacts from the image.  Function will return an image with no fine vertical lines. 
"""
def thinLines():
	# Read an image
	img = cv2.imread('43.bmp')
	# Convert and split image into HSV 
	h,s,v = cv2.split(cv2.cvtColor(img, cv2.COLOR_BGR2HSV))
	# Apply sobel 'x' edge detection 
	sobelx = cv2.Sobel(v,cv2.CV_8U,1,0,ksize=3)
	# Apply Canny edge detection
	edges = cv2.Canny(img,50,150,apertureSize = 3)
	# Set the min line length
	minLineLength=100
	# Detect lines in the image using Probabalistic Hough Line transform
	lines = cv2.HoughLinesP(image=edges,rho=1,theta=np.pi/180, threshold=150,lines=np.array([]), 
		minLineLength=minLineLength,maxLineGap=80)
	# Draw the line on the image
	a,b,c = lines.shape
	for i in range(a):
	    x = lines[i][0][0] - lines [i][0][2]
	    y = lines[i][0][1] - lines [i][0][3]
	    if x!= 0:
	        if abs(y/x) >1:
	            cv2.line(img, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), 
	            	(255, 255, 255), 1, cv2.LINE_AA)
	# Remove the lines
	se = cv2.getStructuringElement(cv2.MORPH_ELLIPSE , (3,3))
	gray = cv2.morphologyEx(img, cv2.MORPH_CLOSE, se)
	# Show the img 
	cv2.imshow('img', gray)
	cv2.waitKey(0)

	# #_, th1 = cv2.threshold(v,150,255,cv2.THRESH_BINARY)

	# sobelx = cv2.Sobel(v,cv2.CV_8U,1,0,ksize=3)  # x

	# _, th1 = cv2.threshold(sobelx,127,255,cv2.THRESH_BINARY)

	# cv2.imshow("ew", th1)
	# cv2.waitKey(0)


	# #edges = cv2.Canny(th1,200,250,apertureSize = 7)

	# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (4,8))
	# morph_img = cv2.morphologyEx(th1, cv2.MORPH_CLOSE, kernel)

	#dst = cv2.inpaint(img,th1,3,cv2.INPAINT_TELEA)

	# cv2.imshow("res", morph_img)
	# cv2.waitKey(0)
	cv2.destroyAllWindows()



