
import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    r = requests.get(url, headers=headers, timeout=10)
    r.raise_for_status()
    return r.text

def extract_text_lines(html):
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text("\n", strip=True)
    return [line.strip() for line in text.splitlines() if line.strip()]
