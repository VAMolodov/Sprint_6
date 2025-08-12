import allure
import pytest
from curl import *
from data import *
from page_objects.main_page import MainPage

class TestScooterYandexLogo:
    @allure.title("Тест логотипа Самоката")
    @allure.description('Проверяте что при клике на логотип Самоката попадешь на главную страницу')
    def test_logo_scooter(self, driver):
        # Arrange
        main_page = MainPage(driver)
        # Act
        main_page.click_cookie_accept()
        main_page.click_on_order()
        main_page.click_on_logo_scooter()
        url_head_page_scooter = main_page.get_url_head_page_scooter()
         # Assert
        assert  url_head_page_scooter == main_site 

    @allure.title("тест логотипа Яндекса")
    @allure.description('Проверяет что если кликнуть на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена')
    def test_logo_yandex(self, driver):
        # Arrange
        main_page = MainPage(driver)
        # Act
        main_page.click_cookie_accept()
        main_page.click_on_logo_Yandex()
        main_page.switch_window_dzen()
        main_page.wait_until_not_about_blank()
        title_dzen = main_page.get_page_title_dzen()
        # Assert
        assert  DataExpectedResponses.dzen in title_dzen
    
