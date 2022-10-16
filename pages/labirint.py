# pytest --driver Firefox --driver-path /path/to/geckodriver.exe
import os
from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'

        super().__init__(web_driver, url)

    # Ссылка книги
    nav_book = WebElement(xpath='//li[@data-toggle="header-genres"]')
    # Ссылка главное 2022
    nav_general = WebElement(xpath='//li[@data-toggle="header-best"]')
    # Ссылка школа
    nav_shool = WebElement(xpath='//li[@data-toggle="header-school"]')
    # Ссылка игры
    nav_game = WebElement(xpath='//li[@data-toggle="header-toys"]')
    # Ссылка канцтовары
    nav_office = WebElement(xpath='//li[@data-toggle="header-office"]')
    # Ссылка клуб
    nav_club = WebElement(xpath='//li[@data-toggle="header-club"]')
    # Книги
    nav_book_end_url = 'https://www.labirint.ru/books/'
    nav_book_end = WebElement(xpath='//h1[@class="genre-name"]')
    # Глав
    nav_genegal_end_url = 'https://www.labirint.ru/best/'
    nav_general_end = WebElement(xpath='//h1[contains(text(), "Главные книги 2022")]')
    # учебники
    nav_shool_end_url = 'https://www.labirint.ru/school/'
    nav_shool_end = WebElement(xpath='//h1[@class="school-cap__header"]')
    # игры
    nav_game_end_url = 'https://www.labirint.ru/games/'
    nav_game_end = WebElement(xpath='//h1[@class="genre-name"]')
    # канцтовары
    nav_office_end_url = 'https://www.labirint.ru/office/'
    nav_office_end = WebElement(xpath='//h1[@class="genre-name"]')
    # клуб
    nav_club_end_url = 'https://www.labirint.ru/club/'
    nav_club_end = WebElement(xpath='//h1[contains(text(), "Клуб")]')

    get_url = WebPage.get_current_url
    wait_load = WebPage.wait_page_loaded


