import unittest
from clientApp import get_time
from webService import get_time_str
import json

class TestClientMethods(unittest.TestCase):

    def test_good_time(self):
        timeOrig = '2019-04-08T22:42:50'
        val = json.dumps({ "currentTime":timeOrig }).encode()
        self.assertEqual(get_time(val), timeOrig)

    def test_bad_time(self):
        timeOrig = '2019-400-8T22:42:50'
        val = json.dumps({ "currentTime":timeOrig }).encode()
        self.assertEqual(get_time(val), 'Invalid format or not a timestamp')

    def test_no_key(self):
        val = json.dumps({ "oldTime": 'any thing'}).encode()
        self.assertEqual(get_time(val), 'No currentTime key')

    def test_bad_json(self):
        self.assertEqual(get_time({'test':0}), 'Failed to decode json')

if __name__ == '__main__':
    unittest.main()
