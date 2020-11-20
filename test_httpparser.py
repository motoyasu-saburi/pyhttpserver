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

Hello"""

        expectResult = ["""GET / HTTP/1.1
Accept: image/gif, image/jpeg, */*
Host: example.com
Connection: Keep-Alive""",
"Hello"]
        self.assertEqual(hp.devideHeaderBody(normalHttpStr), expectResult)

    def test_parseUrlPath(self):
        normalHttpStr = """GET / HTTP/1.1
        Accept: image/gif, image/jpeg, */*
        Host: example.com
        Connection: Keep-Alive"""
        self.assertEqual(hp.parseUrlPath(normalHttpStr), "/")

        normalHttpStr2 = """GET /GET/HTTP/AAA HTTP/1.1
        Accept: image/gif, image/jpeg, */*
        Host: example.com
        Connection: Keep-Alive"""
        self.assertEqual(hp.parseUrlPath(normalHttpStr2), "/GET/HTTP/AAA")

if __name__ == '__main__':
    unittest.main()
