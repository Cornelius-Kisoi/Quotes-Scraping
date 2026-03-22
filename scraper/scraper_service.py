import requests
from bs4 import BeautifulSoup
from .models import Quote

def scrape_quotes(pages=3):
    base_url = "https://quotes.toscrape.com/page/{}/"

    for page in range(1, pages + 1):
        url = base_url.format(page)
        response = requests.get(url)

        if response.status_code != 200:
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        quote_blocks = soup.find_all('div', class_='quote')

        for block in quote_blocks:
            text = block.find('span', class_='text').text
            author = block.find('small', class_='author').text
            tags = [tag.text for tag in block.find_all('a', class_='tag')]

            if not Quote.objects.filter(text=text).exists():
                Quote.objects.create(
                text=text,
                author=author,
                tags=",".join(tags)
            )
