from unittest import TestCase

from crawler import Crawler


class TestCrawler(TestCase):
    def test_crawl(self):
        crawler = Crawler("https://www.w3schools.com/python")
        self.assertIsInstance(crawler.crawl(), str)
