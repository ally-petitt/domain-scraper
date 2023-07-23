##########################################################
# Name: domain-scraper.py
# Description: Python script to scrape domains from a URL
# Author: Ally Petitt
##########################################################

import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def get_linked_domains(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception if request fails

        soup = BeautifulSoup(response.content, 'html.parser')
        linked_domains = set()

        for link in soup.find_all('a', href=True):
            domain = urlparse(link['href']).netloc
            if domain and domain != urlparse(url).netloc:
                linked_domains.add(domain)

        return linked_domains

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return set()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python program.py <url>")
    else:
        url = sys.argv[1]
        linked_domains = get_linked_domains(url)
        for domain in linked_domains:
            print(domain)
