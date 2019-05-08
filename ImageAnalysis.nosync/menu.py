import os
import sliceImage
import RGBgraphs
import compare
import normaliseUnClass
import classImage
import brightness
import watershed
import normaliseByClass
import normaliseHistogram
import verticalLines
import merge
import thinLines
import bigLines
import tests
import unittest

"""
Run the command line menu and read user input.  From the user input, run the revelvant program
functionality.
"""

if __name__ == '__main__':
	cmdInput = True
	while cmdInput:
		print("""
	1. Split input image

	2. Create RGB Graphs for each image

	3. Show Comparisions between graphs and images

	4. Normalise Image without classification

	5. Thresholding Classification Accuracy

	6. Brightness Comparisons 

	7. Watershed segmentation

	8. Normalising by Bitwise operations

	9. Normalising by Histogram Matching

	10. Removal of vertical artefact lines

	11. Fine vertical line detection

	12. Vertical illumination line detection 

	13. Merge the images

	T = Run Tests
			
	q = quit
			""")
		cmdInput = input("Please enter your choice:").upper()
		
		if cmdInput == "1":
			imageChoice = input("""
If you would like to load an image outside of this folder please do so in a format like so: ../../Documents/IMAGE_NAME
else please enter the image name you would like to split:""")
			if imageChoice != None:
				print("Starting image slice...")
				sliceImage.image_slice(imageChoice + ".bmp", 
					os.path.join('../../Documents/ImageAnalysis.nosync/sliceImage'))
				print("Image Sliced!")
			elif imageChoice == None:
				print("No image selected")
		elif cmdInput == "2":
			print("Creating graphs...")
			RGBgraphs.rgbGraphs()
			print("Graphs Created!")
		elif cmdInput == "3":
			chooseImage = input("Choose the image to compare:")
			print("Creating Comparisions...")
			compare.compare(chooseImage)
			print("Comparision complete!")
		elif cmdInput == "4":
			print("Normailising...")
			normaliseClass.normailsiationWithoutClassification()
			print("Images normalised!")
		elif cmdInput == "5":
			print("Classifying and normlising images...")
			classImage.classImage()
			print("Classified!")
		elif cmdInput == "6":
			brightness.brightness()
		elif cmdInput == "7":
			watershed.watershed()
		elif cmdInput == "8":
			print("Normailising...")
			normaliseByClass.normaliseByClass()
			print("Images normalised!")
		elif cmdInput == "9":
			print("Normailising...")
			normaliseHistogram.normaliseImages()
			print("Images normalised!")
		elif cmdInput == "10":
			print("Reducing vertical lines....")
			verticalLines.verticalLines()
			print("Lines reduced!")
		elif cmdInput == "11":
			print("Reducing fine vertical lines....")
			thinLines.thinLines()
			print("Lines reduced!")
		elif cmdInput == "12":
			print("Reducing vertical illumination vertical lines....")
			bigLines.bigLines()
			print("Lines reduced!")
		elif cmdInput == "13":
			print("Merging...")
			merge.remerge()
			print("Merged!")
		elif (cmdInput == "T"):
			suite = unittest.TestLoader().loadTestsFromModule(tests)
			unittest.TextTestRunner(verbosity=2).run(suite)
		elif cmdInput == "Q":
			break



	



