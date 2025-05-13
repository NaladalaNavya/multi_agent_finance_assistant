import requests
from bs4 import BeautifulSoup
from newspaper import Article

class ScraperLoader:
    def extract_text_from_url(self, url: str) -> str:
        article = Article(url)
        article.download()
        article.parse()
        return article.text

    def extract_text_fallback(self, url: str) -> str:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.get_text()
