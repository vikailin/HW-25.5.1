import pytest
import re
from settings import username
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_show_my_pets():
    assert pytest.driver.find_element('tag name', 'h1').text == "PetFriends"
    pytest.driver.find_element('css selector', 'a[href="/my_pets"]').click()
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located(('id', "all_my_pets")))
    assert pytest.driver.find_element('tag name', 'h2').text == username


def test_check_data_in_cards_of_my_pets(show_my_pets):
    pytest.driver.implicitly_wait(15)
    images = pytest.driver.find_elements('css selector', 'table.table.table-hover img')
    names = pytest.driver.find_elements('xpath', '//tbody/tr/td[1]')
    breeds = pytest.driver.find_elements('xpath', '//tbody/tr/td[2]')
    ages = pytest.driver.find_elements('xpath', '//tbody/tr/td[3]')

    image, name, breed, age = 0, 0, 0, 0
    for i in range(len(names)):
        try:
            assert images[i].get_attribute('src') != ''
        except AssertionError:
            image += 1
        try:
            assert names[i].text != ''
        except AssertionError:
            name += 1
        try:
            assert breeds[i].text != ''
        except AssertionError:
            breed += 1
        try:
            assert ages[i].text != ''
        except AssertionError:
            age += 1
    if image > 0:
        print(f'В {image} из {len(names)} карточек нет фото питомца')
    elif name > 0:
        print(f'В {name} из {len(names)} карточек нет имени питомца')
    elif breed > 0:
        print(f'В {breed} из {len(names)} карточек не указана порода питомца')
    elif age > 0:
        print(f'В {age} из {len(names)} карточек не указан возраст питомца')


def test_check_amount_of_my_pets(show_my_pets):
    user_info = pytest.driver.find_element('xpath', '/html/body/div[1]/div/div[@class=".col-sm-4 left"]').text
    my_pet_amount = list(map(int, re.compile(r'(?<=Питомцев: )\d+').findall(user_info)))
    pet_table_row_count = len(pytest.driver.find_elements('css selector', 'tbody tr'))
    assert my_pet_amount[0] == pet_table_row_count


def test_check_pets_have_different_names(show_my_pets):
    names = pytest.driver.find_elements('xpath', '//tbody/tr/td[1]')
    same_names_counter = 0

    for i in range(len(names)-1):
        for j in range(i+1, len(names)):
            if names[i].text == names[j].text:
                same_names_counter += 1
            else:
                pass

    try:
        assert same_names_counter == 0
    except:
        print(f'Найдено {same_names_counter} совпадений имен питомцев')




