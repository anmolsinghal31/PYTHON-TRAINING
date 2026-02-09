import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from register_page import RegisterPage  # CRITICAL IMPORT
import time

driver = uc.Chrome()

try:
    driver.get("http://demo.opencart.com/")

    # Wait for the "Just a moment" screen
    print("ACTION: Solve the human verification if it appears...")
    WebDriverWait(driver, 60).until(EC.title_contains("Your Store"))

    # Execute Lab 5 Tasks
    rp = RegisterPage(driver)
    rp.navigate_to_register()

    # Part 3: Address Details
    rp.select_country_and_zone("India", "Telangana")

    # Part 4: Newsletter & Final Submit
    rp.fill_newsletter_and_privacy()

    # Final Validation
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Created"))
    print("Test Passed: Account Created successfully!")

except Exception as e:
    print(f"Test Stopped: {e}")

finally:
    time.sleep(5)
    driver.quit()