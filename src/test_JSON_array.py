import unittest
import sys
import requests
import requests_mock
from scrapping import *
class TestJSONArray(unittest.TestCase):
	def testjson(self):
		session = requests.Session()
		adapter = requests_mock.Adapter()
		session.mount('mock', adapter)
		adapter.register_uri('GET', 'mock://test.com', text='{"hi":"hello"}')
		json_obj={"hi":"hello"}
		self.assertEqual(convert_to_json_array(session.get('mock://test.com')), json_obj)
if __name__ == '__main__':
	unittest.main()
