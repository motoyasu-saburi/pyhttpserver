# -*- coding: utf-8 -*-
from typing import Optional


class MttpRequest:
    httpHeader: str
    httpBody: str
    urlPath: str
    method: str # TODO enum 的にしたい
    splittedHeaders: dict[str, str]
    contentLength: Optional[str]
    contentType: Optional[str]

    def __init__(self, httpHeader, httpBody, urlPath, method, splittedHeaders, contentLength=None, contentType=None):
        self.httpHeader = httpHeader
        self.httpBody = httpBody
        self.urlPath = urlPath
        self.method = method
        self.splittedHeaders = splittedHeaders
        self.contentLength = contentLength
        self.contentType = contentType