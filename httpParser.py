# -*- coding: utf-8 -*-
import re

class HttpParser():
  def __init__(self):  # インスタンス生成時に自動的に呼ばれるメソッド
    pass

  def parse(self, httpStr):
    return httpStr

  def parseUrlPath(self, headerStr):
    return headerStr

  def parseContentLength(self, headerStr):
    return headerStr

  def devideHeaderBody(self, httpStr):
    MAX_SPLIT = 1
    # TODO Classにしたい。あとHeaderはのちのち（か、このメソッドで）分離させたい
    bodyAndHeader = re.split(r'\n\n', httpStr, MAX_SPLIT)
    strippedBodyAndHeader = [s.strip() for s in bodyAndHeader]
    return strippedBodyAndHeader

  def parseHttpHeader(self, httpStr):
    return httpStr

  def parseHttpBody(self, httpStr):
    return httpStr

