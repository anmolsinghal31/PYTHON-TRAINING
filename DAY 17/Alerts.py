from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://letcode.in/alert")
driver.find_element(By.ID,"accept").click()
alert=driver.switch_to.alert
print(alert.text)
alert.accept()
