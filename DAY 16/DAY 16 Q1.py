from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Setup Browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")
    driver.maximize_window()

    # Step 1: Object Identification (Using your Morning Sheet locators)
    # Generate random data to ensure a fresh registration
    unique_id = random.randint(10000, 99999)
    test_email = f"ninja_test_{unique_id}@gmail.com"

    # Locators from your sheet
    driver.find_element(By.ID, "input-firstname").send_keys("Test")
    driver.find_element(By.NAME, "lastname").send_keys("User")
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='E-Mail']").send_keys(test_email)
    driver.find_element(By.XPATH, "//input[@id='input-telephone']").send_keys("12345678")

    driver.find_element(By.ID, "input-password").send_keys("Pass1234!")
    driver.find_element(By.ID, "input-confirm").send_keys("Pass1234!")

    # Step 2: Interaction (Radio & Checkbox)
    driver.find_element(By.XPATH, "//input[@name='newsletter'][@value='0']").click()
    driver.find_element(By.NAME, "agree").click()

    # Click Submit
    driver.find_element(By.XPATH, "//input[@value='Continue']").click()

    # Step 3: Validation (The "Question 3" Solution)
    # We use a Wait to ensure we don't grab the 'Qafox' logo by mistake
    wait = WebDriverWait(driver, 10)

    # This specifically looks for the H1 inside the #content div
    success_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='content']/h1")))
    success_text = success_element.text

    if success_text == "Your Account Has Been Created!":
        print(f"Validation Passed for {test_email}!")
    else:
        print(f"Validation Failed. Heading found: {success_text}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    time.sleep(5)
    driver.quit()