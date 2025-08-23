# form_filling.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

LOGIN_URL = "http://quotes.toscrape.com/login"

def fill_and_submit_form():
    """
    Fills out a login form with dummy credentials and submits it.
    """
    print("--- Testing form filling with Selenium ---")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    try:
        # 1. Navigate to the login page
        driver.get(LOGIN_URL)
        print("Opened the login page.")

        # 2. Find the input fields for username and password
        username_input = driver.find_element(By.ID, "username")
        password_input = driver.find_element(By.ID, "password")

        # 3. Enter text into the fields using send_keys()
        print("Entering credentials...")
        username_input.send_keys("testuser123")
        time.sleep(1) # Pause to make it visible
        password_input.send_keys("password12345")
        time.sleep(1)

        # 4. Find the submit button and click it
        submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        print("Submitting the form...")
        submit_button.click()
        
        time.sleep(2) # Wait for the page to process the login

        # 5. Check for a result (e.g., a welcome message or an error)
        # On this site, a successful login shows a "Logout" link.
        # A failed login shows an error message.
        try:
            logout_link = driver.find_element(By.LINK_TEXT, "Logout")
            print("Login successful! Found 'Logout' link.")
        except:
            error_message = driver.find_element(By.CSS_SELECTOR, ".alert-danger")
            print(f"Login failed. Message: '{error_message.text}'")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
        print("\n--- Browser closed ---")

if __name__ == "__main__":
    fill_and_submit_form()