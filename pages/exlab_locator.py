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


class YourOpportunity(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'http://test.exlab.team/'

        super().__init__(web_driver, url)

    # Логотип в разделе твоя возможность
    IMG_LOGO = WebElement(xpath='//img[@alt="gif_logo"]')
    # Текст Твоя возможность
    TEXT_YOUR_OPPORTUNITY = WebElement(xpath='//div[@class="sc-kgflAQ gupdxc"]')
    # текст под надписью Твоя возможность (список)
    TEXT_UNDER_YOUR_OPPORTUNITY = ManyWebElements(xpath='//li[@class="sc-cxabCf iOiPKd"]')
    TEXT_UNDER_YOUR_OPPORTUNITY_SOFT_SKILLS = WebElement(xpath='//li[@class="sc-ezWOiH dzMypq"]')
    # Ждать загрузку страницы
    WAIT_LOAD = WebPage.wait_page_loaded


class AboutUs(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'http://test.exlab.team/'

        super().__init__(web_driver, url)


    # Ждать загрузку страницы
    WAIT_LOAD = WebPage.wait_page_loaded
    # Получить url страницы
    GET_URL = WebPage.get_current_url
    GET_PAGE = WebPage.get_page_source
    # Переключить вкладку
    SWITCH_WINDOW = WebPage.switch_to_next_window

    # Заголовок блока О нас в body
    H1_ABOUT_US = WebElement(xpath='//div[@class="sc-eCYdqJ koNCEH is-inview"]')
    # Текст под заголовком в блоке О нас(в правой части экрана)
    TEXT_ABOUT_US = WebElement(xpath='//p[@class="sc-cCsOjp cdaqyF"]')
    # Заголовок Почему ExLab?
    H1_WHY_EXLAB = WebElement(xpath='//div[@class="sc-bZnhIo CLhmH is-inview"]')
    # Текст поднадписью Почему ExLab? (список)
    TEXT_WHY_EXLAB = ManyWebElements(xpath='//li[@class="sc-efBctP bQeQvl"]')
    # Кнопка присоедениться
    BUTTON_JOIN = WebElement(xpath='//a[@class="sc-dkzDqf gpYSxm is-inview"]')
    # URL t.me перехода в группу Exlab, приложения телеграмм
    URL_JOIN_TELEGRAMM = 'https://t.me/ExLab_registration_bot'

    MOVE_DOWN = WebPage.scroll_down
    BODY = WebElement(tag_name='html')


class Projects(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'http://test.exlab.team/'

        super().__init__(web_driver, url)

    # Ждать загрузку страницы
    WAIT_LOAD = WebPage.wait_page_loaded
    # Получить url страницы
    GET_URL = WebPage.get_current_url
    GET_PAGE = WebPage.get_page_source
    # Переключить вкладку
    SWITCH_WINDOW = WebPage.switch_to_next_window
    MOVE_DOWN = WebPage.scroll_down
    BODY = WebElement(tag_name='html')
    #  Скролл до веб_элемента
    SCROLL_TO_WEB_ELEMENT = WebPage.scroll_to

    # Заголовок блока Проекты в body
    #H1_PROJECTS = WebElement(xpath='//div[@class="sc-eCYdqJ koNCEH" and @data-scroll-target="#projects"]')
    H1_PROJECTS = WebElement(xpath='//div[@id="projects"]/div[@class="sc-eCYdqJ koNCEH is-inview"]')
    # Заголовки проектов
    H2_PROJECTS = ManyWebElements(xpath='//h2[@class="sc-dPyBCJ elZmsx is-inview"]')
    # Логотипы проектов
    IMG_PROJECTS = ManyWebElements(xpath='//img[@class="sc-bBXxYQ hEflMO"]')
    # Текст описание проектов
    TEXT_PROJECTS_DESCRIPT = ManyWebElements(xpath='//p[@class="sc-cOFTSb bNtNdQ is-inview"]')
    # Текст Руководители проектов
    TEXT_PRODUCT_OWNER = ManyWebElements(xpath='//span[@class="sc-hTtwUo nouGC"]')






























