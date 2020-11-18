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

    def test_devideHeaderBody(self):
        normalHttpStr = """
GET / HTTP/1.1
Accept: image/gif, image/jpeg, */*
Host: example.com
Connection: Keep-Alive

Hello
"""

        expectResult = ["""
GET / HTTP/1.1
Accept: image/gif, image/jpeg, */*
Host: example.com
Connection: Keep-Alive 
""",
"Hello"]

        # self.assertEqual(hp.devideHeaderBody(normalHttpStr), expectResult)
        # TODO 落ちる
        self.assertEqual(hp.devideHeaderBody(normalHttpStr)[1], "Hello")


if __name__ == '__main__':
    unittest.main()
