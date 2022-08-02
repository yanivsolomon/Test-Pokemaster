from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from selenium.webdriver.support.color import Color


# setup and teardown (fixture)
@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    print("test completed")

# valid title test
def test_title(test_setup):
    driver.get("https://poke-master.000webhostapp.com/index.html")
    x = driver.title
    assert x == "Pokémaster!"

# INVALID title test
def test_title_invalid(test_setup):
    driver.get("https://poke-master.000webhostapp.com/index.html")
    x = driver.title
    assert x == "Our invalid input"

# valid logo test (color)
def test_logo_color_valid(test_setup):
    driver.get("https://poke-master.000webhostapp.com/index.html")
    # logo color test - valid result should be ffff00
    color = driver.find_element_by_xpath("//a[contains(text(),'Pokémaster!')]").value_of_css_property('color')
    # after fetching rgba were converting into hex for easier reading
    hex = Color.from_string(color).hex
    assert hex == '#ffff00'

# INVALID logo test (color)
def test_logo_color_invalid(test_setup):
    driver.get("https://poke-master.000webhostapp.com/index.html")
    # logo color test - valid result should be ffff00
    color = driver.find_element_by_xpath("//a[contains(text(),'Pokémaster!')]").value_of_css_property('color')
    # after fetching rgba were converting into hex for easier reading
    hex = Color.from_string(color).hex
    assert hex == '#fff066'

# valid logo test (size)
def test_logo_size_valid(test_setup):
    # logo size test - valid result should be 36 height and 163 width
    driver.get("https://poke-master.000webhostapp.com/index.html")
    size = driver.find_element_by_xpath("//a[contains(text(),'Pokémaster!')]").size
    assert size == {'height': 36, 'width': 163}


# INVALID logo test (size)
def test_logo_size_invalid(test_setup):
    driver.get("https://poke-master.000webhostapp.com/index.html")
    # logo size test - valid result should be 36 height and 163 width
    size = driver.find_element_by_xpath("//a[contains(text(),'Pokémaster!')]").size
    assert size == {'height': 50, 'width': 50}

# valid background image URL test
def test_bg_image_valid(test_setup):
    driver.get("https://poke-master.000webhostapp.com/index.html")
    bg_image = driver.find_element_by_xpath("//body/div[1]").value_of_css_property("background-image")
    assert bg_image == 'url("https://assets.pokemon.com//assets/cms2/img/misc/virtual-backgrounds/sword-shield/pokemon-in-the-wild.png")'

# INVALID background image URL test
def test_bg_image_invalid(test_setup):
    driver.get("https://poke-master.000webhostapp.com/index.html")
    bg_image = driver.find_element_by_xpath("//body/div[1]").value_of_css_property("background-image")
    assert bg_image == 'url("https://notrealurl.png")'


# valid functional testing (correct number of clicks for every pokemon)
def test_pokemaster_valid(test_setup):
    driver.get("https://poke-master.000webhostapp.com/index.html")
    # clicking on start a game btn
    start_game_btn = driver.find_element_by_xpath('//input[@type="button"]')
    start_game_btn.click()
    time.sleep(2)

    # POKEMON NUMBER 1
    first_pokeball = driver.find_element_by_id('pokeball')
    first_pokeball.click()
    time.sleep(2)
    # get the first pokemon element (using astrochains to perform multiple clicks)
    element = driver.find_element_by_id('monster')
    # create action chain object
    action = ActionChains(driver)
    # click the item
    action.click(on_element=element)
    action.double_click(on_element=element)
    action.click(on_element=element)
    # perform the operation
    action.perform()

    # POKEMON NUMBER 2
    time.sleep(2)
    link = driver.find_element_by_id('pokeball')
    link.click()
    time.sleep(2)
    # get element
    element = driver.find_element_by_id('monster')
    # create action chain object
    action = ActionChains(driver)
    # click the item
    action.double_click(on_element=element)
    action.double_click(on_element=element)
    action.click(on_element=element)
    # perform the operation
    action.perform()

    # POKEMON NUMBER 3
    time.sleep(2)
    link = driver.find_element_by_id('pokeball')
    link.click()
    time.sleep(2)
    # get element
    element = driver.find_element_by_id('monster')
    # create action chain object
    action = ActionChains(driver)
    # click the item --- evee
    action.double_click(on_element=element)
    action.double_click(on_element=element)
    action.double_click(on_element=element)
    # perform the operation
    action.perform()

    # POKEMON NUMBER 4
    time.sleep(2)
    link = driver.find_element_by_id('pokeball')
    link.click()
    # get element
    element = driver.find_element_by_id('monster')
    # create action chain object
    action = ActionChains(driver)
    # click the item
    action.double_click(on_element=element)
    action.double_click(on_element=element)
    action.double_click(on_element=element)
    action.click(on_element=element)
    # perform the operation
    action.perform()

    # POKEMON NUMBER 5
    time.sleep(2)
    link = driver.find_element_by_id('pokeball')
    link.click()
    # get element
    element = driver.find_element_by_id('monster')
    # create action chain object
    action = ActionChains(driver)
    # click the item  AGAS
    action.double_click(on_element=element)
    action.double_click(on_element=element)
    action.double_click(on_element=element)
    action.double_click(on_element=element)
    # perform the operation
    action.perform()

    # POKEMON NUMBER 6
    time.sleep(2)
    link = driver.find_element_by_id('pokeball')
    link.click()
    # get element
    element = driver.find_element_by_id('monster')
    # create action chain object
    action = ActionChains(driver)
    # click the item
    action.double_click(on_element=element)
    action.double_click(on_element=element)
    action.double_click(on_element=element)
    action.double_click(on_element=element)
    action.click(on_element=element)
    # perform the operation
    action.perform()

    # POKEMON NUMBER 7
    time.sleep(2)
    link = driver.find_element_by_id('pokeball')
    link.click()
    # get element
    element = driver.find_element_by_id('monster')
    # create action chain object
    action = ActionChains(driver)
    # click the item
    action.double_click(on_element=element)
    action.double_click(on_element=element)
    action.double_click(on_element=element)
    action.double_click(on_element=element)
    action.double_click(on_element=element)
    # perform the operation
    action.perform()

# INVALID functional testing - incorrect number of clicks (3 instead of 4)
# the expected result should be the failure page
def test_pokemaster_invalid(test_setup):
    driver.get("https://poke-master.000webhostapp.com/index.html")
    # clicking on start a game btn
    start_game_btn = driver.find_element_by_xpath('//input[@type="button"]')
    start_game_btn.click()
    time.sleep(2)

    # POKEMON NUMBER 1
    first_pokeball = driver.find_element_by_id('pokeball')
    first_pokeball.click()
    time.sleep(2)
    # get the first pokemon element (using astrochains to perform multiple clicks)
    element = driver.find_element_by_id('monster')
    # create action chain object
    action = ActionChains(driver)
    # click the item
    action.click(on_element=element)
    action.double_click(on_element=element)
        # perform the operation
    action.perform()

    time.sleep(7)
