from selenium.webdriver import Chrome
import pytest


@pytest.fixture(scope="module")
def setPath():
    global driver
    path = "C:\\Users\\Ankit\\PycharmProjects\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    yield
    driver.close()


def test_registration_valid_data(setPath):
    driver.get('https://www.thetestingworld.com/')
    driver.maximize_window()


def test_registration_invalid_data(setPath):
    driver.get('https://www.thetestingworld.com/')
    driver.maximize_window()


def test_registration_invalid_data(setPath):
    driver.get('https://www.thetestingworld.com/')
    driver.maximize_window()
