import sliceImage
import unittest
import cv2
import os

"""
UNIT TESTS
"""
class TestImageSize(unittest.TestCase):

	def test_imageloadingoutsideoffolder(self):
		sliceImage.image_slice('../../Documents/1.bmp',\
			os.path.join('../../Documents/ImageAnalysis.nosync/testLoad'))
		try:
			self.assertTrue(cv2.imread('../../Documents/ImageAnalysis.nosync/testLoad/1.bmp'))
		except Exception as e:
			return False
	
	def test_savedimagesizeHeight(self):
		image = cv2.imread('../../Documents/ImageAnalysis.nosync/sliceImage/1.bmp')
		h, w = image.shape[:2]
		self.assertEqual(h, 1500)

	def test_savedimagesizeWidth(self):
		image = cv2.imread('../../Documents/ImageAnalysis.nosync/sliceImage/1.bmp')
		h, w = image.shape[:2]
		self.assertNotEqual(w, 1500)

	


if __name__ == '__main__':
    unittest.main()