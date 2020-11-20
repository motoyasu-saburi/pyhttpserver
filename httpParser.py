# -*- coding: utf-8 -*-
import re
from typing import *

class HttpParser():
  def __init__(self) -> None :  # インスタンス生成時に自動的に呼ばれるメソッド
    pass

  def parse(self, httpStr):
    return httpStr

  def parseUrlPath(self, headerStr: str) -> str:
      return re.search("\s.+\s(?=HTTP/.+)", headerStr).group().strip()

  def parseContentLength(self, headerStr):
    return headerStr

  # TODO list[str] を 専用のデータクラスにしたい
  def devideHeaderBody(self, httpStr: str) -> List[str]:
    MAX_SPLIT = 1
    # TODO Classにしたい。あとHeaderはのちのち（か、このメソッドで）分離させたい
    bodyAndHeader: List[str] = re.split(r'\n\n', httpStr, MAX_SPLIT)
    strippedBodyAndHeader = [s.strip() for s in bodyAndHeader]
    return strippedBodyAndHeader

  def parseHttpHeader(self, httpStr):
    return httpStr

  def parseHttpBody(self, httpStr):
    return httpStr

