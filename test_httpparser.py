import unittest
from httpparser import HttpParser

hp = HttpParser()

class MyTestCase1(unittest.TestCase):

    # Only use setUp() and tearDown() if necessary

    #def setUp(self):
    #    ... code to execute in preparation for tests ...

    #def tearDown(self):
    #    ... code to execute to clean up after tests ...

    def test_httpParser(self):
        self.assertEqual(hp.bodyParser(), "hoge")

if __name__ == '__main__':
    unittest.main()
