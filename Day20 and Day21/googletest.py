import pytest
import time
from Day20.driverfactory import getdriver


@pytest.mark.parametrize("browser", ["chrome", "brave"])
def test_google_search(browser):
    driver = getdriver(browser)
    try:
        driver.get("https://www.google.com/")

        # Find search box and type
        searchbox = driver.find_element("name", "q")
        searchbox.send_keys("Selenium Grid")
        searchbox.submit()

        # Give it a lot of time to load results
        time.sleep(5)

        # Print title to console for debugging
        print(f"Current Title: {driver.title}")

        # Verify if search term is in title
        assert "Selenium Grid" in driver.title
    finally:
        driver.quit()