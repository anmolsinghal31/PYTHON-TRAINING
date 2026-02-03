import pytest
from selenium import webdriver


class TestTc001():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_tc001(self):
        # 1. Navigates to the URL
        expectedurl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.driver.get(expectedurl)
        self.driver.set_window_size(1169, 824)

        # 2. PRINTS the page title and URL (The specific task requirement)
        print("\nPage Title is:", self.driver.title)
        print("Current URL is:", self.driver.current_url)