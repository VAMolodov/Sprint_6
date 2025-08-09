from selenium.webdriver.common.by import By

class MainPageLocators :
    # кнопка Заказать в заголовкке
    button_order_header = (By.XPATH, '//div[@class = "Header_Nav__AGCXC"]/button[text() = "Заказать"]')

    # логотип Яндекс в заголовке
    Yandex_logo_header = (By.XPATH, '//a[contains(@class, "Header_LogoYandex__")]')

    # логотип Самоката в заголовке
    Scooter_logo_header = (By.XPATH, '//a[contains(@class, "Header_LogoScooter__")]')

    # кнопка Заказать под разделом Как это работает
    button_order_middl = (By.XPATH, '//div[@class = "Home_FinishButton__1_cWm"]/button[text() = "Заказать"]')

# раздел Вопросы о важном

    # заголовок секции Вопросы о важном
    important_questions_section = (By.XPATH, '//div[@class = "Home_SubHeader__zwi_E"] [text() = "Вопросы о важном"]')

    # локатор текста ответов
    #text_answer_faq = (By.XPATH, '//*[@id="accordion__panel-3"]')
    
    # метод формирует локатор для вопросов faq
    @staticmethod
    def faq_questions_number(question_number):
        return [By.XPATH, f".//div[@class='accordion__button' and @id='accordion__heading-{question_number}']"]
    
    # метод формирует локатор для ответов faq
    @staticmethod
    def faq_answer_number(answer_number):
        return (By.CSS_SELECTOR, f"div[id='accordion__panel-{answer_number}'] p")
       # return [By.XPATH, f".//div[@class='accordion__panel' and @id='accordion__panel-{question_number}']/p"]
    