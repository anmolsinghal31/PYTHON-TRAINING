from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException

driver = webdriver.Chrome()

# 1. Implicit Wait
driver.implicitly_wait(10)

driver.get("https://www.google.com")

try:
    # 2. Explicit Wait (Fixed method name: element_to_be_clickable)
    explicit_wait = WebDriverWait(driver, 10)
    search_box = explicit_wait.until(EC.element_to_be_clickable((By.NAME, "q")))

    # 3. Fluent Wait (Fixed method name: presence_of_element_located)
    fluent_wait = WebDriverWait(driver, 20, poll_frequency=1,
                                ignored_exceptions=[ElementNotVisibleException,
                                                    ElementNotSelectableException])

    element = fluent_wait.until(EC.presence_of_element_located((By.NAME, "q")))

    # 4. Success Message
    print("Element is available for interaction!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()