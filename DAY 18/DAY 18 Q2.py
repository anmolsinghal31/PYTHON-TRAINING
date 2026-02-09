from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the driver
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

try:
    wait = WebDriverWait(driver, 10)

    # 1 & 2: Trigger JavaScript Alert, print message, and Accept
    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
    alert = wait.until(EC.alert_is_present())
    print(f"Alert Message: {alert.text}")
    alert.accept()

    # 3: Dismiss a Confirmation Pop-up
    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
    confirm_alert = wait.until(EC.alert_is_present())
    confirm_alert.dismiss()  # Clicks 'Cancel'

    # 4: Enter text in a Prompt Alert and Accept
    driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
    prompt_alert = wait.until(EC.alert_is_present())
    prompt_text = "Selenium is fun!"
    prompt_alert.send_keys(prompt_text)
    prompt_alert.accept()

    # 5: Verify the result displayed on the page
    result_element = driver.find_element(By.ID, "result")
    expected_result = f"You entered: {prompt_text}"

    if expected_result in result_element.text:
        print(f"Verification Success: {result_element.text}")
    else:
        print(f"Verification Failed. Found: {result_element.text}")

finally:
    driver.quit()