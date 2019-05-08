from PIL import Image
import glob
import re
import numpy as np 

"""
Function to take all the equalise images and remerge them back together to bring them back 
to the orginal image size and shape.  Reads all images in a file and merges them together,
uses a numpy vertical stack as an array to stack the images together.
"""

def remerge():
	# Read in the files to be remerged 
	files = sorted(glob.glob('../../Documents/ImageAnalysis.nosync/EqualisedImagesHistogram/*.bmp'),
		key=lambda x: tuple(map(int, re.findall(r'\d+', x))))
	# Read each individual image in the sliced image folder
	imgs = [Image.open(i) for img in files]
	# Sort the images so they are added in the correct order
	minImage = sorted([(np.sum(img.size), img.size ) for img in imgs])[0][1]
	# Stack each image in a vertical stack as an array until all images are used
	mergeImg = np.vstack( (np.asarray( i.resize(minImage,Image.ANTIALIAS) ) for i in imgs))
	mergeImg = Image.fromarray(mergeImg)
	# Save the image to file 
	mergeImg.save('FinalImage.bmp')