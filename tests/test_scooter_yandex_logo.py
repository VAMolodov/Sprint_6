import allure
import pytest
from curl import *
from page_objects.main_page import MainPage

class TestScooterYandexLogo:
    @allure.title("Тест логотипа Самоката")
    def test_logo_scooter(self, driver):
        # Arrange
        main_page = MainPage(driver)
        # Act
        main_page.click_on_order()
        main_page.click_on_logo_scooter()
        # Assert
        assert driver.current_url == main_site 

    @allure.title("тест логотипа Яндекса")
    def test_logo_yandex(self, driver):
        # Arrange
        main_page = MainPage(driver)
        # Act
        main_page.click_on_logo_Yandex()
        main_page.switch_window()
        main_page.wait_until_not_about_blank()
        # Assert
        assert 'Дзен' in main_page.get_page_title_dzen()
    
