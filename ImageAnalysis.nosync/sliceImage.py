from PIL import Image
import os
import math

"""
image_slice is a function that is used to take the input image that the user defines
and split the image.  The function takes the image and splits the image vertically 
by 1500 pixels.
"""

def image_slice(image_path, outdir):
	Image.MAX_IMAGE_PIXELS = None # Set the maximum number of pixels to None - allows image to read
	img = Image.open(image_path) # Open the image defined by the user

	w,h = img.size # Find the width and the height of the image

	upperLimit = 0 
	leftLimit = 0

	sliceHeight = int(math.ceil(h/1500)) #find the height of the image and divide by 1500

	count = 1

	# For each image slice in the sliced image height then if the count is equal to the slice height
	# then make h equal to the lower height
	for imageSlice in range(sliceHeight):
	    if count == sliceHeight:
	        lower = h
	    else: 
	        lower = int(count * 1500)

	    boundingBox = (leftLimit,upperLimit,w,lower) # Create a 'box' that slides over the image
	    currentImageSlice = img.crop(boundingBox) # Crop the current slice based on the bounding box
	    upperLimit += 1500 

	    currentImageSlice.save(os.path.join(outdir, str(count)+ ".bmp")) # Save the image
	    count += 1