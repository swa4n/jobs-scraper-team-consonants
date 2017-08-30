import unittest
import sys
from scrapping import *
class TestScrapping(unittest.TestCase):
	def testkeyword(self):
		self.assertEqual(input_sanitizer('"Big Data"'), "big+data")
if __name__ == '__main__':
	unittest.main()
