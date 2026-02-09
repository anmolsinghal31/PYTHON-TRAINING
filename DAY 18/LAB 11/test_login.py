from selenium import webdriver
from login_page import LoginPage

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")

login = LoginPage(driver)
login.enter_username("test@example.com")
login.enter_password("12345")
login.click_login()

print("Login attempt complete. Title is:", driver.title)
driver.quit()