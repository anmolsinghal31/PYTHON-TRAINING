import pytest

# Requirement 1: Parameterization
@pytest.mark.parametrize("input_val, expected", [
    (1, 2),
    (5, 6),
    (10, 11)
])
def test_increment(input_val, expected):
    assert input_val + 1 == expected

# Requirement 4: Skip and Xfail
@pytest.mark.skip(reason="Functionality not yet implemented")
def test_future_feature():
    assert True

@pytest.mark.xfail(reason="Known bug in legacy system")
def test_known_bug():
    assert 1 == 2

# Using CLI and Config values
def test_environment_setup(browser, env_config):
    print(f"\nRunning on {browser} in {env_config} environment")
    assert browser in ["chrome", "firefox", "edge"]

def test_browser_setup(browser_name):
    print(f"\nTesting on browser: {browser_name}")
    assert browser_name in ["chrome", "firefox", "edge"]