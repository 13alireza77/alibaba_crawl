import re

from bs4 import BeautifulSoup


class Parser:
    def __init__(self, html):
        self.html = html

    def parse(self, pattern):
        links = []
        patterns = re.findall(pattern, self.html)
        soup = BeautifulSoup(self.html, "html.parser")
        for link in soup.findAll('a'):
            temp = link.get('href')
            if temp:
                if temp.startswith("http"):
                    links.append(temp)
        return links, patterns
