from selenium.webdriver import Chrome
import pytest

@pytest.mark.Sanity
def test_registration_valid_data():
    #path = "C:\\Users\\Ankit\\Downloads\\chromedriver_win32\\chromedriver.exe"
    path = "C:\\Users\\Ankit\\PycharmProjects\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get('https://www.thetestingworld.com/')
    driver.maximize_window()

@pytest.mark.Regression
def test_registration_invalid_data():
    path = "C:\\Users\\Ankit\\PycharmProjects\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get('https://www.thetestingworld.com/')
    driver.maximize_window()

@pytest.mark.Regression
def test_registration_invalid_data():
    path = "C:\\Users\\Ankit\\PycharmProjects\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get('https://www.thetestingworld.com/')
    driver.maximize_window()


