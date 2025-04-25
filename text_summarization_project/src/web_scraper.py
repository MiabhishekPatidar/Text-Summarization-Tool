import requests
from bs4 import BeautifulSoup

def fetch_article_text(url):
    """
    Fetches the main content from a news article.
    :param url: News article URL
    :return: Extracted text
    """
    response = requests.get(url)
    if response.status_code != 200:
        return "Failed to fetch article."

    soup = BeautifulSoup(response.text, "html.parser")

    # Remove unwanted elements
    for tag in soup(["script", "style", "header", "footer", "nav", "aside", "form", "button"]):
        tag.extract()

    paragraphs = soup.find_all('p')
    text = ' '.join([p.get_text() for p in paragraphs])

    return text.strip()
