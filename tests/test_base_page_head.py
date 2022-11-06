#  3) Run tests:
#     python -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
from selenium import webdriver
from pages.exlab_locator import BaseUrl, BlockHeader
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.print_page_options import PrintOptions
import re


def test_url_exlab(web_browser):
    """Лединг доступен по адресу http://test.exlab.team/"""
    page = BaseUrl(web_browser)
    page.WAIT_LOAD()
    assert page.GET_URL() == 'http://test.exlab.team/'


def test_base_dark_vision(web_browser):
    """По умолчанию открыввется тёмная тема лединга"""
    page = BlockHeader(web_browser)
    page.WAIT_LOAD()
    assert page.DARK_BODY.is_visible() is True,'Отсутствует элемент с классом css для Тёмной темы'
    BACKGROUND = page.DARK_BODY.get_css('background')
    assert '17, 17, 17' in re.split('[()]', BACKGROUND), 'Цвет rgb(17, 17, 17) отсутствует '


def test_logo_head(web_browser):
    """Отображение логотипа ExLab"""
    page = BlockHeader(web_browser)
    page.WAIT_LOAD()
    assert page.LOGO_HEAD.is_visible() is True, 'Логотип не найден'
    img_logo_css = page.LOGO_HEAD.get_css('background')
    # pattern_logo_name = r"\w+"
    img_logo_head_url = re.split('[()]', img_logo_css)[3].replace('"','')
    assert 'http://test.exlab.team/images/logo/logo_black.png' == img_logo_head_url


def test_link_click_about(web_browser):
    """Клик по ссылке меню О нас"""
    page = BlockHeader(web_browser)
    page.WAIT_LOAD()
    time.sleep(2)
    assert page.LINK_ABOUT.is_visible() is True, 'Ссылку меню не видно'
    page.LINK_ABOUT.click()
    time.sleep(2)
    page.WAIT_LOAD()
    assert page.H1_ABOUT.is_visible() is True, 'Заголовок H1 О нас не виден'
    assert page.H1_ABOUT.get_text() == 'О нас', 'проблема с текстом в заголовке'
    time.sleep(2)


def test_link_click_projects(web_browser):
    """Клик по ссылке меню Проекты"""
    page = BlockHeader(web_browser)
    page.WAIT_LOAD()
    assert page.LINK_PROJECTS.is_visible() is True, 'Ссылку меню не видно'
    page.LINK_PROJECTS.click()
    page.WAIT_LOAD()
    assert page.H1_PROJECTS.is_visible() is True, 'Заголовок H1 О нас не виден'
    assert page.H1_PROJECTS.get_text() == 'Проекты', 'проблема с текстом в заголовке'


def test_link_click_mentors(web_browser):
    """Клик по ссылке меню Менторы"""
    page = BlockHeader(web_browser)
    page.WAIT_LOAD()
    assert page.LINK_MENTORS.is_visible() is True, 'Ссылку меню не видно'
    page.LINK_MENTORS.click()
    page.WAIT_LOAD()
    assert page.H1_MENTORS.is_visible() is True, 'Заголовок H1 Менторы не виден'
    assert page.H1_MENTORS.get_text() == 'Менторы', 'проблема с текстом в заголовке'


def test_link_click_startup(web_browser):
    """Клик по ссылке меню StartUp для"""
    page = BlockHeader(web_browser)
    page.WAIT_LOAD()
    assert page.LINK_STARTUP.is_visible() is True, 'Ссылку меню не видно'
    page.LINK_STARTUP.click()
    page.WAIT_LOAD()
    assert page.H1_STARTUP.is_visible() is True, 'Заголовок H1 StartUp для не виден'
    assert page.H1_STARTUP.get_text() == 'StartUp для', 'проблема с текстом в заголовке'


def test_button_sun_icon(web_browser):
    """Проверка отображения кнопки переключения темы пользовательского интерфейса Sun Icon"""
    page = BlockHeader(web_browser)
    page.WAIT_LOAD()
    assert page.DARK_BODY.is_visible() is True, 'Отсутствует элемент с классом css для Тёмной темы'
    BACKGROUND_DARK = page.DARK_BODY.get_css('background')
    assert '17, 17, 17' in re.split('[()]', BACKGROUND_DARK), 'Цвет Темной темы rgb(17, 17, 17) отсутствует '
    assert page.BUTTON_DARK_ICON.is_visible() is True, 'Отсутствует элемент Sun Icon в Темной теме'
    page.BUTTON_DARK_ICON.click()
    page.WAIT_LOAD()
    assert page.WHITE_BODY.is_visible() is True, 'Отсутствует элемент с классом css для Светлой темы'
    BACKGROUND_WHITE = page.WHITE_BODY.get_css('background')
    assert '255, 255, 255' in re.split('[()]', BACKGROUND_WHITE), 'Цвет Светлой темы rgb(255, 255, 255) отсутствует '

def test_button_join(web_browser):
    page = BlockHeader(web_browser)
    page.WAIT_LOAD()
    assert page.BUTTON_JOIN.is_visible() is True, 'Кнопка Присоедениться не отображается'
    assert page.BUTTON_JOIN.is_clickable() is True, 'Кнопка Присоедениться не кликабельна'
    page.BUTTON_JOIN.click()
    page.WAIT_LOAD()
    page.SWITCH_WINDOW()
    assert 'ExLab_registration_bot' in page.GET_URL(), 'Нет перехода на страницу с ссылкой на ТГ Бот проекта'

















































































