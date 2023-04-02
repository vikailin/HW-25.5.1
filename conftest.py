import pytest
from settings import email, password
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def authorization():
    pytest.driver = webdriver.Chrome('HW-25.5.1./chromedriver.exe')
    pytest.driver.implicitly_wait(10)
    pytest.driver.get('http://petfriends.skillfactory.ru/login')
    pytest.driver.find_element('id', 'email').send_keys(email)
    pytest.driver.find_element('id', 'pass').send_keys(password)
    pytest.driver.find_element('css selector', 'button[type="submit"]').click()

    yield

    pytest.driver.quit()


@pytest.fixture()
def show_my_pets():
    pytest.driver.find_element('css selector', 'a[href="/my_pets"]').click()
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located(('id', "all_my_pets")))
