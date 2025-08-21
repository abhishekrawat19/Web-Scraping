# bs4_example.py

import requests
from bs4 import BeautifulSoup

# URL of a simple website designed for scraping
URL = "http://quotes.toscrape.com/"

def scrape_quotes():
    """
    Scrapes quotes and authors from the website using requests and BeautifulSoup.
    """
    print(f"--- Scraping quotes from {URL} ---")
    try:
        # 1. Make a GET request to the URL
        response = requests.get(URL)
        response.raise_for_status()  # Check for request errors

        # 2. Parse the HTML content of the page
        # 'lxml' is a fast and efficient parser
        soup = BeautifulSoup(response.text, 'lxml')

        # 3. Find all quote containers
        # The quotes are inside a <div> with class="quote"
        quotes = soup.find_all('div', class_='quote')
        
        if not quotes:
            print("No quotes found. The website structure might have changed.")
            return

        print(f"Found {len(quotes)} quotes on the page.\n")

        # 4. Loop through each quote container and extract data
        for quote in quotes:
            # Find the text of the quote using a <span> with class="text"
            text = quote.find('span', class_='text').text
            
            # Find the author's name using a <small> with class="author"
            author = quote.find('small', class_='author').text
            
            # Find all tags associated with the quote
            tags = [tag.text for tag in quote.find_all('a', class_='tag')]
            
            print(f'"{text}"')
            print(f"- {author}")
            print(f"Tags: {', '.join(tags)}\n")

    except requests.exceptions.RequestException as e:
        print(f"Could not fetch the URL: {e}")
    except Exception as e:
        print(f"An error occurred during parsing: {e}")

if __name__ == "__main__":
    scrape_quotes()