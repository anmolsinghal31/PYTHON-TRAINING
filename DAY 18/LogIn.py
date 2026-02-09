from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize driver
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)

# Open URL
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Explicit Wait for the username field
element = wait.until(EC.element_to_be_clickable((By.NAME, "username")))
element.send_keys("Admin")

# Input password and click login
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Keep browser open for 5 seconds before closing
time.sleep(5)
driver.quit()