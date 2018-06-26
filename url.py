#coding=utf-8
'''
the url structure of website
'''

from handlers.index import IndexHandler
from handlers.result import ResultHandler
from handlers.test import TestHandler

url = [
    (r'/', IndexHandler),
    (r'/res', ResultHandler),
    (r'/test*', TestHandler)
] 