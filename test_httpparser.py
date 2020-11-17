import unittest
from httpparser import HttpParser

hp = HttpParser()

class MyTestCase1(unittest.TestCase):

    # Only use setUp() and tearDown() if necessary

    def setUp(self):
        # 初期化処理
        pass

    def tearDown(self):
        # 終了処理
        pass

    def test_httpParser(self):
        self.assertEqual(hp.bodyParser(" "), " ")

if __name__ == '__main__':
    unittest.main()
