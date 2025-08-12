import allure
from page_objects.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step("Заполнение формы Для кого самокат и клик по кнопке Далее")
    def filling_user_data(self, test_data):
        self.wait_for_element(OrderPageLocators.user_form_order_locator)

        self.click_on_element(OrderPageLocators.name_order_locator)
        self.send_keys_to_input(OrderPageLocators.name_order_locator, test_data[0])

        self.click_on_element(OrderPageLocators.surname_order_locator)
        self.send_keys_to_input(OrderPageLocators.surname_order_locator, test_data[1])

        self.click_on_element(OrderPageLocators.adress_order_locator)
        self.send_keys_to_input(OrderPageLocators.adress_order_locator, test_data[2])

        self.click_on_element(OrderPageLocators.metro_station_order_locator)
        self.send_keys_to_input(OrderPageLocators.metro_station_order_locator, test_data[3])
        self.click_on_element(OrderPageLocators.select_dropdown_metro)

        self.click_on_element(OrderPageLocators.telefon_order_locator)
        self.send_keys_to_input(OrderPageLocators.telefon_order_locator, test_data[4])

        self.click_on_element(OrderPageLocators.button_go_order_locator)
        
    @allure.step("Заполнение формы Для кого самокат и клик по кнопке Далее")
    def filling_order_data(self, test_data):
        self.wait_for_element(OrderPageLocators.button_order_locator)

        self.click_on_element(OrderPageLocators.date_order_locator)
        self.send_keys_to_input(OrderPageLocators.date_order_locator, test_data[5])
        self.click_on_element(OrderPageLocators.calendar_order_locator)

        self.click_on_element(OrderPageLocators.rental_period_order_locator)
        self.click_on_element(OrderPageLocators.dropdown_rental_period)

        self.click_on_element(OrderPageLocators.color_black_scooter_order_locator)
        self.click_on_element(OrderPageLocators.color_black_scooter_order_locator)
        self.click_on_element(OrderPageLocators.grey_black_scooter_order_locator)

        self.click_on_element(OrderPageLocators.comment_order_locator)
        self.send_keys_to_input(OrderPageLocators.comment_order_locator, test_data[6])

        self.click_on_element(OrderPageLocators.button_order_locator)


    @allure.step("Оформление заказа")
    def place_an_order (self):
        self.wait_for_element(OrderPageLocators.button_yes_locator)

        self.click_on_element(OrderPageLocators.button_yes_locator)

    @allure.step("Получить текст об успешном создании заказа")
    def get_text_successful_order_creation (self):
        actual_text = self.get_text_on_element(OrderPageLocators.text_order_locator) 
        return actual_text