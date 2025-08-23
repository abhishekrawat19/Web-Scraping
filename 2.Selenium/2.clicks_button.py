# click_buttons.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

URL = "http://quotes.toscrape.com/"

def click_next_button():
    """
    Navigates to a webpage, clicks the 'Next' button, and verifies the page changed.
    """
    print("--- Testing button clicks with Selenium ---")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    try:
        # 1. Open the initial page
        driver.get(URL)
        print(f"Initial page URL: {driver.current_url}")

        # 2. Find the 'Next' button link
        # It's a <li> with class="next", containing an <a> tag.
        next_button = driver.find_element(By.CSS_SELECTOR, "li.next a")
        print("Found the 'Next' button.")

        # 3. Click the button
        next_button.click()
        print("Clicked the 'Next' button.")
        
        # Wait a moment for the new page to load
        time.sleep(2)

        # 4. Verify that the URL has changed
        print(f"New page URL: {driver.current_url}")
        if "/page/2/" in driver.current_url:
            print("Successfully navigated to the next page!")
        else:
            print("Failed to navigate to the next page.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
        print("\n--- Browser closed ---")

if __name__ == "__main__":
    click_next_button()