class GeneralSearch(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'

        super().__init__(web_driver, url)

    # Общий поиск
    general_search = WebElement(xpath='//input[@id="search-field"]')
    # кнопка "Искать"
    button_search = WebElement(xpath='//button[@type="submit"]')
    # страница с результатом - заголовок
    search_result_h1 = WebElement(xpath='//h1[@class="index-top-title"]')

    pag_num = WebElement(xpath='//a[@class="pagination-number__text"]')

    pag_list = ManyWebElements(xpath='//a[@class="pagination-number__text"]')

    pag_next = WebElement(xpath='//a[@title="Следующая"]')

    pag_next_2 = WebElement(xpath='//div[@class="pagination-next"]')

    card = WebElement(xpath='//div[@class="product need-watch watched"]')
    # Полуить текущий url страницы
    get_url = WebPage.get_current_url
    # Ждать загрузки страницы
    wait_load = WebPage.wait_page_loaded


class PersonalAreaIcon(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'

        super().__init__(web_driver, url)

    # Полуить текущий url страницы
    get_url = WebPage.get_current_url
    # Ждать загрузки страницы
    wait_load = WebPage.wait_page_loaded
    # Иконка личного кабинета
    per_area_icon = WebElement(xpath='//span[@class="js-b-autofade-text"]')
    # Всплывающее окно иконки личного кабинета
    page_per_area_icon = WebElement(xpath='//div[@style="width: 390px; text-align-last: left; left: auto;"]')
    # Дарим 50р
    donate_50 = WebElement(xpath='//span[contains(text(), "50р.")]')
    # баллы за отзывы
    points_reviews = WebElement(xpath='//span[contains(text(), "Баллы")]')
    # постоянная скидка
    permanent_discount = WebElement(xpath='//span[@class="no-wrap"]')
    # вход или регистрация
    login_register = WebElement(xpath='//a[@class="b-menu-list-title b-header-e-border-top"]')
    # Окно формы входа и регистрации
    window_login_register = WebElement(xpath='//div[@class="lab-modal-content"]')
    # Заголовок окна формы входа и регистрации:Полный доступ к Лабиринту
    window_log_reg_h1 = WebElement(xpath='//div[contains(text(), "Полный доступ к Лабиринту")]')


class AuthPersonalArea(WebPage):
    """Здесь локаторы для формы авторизации и прохождения её прохождения"""
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'

        super().__init__(web_driver, url)

    scr_page = WebPage.screenshot
    # Полуить текущий url страницы
    get_url = WebPage.get_current_url
    # Ждать загрузки страницы
    wait_load = WebPage.wait_page_loaded
    # Иконка личного кабинета
    per_area_icon = WebElement(xpath='//span[@class="js-b-autofade-text"]')
    # Окно формы входа и регистрации
    window_login_register = WebElement(xpath='//div[@class="lab-modal-content"]')
    # Заголовок окна формы входа и регистрации:Полный доступ к Лабиринту
    window_log_reg_h1 = WebElement(xpath='//div[contains(text(), "Полный доступ к Лабиринту")]')
    # Заголовок/условия поля ввода данных для аутетификации
    field_input_h1 = WebElement(xpath='//span[contains(text(), "Введите")]')
    # Поле ввода данных для аутетификации
    field_input = WebElement(xpath='//input[@placeholder="Введите свой код скидки, телефон или эл.почту"]')
    # Заголовок над кнопкой "войти":Найдем вас в Лабиринте или зарегистрируем
    button_auth_h1 = WebElement(xpath='//span[@class="full-input__msg js-msg" and @data-default-text='
                                      '"Найдем вас в Лабиринте или зарегистрируем"]')
    # Кнопка "Войти"
    button_auth = WebElement(css_selector='input#g-recap-0-btn')
    # Ссылка/кнопка:Другие способы входа
    other_login_methods = WebElement(xpath='//a[contains(text(), "Другие способы входа")]')
    # Иконка вк (Иконка ведет на страницу где присутствует адрес обоих сайтов)
    login_vk = WebElement(xpath='//a[@title="ВКонтакте"]')
    # Иконка однокласники (Иконка ведет на страницу где присутствует адрес обоих сайтов)
    login_ok = WebElement(xpath='//a[@title="Одноклассники"]')
    # Иконка майл.ру (Иконка ведет на страницу где присутствует адрес обоих сайтов)
    login_mail_ru = WebElement(xpath='//a[@title="Mail.ru"]')
    # Иконка яндекс (Иконка ведет на страницу где присутствует адрес обоих сайтов)
    login_yandex = WebElement(xpath='//a[@title="Яндекс"]')
    # Иконка гугл (Иконка ведет на страницу где присутствует адрес обоих сайтов)
    login_google = WebElement(xpath='//a[@title="Google"]')
    # Чек-бокс подтверждение принятия соглашения (иконки соцсетей не активны)
    check_box = WebElement(css_selector='input[type="checkbox"]')
    # Не активная кнопка авторизации:Необходимо принять соглашение
    no_active_button_auth = WebElement(css_selector='input[value="Необходимо принять соглашение"]')
    # Ссылка на пользовательское соглашение
    user_agreement = WebElement(xpath='//a[contains(text(), "пользовательского соглашения")]')
    # Ссылка на основные правила
    rules_agreement = WebElement(xpath='//a[contains(text(), "основные правила")]')
    # окно для ввода “введите свой код"
    window_enter_code = WebElement(xpath='//form[@id="auth-email-sent"]')
    # поле ввода “введите свой код"
    field_input_code = WebElement(xpath='//input[@autocomplete="email mail"]')
    # Кнопка подтверждения ввода  кода
    button_auth_code = WebElement(xpath='//form[@id="auth-email-sent"]/input[@value="Проверить код и войти"]')
    # Всплывающее окно с подтверждением входа(15 сек активно)
    window_well_come = WebElement(xpath='//div[@class="lab-modal-content"]')
    # Страница личного кабинета url
    page_auth_url = 'https://www.labirint.ru/cabinet/'
    # Заголовок на странице личного кабинета
    page_auth_h1 = WebElement(xpath='//span[contains(text(), "Личный кабинет — ")]')
    # Личныйй кабинет кнопка перехода в раздел "мои данные и настройки"
    page_auth_my_data = WebElement(xpath='//span[contains(text(), "Мои данные")]')
    # Личный кабинет, раздел "мои данные и настройки" , данные email
    page_auth_my_data_email = WebElement(xpath='//input[@placeholder="Email"]')
    # Временно поле где содержится емайл пользователя
    window_my_data_email = WebElement(xpath='//div[@class="edit-email-container  form-input"]')
    general_search = WebElement(css_selector='input#search-field')


class CardProduct(WebPage):
    """Здель содержатся локаторы для тестов карт товара"""
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'

        super().__init__(web_driver, url)

    # Полуить текущий url страницы
    get_url = WebPage.get_current_url
    # Ждать загрузки страницы
    wait_load = WebPage.wait_page_loaded
    # Ссылка книги
    nav_book = WebElement(xpath='//li[@data-toggle="header-genres"]')
    # Раздел Книги
    nav_book_end_url = 'https://www.labirint.ru/books/'
    nav_book_end = WebElement(xpath='//h1[@class="genre-name"]')
    # Заголовок списка товара
    product_list_h1 = WebElement(xpath='//div[@class="catalog-title"]')
    # Кол-во найденных товаров
    product_amount = WebElement(xpath='//span[@class="navisort-part navisort-head navisort-part-9"]')
    # Карточки товара (первые 5 не совсем в списке)
    product_card = ManyWebElements(xpath='//div[@class="card-column'
                                         ' card-column_gutter col-xs-6 col-sm-3 col-md-1-5 col-xl-2"]')
    # Все карточки на странице (пока WebElement, для поиска всех использовать ManyWebElements)
    all_product_card_page = WebElement(xpath='//div[@class="product need-watch watched"]')
    # Кнопки пагинации
    pag_num = WebElement(xpath='//a[@class="pagination-number__text"]')
    # Список книпок пагинации
    pag_list = ManyWebElements(xpath='//a[@class="pagination-number__text"]')
    # Кнопка "Следующая" для перехода на след страницу ссылка №1
    pag_next = WebElement(xpath='//a[@title="Следующая"]')
    # Кнопка "Следующая" для перехода на след страницу ссылка №2
    pag_next_2 = WebElement(xpath='//div[@class="pagination-next"]')


