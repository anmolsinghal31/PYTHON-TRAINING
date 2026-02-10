from selenium import webdriver

# THIS MUST MATCH YOUR HUB COMMAND (localhost)
GRIDURL = "http://localhost:4444"


def getdriver(browser):
    if browser == "chrome" or browser == "brave":
        options = webdriver.ChromeOptions()
        if browser == "brave":
            options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

        # Helps bypass bot detection
        options.add_argument("--disable-blink-features=AutomationControlled")
    else:
        raise ValueError("Browser not supported")

    # Connect to the Hub using the localhost URL
    driver = webdriver.Remote(command_executor=GRIDURL, options=options)
    driver.maximize_window()
    return driver