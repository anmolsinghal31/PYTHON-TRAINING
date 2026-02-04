from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 1. Opens a browser and navigates to example.com
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Initial Navigation
    driver.get("https://www.example.com")
    driver.maximize_window()
    # 4. Prints the page title after each navigation
    print(f"Initial Page Title: {driver.title}")
    time.sleep(2)

    # 2. Navigates to another page (using Google as the second page)
    driver.get("https://www.google.com")
    print(f"Second Page Title: {driver.title}")
    time.sleep(2)

    # 3. Uses back(), forward(), and refresh()

    # Go Back to Example.com
    driver.back()
    print(f"After Back(), Title is: {driver.title}")
    time.sleep(2)

    # Go Forward to Google.com
    driver.forward()
    print(f"After Forward(), Title is: {driver.title}")
    time.sleep(2)

    # Refresh the page
    driver.refresh()
    print(f"After Refresh(), Title is: {driver.title}")
    time.sleep(2)

finally:
    # 5. Closes the browser
    driver.quit()
    print("Browser closed successfully.")