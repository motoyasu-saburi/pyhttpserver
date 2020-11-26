import unittest

from HttpRequest import HttpRequest
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

    def test_parseHttpHeader(self):
        normalHttpStr = """GET /GET/HTTP/AAA HTTP/1.1
        Accept: image/gif, image/jpeg, */*
        Host: example.com
        Connection: Keep-Alive"""

        expectDict = {'Accept': ' image/gif, image/jpeg, */*',
            'Connection': ' Keep-Alive',
            'Host': ' example.com'}
        self.assertEqual(hp.parseHttpHeader(normalHttpStr), expectDict)

    def test_parseContentType(self):
        normalHttps = {'Accept': ' image/gif, image/jpeg, */*',
                         'Connection': ' Keep-Alive',
                         'Content-Type': 'text/html',
                         'Content-Length': '30',
                         'Host': ' example.com'}
        self.assertEqual(hp.parseContentType(normalHttps), 'text/html')

        normalHttps2 = {'Accept': ' image/gif, image/jpeg, */*',
                          'Connection': ' Keep-Alive',
                          'Content-Type': 'text/html; charset=UTF-8',
                          'Content-Length': '30',
                          'Host': ' example.com'}
        self.assertEqual(hp.parseContentType(normalHttps2), 'text/html')

        noneContentType = {'Accept': ' image/gif, image/jpeg, */*',
                        'Host': ' example.com'}
        self.assertEqual(hp.parseContentType(noneContentType), None)

    def test_parseContentLength(self):
        normalHttps = {'Accept': ' image/gif, image/jpeg, */*',
                      'Connection': ' Keep-Alive',
                     'Content-Length': '30',
                      'Host': ' example.com'}
        self.assertEqual(hp.parseContentLength(normalHttps), 30)

        noneContentLengthHttps = {'Accept': ' image/gif, image/jpeg, */*',
                         'Connection': ' Keep-Alive',
                         'Host': ' example.com'}
        self.assertEqual(hp.parseContentLength(noneContentLengthHttps), None)

    def test_parseMethod(self):
        normalHttpStr = """GET /GET/HTTP/AAA HTTP/1.1
                Accept: image/gif, image/jpeg, */*
                Host: example.com
                Connection: Keep-Alive"""
        self.assertEqual(hp.parseMethod(normalHttpStr), "GET")

        abnormalMethodHttpStr = """GED /GET/HTTP/AAA HTTP/1.1
                Accept: image/gif, image/jpeg, */*
                Host: example.com
                Connection: Keep-Alive"""
        self.assertEqual(hp.parseMethod(abnormalMethodHttpStr), None)

    def test_parse(self):
        normalHttpStr = """GET / HTTP/1.1
        Accept: image/gif, image/jpeg, */*
        Host: example.com
        Connection: Keep-Alive

        Hello"""


        # TODO 落ちるテストの修正
        expectedHeader = """GET / HTTP/1.1
        Accept: image/gif, image/jpeg, */*
        Host: example.com
        Connection: Keep-Alive"""
        expectBody = "Hello"
        expectUrlPath = "/"
        expectSplittedHeader = {
            "Accept": "image/gif, image/jpeg, */*",
            "Host": "example.com",
            "Connection": "Keep-Alive"
        }
        expectMethod = "GET"
        expectContentLength = None
        expectContentType = None


        expectData = HttpRequest(expectedHeader, expectBody, expectUrlPath, expectMethod, expectSplittedHeader, expectContentLength, expectContentType)

        self.assertEqual(hp.parse(normalHttpStr), expectData)

if __name__ == '__main__':
    unittest.main()
