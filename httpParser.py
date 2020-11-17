# -*- coding: utf-8 -*-

class HttpParser():
  def __init__(self):  # インスタンス生成時に自動的に呼ばれるメソッド
    pass

  def parse(self, httpStr):
    return httpStr

  def pathParser(self, headerStr):
    return headerStr

  def contentLengthParser(self, headerStr):
    return headerStr

  def bodyParser(self, httpStr):
    return httpStr

