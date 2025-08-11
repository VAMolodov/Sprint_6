import allure
import pytest

from data import *
from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage

class TestOrder:
    @allure.title("Проверка позитивного сценария с двумя наборами данных и точек входа в сценарий через кнопки «Заказать» ")
    @allure.description('Проверяет через разные точки входа весь флоу позитивного сценария с двумя наборами данных')
    @pytest.mark.parametrize("test_data, select_button", [(DataUser.test_data_user_1, MainPage.click_on_order) , (DataUser.test_data_user_2, MainPage.click_on_order_midll)])
    def test_text_answers(self, driver, test_data, select_button):
        # Arrange
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_cookie_accept()
        select_button(main_page)
        
        # Act
        order_page.filling_user_data(test_data)
        order_page.filling_order_data(test_data)
        order_page.place_an_order()
        # Assert
        assert 'Заказ оформлен' in order_page.get_text_successful_order_creation()
