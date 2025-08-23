# scrolling.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# A special version of the site with infinite scrolling
URL = "http://quotes.toscrape.com/scroll"

def scrape_infinite_scroll():
    """
    Scrapes a page with infinite scrolling by repeatedly scrolling to the bottom.
    """
    print("--- Scraping an infinite scroll page ---")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    try:
        driver.get(URL)
        print("Opened the page.")

        # Get the initial number of quotes
        initial_quotes = driver.find_elements(By.CSS_SELECTOR, ".quote")
        print(f"Initially found {len(initial_quotes)} quotes.")
        
        scroll_attempts = 0
        max_scrolls = 5

        while scroll_attempts < max_scrolls:
            scroll_attempts += 1
            print(f"\n--- Scroll attempt #{scroll_attempts} ---")

            # Get the current scroll height
            last_height = driver.execute_script("return document.body.scrollHeight")
            
            # Execute JavaScript to scroll to the bottom of the page
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print("Scrolled to the bottom.")

            # Wait for new content to load
            time.sleep(2)

            # Check if new content has loaded by comparing scroll heights
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                print("No new content loaded. Reached the end of the page.")
                break
            
            quotes_count = len(driver.find_elements(By.CSS_SELECTOR, ".quote"))
            print(f"Total quotes found so far: {quotes_count}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
        print("\n--- Browser closed ---")

if __name__ == "__main__":
    scrape_infinite_scroll()