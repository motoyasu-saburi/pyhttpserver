# -*- coding: utf-8 -*-
import re
from typing import *

class HttpParser():
  def __init__(self) -> None :  # インスタンス生成時に自動的に呼ばれるメソッド
    pass

  def parse(self, httpStr):
    pass
    return httpStr

  def parseUrlPath(self, headerStr: str) -> str:
      return re.search("\s.+\s(?=HTTP/.+)", headerStr).group().strip()

  def parseContentLength(self, headerStr):
    pass
    return headerStr

  # TODO list[str] を 専用のデータクラスにしたい
  def devideHeaderBody(self, httpStr: str) -> List[str]:
    MAX_SPLIT = 1
    # TODO Classにしたい。あとHeaderはのちのち（か、このメソッドで）分離させたい
    bodyAndHeader: List[str] = re.split(r'\n\n', httpStr, MAX_SPLIT)
    strippedBodyAndHeader = [s.strip() for s in bodyAndHeader]
    return strippedBodyAndHeader

  def parseHttpHeader(self, httpStr: str) -> Dict[str, str]:
    MAX_SPLIT = 1 # HTTP は Key : Value 形式のため、初回のみ
    httpHeaderLines: List[str] = httpStr.split("\n")[1:] # 最初の行は "GET / HTTP/1.1" なので無視
    httpLinesArr: List[List[str]] = [line.strip().split(":", MAX_SPLIT) for line in httpHeaderLines]
    httpLinesDict = {k: v for (k, v) in httpLinesArr}
    return httpLinesDict

  def parseHttpBody(self, httpStr):
    return httpStr

