from concurrent.futures.thread import ThreadPoolExecutor

from crawler import Crawler
from linkparser import Parser
from collections import defaultdict


class Manager:
    def __init__(self, level: int, pattern: str):
        self.pattern = pattern
        self.level = level
        self.result = None

    def get_links_patterns(self, url):
        if url:
            resp = Crawler(url).crawl()
            if resp:
                links, patterns = Parser(resp).parse(self.pattern)
                self.result[url] += len(patterns)
                return links

    def manage_crawler(self, url):
        self.result = defaultdict(lambda: 0)
        links = self.get_links_patterns(url)
        for i in range(self.level - 1):
            with ThreadPoolExecutor(max_workers=50) as executor:
                res = executor.map(self.get_links_patterns, links)
                res = list(filter(None, res))
                links = [item for sublist in res for item in sublist if not None]
        return

    @property
    def dict_result(self):
        return dict(self.result)
