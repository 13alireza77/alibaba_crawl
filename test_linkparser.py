from unittest import TestCase

from crawler import Crawler
from linkparser import Parser


class TestParser(TestCase):
    def test_parse(self):
        crawler = Crawler("https://www.w3schools.com/python")
        resp = crawler.crawl()
        parser = Parser(resp).parse("[a-z]{10}")
        self.assertIsNotNone(parser[0])
        self.assertIsNotNone(parser[1])
        self.failIf(len(parser[1]) < 1 or len(parser[0]) < 1)
