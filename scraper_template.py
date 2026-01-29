# Sentinel News Scraper - Starter Template
# Week 2: Data Acquisition
# Complete the TODOs to collect news articles respectfully.

import json
import time

import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "SentinelBot/1.0"}


class NewsScraper:
    def __init__(self, wait_seconds=1.0):
        self.wait_seconds = wait_seconds

    def fetch(self, url):
        # TODO: Fetch a URL with polite headers and basic error handling.
        # 1. Use requests.get with HEADERS and timeout
        # 2. Return response.text on success
        # 3. Print a helpful message and return None on failure
        raise NotImplementedError

    def parse(self, html, url):
        # TODO: Parse HTML and return a dictionary with title, content, and published date.
        # 1. Create BeautifulSoup object
        # 2. Try multiple selectors for title, content, and date
        # 3. Remove script/style tags from content
        # 4. Return a dictionary with keys: url, title, content, published
        raise NotImplementedError

    def is_valid(self, article):
        # TODO: Validate title, content length (>= 100), and URL format.
        raise NotImplementedError

    def scrape_many(self, urls):
        # TODO: Loop through URLs, wait between requests, return valid articles.
        # 1. Iterate through URLs with enumerate for progress output
        # 2. Call fetch -> parse -> validate
        # 3. Append valid articles to a list
        # 4. Sleep self.wait_seconds after each URL
        raise NotImplementedError


def save_articles(path, articles):
    # TODO: Write articles to JSON with generated_at timestamp.
    # Hint: use time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    raise NotImplementedError


if __name__ == "__main__":
    scraper = NewsScraper(wait_seconds=1.0)

    TEST_URLS = [
        "https://news.example.com/placeholder-1",
        "https://news.example.com/placeholder-2",
    ]

    # TODO: Replace TEST_URLS with real news article URLs
    # articles = scraper.scrape_many(TEST_URLS)
    # save_articles("data/articles.json", articles)
