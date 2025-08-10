from selenium.webdriver.common.by import By


class OrderPageLocators :
 # Раздел Для кого самокат  
   # локатор поля Имя на странице заказа
    name_order_locator = (By.XPATH, ' //input[@placeholder="* Имя"]')

   # локатор поля Фамилия на странице заказа
    surname_order_locator = (By.XPATH, ' //input[@placeholder="* Фамилия"]')

   # локатор поля Адрес на странице заказа
    adress_order_locator = (By.XPATH, ' //input[@placeholder="* Адрес: куда привезти заказ"]')

   # локатор поля Станция метро на странице заказа
    metro_station_order_locator = (By.XPATH, ' //input[@placeholder="* Станция метро"]')

   # локатор поля Телефон на странице заказа
    telefon_order_locator = (By.XPATH, ' //input[@placeholder="* Телефон: на него позвонит курьер"]')

   # локатор кнопки Далее на странице заказа
    button_go_order_locator = (By.XPATH, '//div[@class = "Order_NextButton__1_rCA"]/button[text() = "Далее"]')

# Раздел Про аренду
   # локатор поля Когда привезти самокат 
    date_order_locator = (By.XPATH, ' //input[@placeholder="* Когда привезти самокат"]')

   # локатор поля  Срок аренды
    rental_period_order_locator = (By.XPATH, ' //div[@class = "Dropdown-placeholder"]')

   # блок чек-боксов цвет самоката
   # локатор чек бокса - цвет самоката черный
    color_black_scooter_order_locator = (By.XPATH, '//input[@id="black" and @class="Checkbox_Input__14A2w" and @type="checkbox" and @name=""]')
    # локатор чек бокса - цвет самоката серый
    grey_black_scooter_order_locator = (By.XPATH, '//input[@id="grey" and @class="Checkbox_Input__14A2w" and @type="checkbox" and @name=""]')

    # поле ввода Коментарий для курьера
    comment_order_locator = (By.XPATH, ' //input[@placeholder="Комментарий для курьера"]')

    # локатор кнопки  Заказать 
    button_order_locator =(By.XPATH, '//div[@class = "Order_Buttons__1xGrp"]/button[text() = "Заказать"]')

# Окно Хотите оформить заказ 
# Копка Да 
    button_yes_locator =(By.XPATH, '//div[@class = "Order_Buttons__1xGrp"]/button[text() = "Заказать"]')

# Окно Заказ оформлен 
# текст Заказ оформлен 
    text_order_locator =(By.XPATH, '//div[@class = "Order_ModalHeader__3FDaJ"]')
