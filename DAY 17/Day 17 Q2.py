from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
alert = driver.switch_to.alert
print("Alert Message:", alert.text)
alert.accept()

driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
confirm = driver.switch_to.alert
confirm.dismiss()

driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
prompt = driver.switch_to.alert
prompt.send_keys("Selenium Automation")
prompt.accept()

result_text = driver.find_element(By.ID, "result").text
if "Selenium Automation" in result_text:
    print("Verification Successful:", result_text)
else:
    print("Verification Failed")

driver.quit()