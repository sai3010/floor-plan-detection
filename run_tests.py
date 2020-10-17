import os
import cv2 
import unittest

class TestProject(unittest.TestCase):

    def test_file_exists(self):
        self.assertEqual(os.path.isfile("img.png"),True)

    def test_opencv_load(self):
        img = cv2.imread('img.png')
        self.assertEqual(img.any(),True)

if __name__ == '__main__':
    unittest.main()