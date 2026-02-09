from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# 1. Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # 2. Navigate to a stable practice site
    # This site is specifically designed for Selenium practice
    driver.get("https://formy-project.herokuapp.com/form")
    driver.maximize_window()

    # Create a Wait object (wait up to 10 seconds)
    wait = WebDriverWait(driver, 10)

    # --- 1. FILL TEXT BOXES ---
    # We wait for the first element to ensure the page is loaded
    first_name = wait.until(EC.presence_of_element_located((By.ID, "first-name")))
    first_name.send_keys("Anmol")

    driver.find_element(By.ID, "last-name").send_keys("Singhal")
    driver.find_element(By.ID, "job-title").send_keys("Developer")

    # --- 2. SELECT RADIO BUTTONS AND CHECKBOXES ---
    # Radio Button (High School)
    driver.find_element(By.ID, "radio-button-1").click()

    # Checkbox (Male)
    driver.find_element(By.ID, "checkbox-1").click()

    # --- 3. CHOOSE FROM DROP-DOWN USING SELECT CLASS ---
    dropdown_element = driver.find_element(By.ID, "select-menu")
    dropdown = Select(dropdown_element)
    dropdown.select_by_value("1")  # Selects '0-1' years of experience

    # --- 4. SUBMIT AND VERIFY ---
    # Clicking the Submit button
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary").click()

    # Wait for the success message on the next page
    success_banner = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert-success")))

    print(f"Result: {success_banner.text}")

    if "successfully submitted" in success_banner.text.lower():
        print("Test Passed: Form submitted and verified!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Keep browser open for 5 seconds to see the result
    time.sleep(5)
    driver.quit()