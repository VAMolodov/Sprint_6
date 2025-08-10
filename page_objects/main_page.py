import allure
from page_objects.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):

    @allure.step("Кликнуть по кнопке Заказать")
    def click_on_order(self):
        self.click_on_element(MainPageLocators.button_order_header)  

    @allure.step("Кликнуть по логотипу Самоката")
    def click_on_logo_scooter(self):
        self.click_on_element(MainPageLocators.Scooter_logo_header)

    @allure.step("Кликнуть по логотипу Яндекса")
    def click_on_logo_Yandex(self):
        self.click_on_element(MainPageLocators.Yandex_logo_header)
    
    @allure.step("Скролл до секции Вопросы о важном")
    def scroll_to_section_faq(self):
        self.scroll_to_element(MainPageLocators.important_questions_section)

    @allure.step("Кликнуть по вопросу секции faq")
    def click_on_question_section_faq(self, faq_questions_number):
        question_number_locator = MainPageLocators.faq_questions_number(faq_questions_number)
        self.scroll_to_element(question_number_locator)
        self.click_on_element(question_number_locator)
   

    @allure.step("Сравни текст ответа faq")
    def check_text_answer_to_section_faq(self,faq_answer_number, expected_text):
        answer_number_locator = MainPageLocators.faq_answer_number(faq_answer_number)
        actual_text = self.get_text_on_element(answer_number_locator)
        return actual_text == expected_text
    
    @allure.step('Переключиться на вкладку Дзена')
    def switch_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])


    @allure.step("Получение титла Дзен")
    def get_page_title_dzen(self):
        actual_title = self.get_page_title(MainPageLocators.title_of_page)
        return actual_title

    
