import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Type of browser: chrome, firefox, or edge"
    )

@pytest.fixture
def browser(request): # Changed from browser_name to browser
    return request.config.getoption("--browser")

@pytest.fixture
def env_config(pytestconfig):
    return pytestconfig.getini("env_name")