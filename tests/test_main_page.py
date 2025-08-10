import allure
import pytest

import data
from page_objects.main_page import MainPage

class TestFAQ:
    @allure.title("Тест выпадающего списка ответов в разделе «Вопросы о важном»")
    @pytest.mark.parametrize('faq_questions_number,faq_answer_number, expected_text', data.Answers.the_answers_text)
    def test_text_answers(self, driver, faq_questions_number,faq_answer_number, expected_text):
        # Arrange
        main_page = MainPage(driver)
        main_page.scroll_to_section_faq()
        # Act
        main_page.click_on_question_section_faq(faq_questions_number)
        # Assert
        assert main_page.check_text_answer_to_section_faq(faq_answer_number,expected_text)
