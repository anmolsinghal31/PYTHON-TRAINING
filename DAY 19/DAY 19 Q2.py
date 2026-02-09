from selenium import webdriver
from selenium.webdriver.common.options import ArgOptions

# Define the Grid Hub URL (default local address)
grid_url = "http://localhost:4444/wd/hub"

# 2. List of browsers to test on
browsers = [
    webdriver.ChromeOptions(),
    webdriver.FirefoxOptions(),
    webdriver.EdgeOptions()
]


def run_grid_test(options):
    try:
        # 1. Connect to Selenium Grid using RemoteWebDriver
        driver = webdriver.Remote(
            command_executor=grid_url,
            options=options
        )

        # 3. Navigate to a website and verify the page title
        driver.get("https://www.google.com")
        page_title = driver.title

        # 4. Prints browser name and platform for each execution
        capabilities = driver.capabilities
        print(f"Browser: {capabilities['browserName']}")
        print(f"Platform: {capabilities['platformName']}")
        print(f"Verified Title: {page_title}")
        print("-" * 30)

        driver.quit()

    except Exception as e:
        print(f"Could not connect to Grid for {options.capabilities['browserName']}: {e}")


# Execute the same test on multiple browsers
for browser_option in browsers:
    run_grid_test(browser_option)