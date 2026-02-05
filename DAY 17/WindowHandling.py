from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

# Verify your internet connection and the spelling of this URL
driver.get("https://letcode.in/window")
time.sleep(5)

# Click the button that opens multiple windows
driver.find_element(By.ID, "multi").click()

# Get all window handles
windows = driver.window_handles

for child in windows:
    driver.switch_to.window(child)
    # A brief sleep to allow the URL to fully resolve in the new window
    time.sleep(2)
    print("Window URL:", driver.current_url)

# Clean up and close all windows
driver.quit()