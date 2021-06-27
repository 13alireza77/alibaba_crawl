import requests


class Crawler:
    def __init__(self, url: str):
        self.url = url

    def crawl(self):
        try:
            resp = requests.get(self.url, timeout=5)
            return resp.text
        except Exception as e:
            # print(e)
            return
