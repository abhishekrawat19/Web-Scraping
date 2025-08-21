# selenium_intro.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# URL of a simple website
URL = "http://quotes.toscrape.com/"

def basic_scrape():
    """
    Opens a webpage, extracts the text of the first quote, and closes the browser.
    """
    print("--- Starting basic Selenium scrape ---")
    
    # Automatically download and manage the ChromeDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    try:
        # 1. Open the webpage
        driver.get(URL)
        print(f"Opened page with title: '{driver.title}'")

        # 2. Find the first quote element
        # We are using CSS_SELECTOR to find a <span> tag with the class "text"
        first_quote = driver.find_element(By.CSS_SELECTOR, "span.text")

        # 3. Extract its text content
        print(f"\nFirst quote found: '{first_quote.text}'")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # 4. Close the browser window
        # It's important to quit the driver to free up resources.
        time.sleep(2) # Wait 2 seconds to see the browser action
        driver.quit()
        print("\n--- Browser closed ---")


if __name__ == "__main__":
    basic_scrape()