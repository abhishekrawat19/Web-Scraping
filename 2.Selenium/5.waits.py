# waits.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

URL = "http://uitestingplayground.com/ajax"

def demonstrate_waits():
    """
    Demonstrates the importance of waits when dealing with AJAX content.
    """
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    # --- Implicit Wait ---
    # Tells Selenium to wait for a certain amount of time before throwing an exception.
    # It's a global setting and applies to all find_element calls.
    # Generally discouraged in favor of explicit waits.
    # driver.implicitly_wait(10) # Wait up to 10 seconds

    try:
        driver.get(URL)
        print("Opened AJAX testing page.")
        
        # Click the button that triggers an AJAX request
        ajax_button = driver.find_element(By.ID, "ajaxButton")
        ajax_button.click()
        print("Clicked the button to load data.")
        
        # --- The WRONG way: Using time.sleep() ---
        # This is bad because it's fixed. If the content loads faster, you waste time.
        # If it loads slower, your script breaks.
        # print("Waiting for 16 seconds with time.sleep()...")
        # time.sleep(16)
        
        # --- The RIGHT way: Explicit Wait ---
        # This is the recommended approach. It waits for a specific condition to be met
        # for a maximum amount of time. It polls the DOM, so it proceeds as soon
        # as the condition is true.
        print("Waiting for the content to appear using WebDriverWait...")
        
        # Create a WebDriverWait instance (wait up to 20 seconds)
        wait = WebDriverWait(driver, 20)
        
        # Define the condition to wait for: the element with class 'bg-success' is present.
        content_element = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".bg-success"))
        )
        
        print("Content has loaded successfully!")
        print(f"Loaded content text: '{content_element.text}'")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
        print("\n--- Browser closed ---")

if __name__ == "__main__":
    demonstrate_waits()