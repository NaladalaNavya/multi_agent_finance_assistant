import requests
from bs4 import BeautifulSoup

class ScrapingAgent:
    def scrape_earnings_filings(self, url: str):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.get_text()
