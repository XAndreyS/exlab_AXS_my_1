# pytest --driver Firefox --driver-path /path/to/geckodriver.exe
import os
from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class BaseUrl(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'http://test.exlab.team/'

        super().__init__(web_driver, url)

    BASE_URL = 'http://test.exlab.team/'
    WAIT_LOAD = WebPage.wait_page_loaded
    GET_URL = WebPage.get_current_url

class BlockHeader(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'http://test.exlab.team/'

        super().__init__(web_driver, url)

    # Темная тема страницы
    DARK_BODY = WebElement(xpath='//div[@class="sc-bczRLJ ckyTig"]')
    # Светлая тема страницы
    WHITE_BODY = WebElement(xpath='//div[@class="sc-bczRLJ cxdoLY"]')
    # Кнопка переключения стилей интерфейса sun_icon в Темной теме
    BUTTON_DARK_ICON = WebElement(xpath='//div[@class="sc-fnykZs fEkGUM"]')
    # Кнопка переключения стилей интерфейса sun_icon в Светлой теме
    BUTTON_WHITE_ICON = WebElement(xpath='//div[@class="sc-fnykZs lfkjFc"]')
    # О нас
    LINK_ABOUT = WebElement(xpath='//a[@data-scroll-to="#about"]')
    # Проекты
    LINK_PROJECTS = WebElement(xpath='//a[@data-scroll-to="#projects"]')
    # Менторы
    LINK_MENTORS = WebElement(xpath='//a[@data-scroll-to="#mentors"]')
    # StartUp для
    LINK_STARTUP = WebElement(xpath='//a[@data-scroll-to="#startup"]')
    # О нас экран с заголовком H1
    H1_ABOUT = WebElement(xpath='//div[@class="sc-eCYdqJ koNCEH is-inview"]')
    # Проекты экран с заголовком H1
    H1_PROJECTS = WebElement(xpath='//div[@class="sc-eCYdqJ koNCEH" and @data-scroll-target="#projects"]')
    # Менторы экран с заголовком H1
    H1_MENTORS = WebElement(xpath='//div[contains(text(), "Менторы")]')
    # StartUp для экран с заголовком H1
    H1_STARTUP = WebElement(xpath='//div[@class="sc-eCYdqJ koNCEH" and @data-scroll-target="#startup"]')
    # Логотп в шапке
    LOGO_HEAD = WebElement(xpath='//div[@id="logo_mobile"]')
    # Картинки в теле раздела Проекты
    IMG_BODY_PROJECTS = WebElement(xpath='//img[@class="sc-bBXxYQ hEflMO"]')
    # Кнопка Присоедениться
    BUTTON_JOIN = WebElement(xpath='//div[@class="sc-hAZoDl hrEelO"]')
    # Кнопка Присоедениться ниже подереве тег a со ссылкой
    BUTTON_JOIN_HREF = WebElement(xpath='//a[@class="sc-dkzDqf gpYSxm"]')

    # Ждать загрузку страницы
    WAIT_LOAD = WebPage.wait_page_loaded

    MOVE_DOWN = WebPage.scroll_my_base
    BODY = WebElement(tag_name='html')
    # Получить url страницы
    GET_URL =  WebPage.get_current_url
    GET_PAGE = WebPage.get_page_source
    # Переключить вкладку
    SWITCH_WINDOW = WebPage.switch_to_next_window