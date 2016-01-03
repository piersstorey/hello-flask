#!/usr/bin/python
# Default app tests

from app import APP
import pytest
import json
import unittest

class FlaskTestCase(unittest.TestCase):


	# Test default route
	def test_default_route(self):  
		tester = APP.test_client(self)
		response = tester.get('/', content_type='application/json')

		# Check 200 response from default route
		self.assertEqual(response.status_code, 200)

		# Check default route message output
		self.assertEqual(json.loads(response.data.decode('utf-8')), 
			{
			    "message" : "Hello pythonistic world"
			}
		)

		# Check number of characters in message
		response.json = json.loads(response.data.decode('utf-8'))
		self.assertEqual(len(response.json['message']), 23)