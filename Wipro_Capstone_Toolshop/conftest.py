import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

# This adds the custom command line flag '--browser'
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser: chrome, firefox, or edge")

@pytest.fixture
def driver(request):
    # Retrieve the browser name from the command line
    browser_name = request.config.getoption("--browser").lower()

    # Logic to switch between browsers
    if browser_name == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser_name == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    elif browser_name == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
    else:
        raise pytest.UsageError("--browser must be chrome, firefox, or edge")

    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    # Teardown: This ensures the browser always closes
    driver.quit()