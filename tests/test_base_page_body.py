#  3) Run tests:
#     python -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
from selenium import webdriver
from pages.exlab_locator import YourOpportunity, AboutUs
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.print_page_options import PrintOptions
import re

def for_scroll(page):
    page.WAIT_LOAD()
    page.BODY.scroll_my_down()
    page.WAIT_LOAD()
    page.BODY.scroll_my_up()
    page.WAIT_LOAD()

def test_img_logo(web_browser):
    """Отображение логотипа ExLab в блоке(отображение элемента с гиф)"""

    page = YourOpportunity(web_browser)
    page.WAIT_LOAD()
    assert page.IMG_LOGO.is_presented(), 'Нет элемента с логотипом'
    assert page.IMG_LOGO.is_visible(), 'Элемент слоготипом не видно'


def test_text_your_opportunity(web_browser):
    """Отображение надписи Твоя возможность"""

    page = YourOpportunity(web_browser)
    page.WAIT_LOAD()
    assert page.TEXT_YOUR_OPPORTUNITY.is_presented(), 'Нет элемента Твоя возможность'
    assert page.TEXT_YOUR_OPPORTUNITY.is_visible(), 'Элемент Твоя возможность невидно'


def test_text_under_your_opportunity(web_browser):
    """Отображение текста под надписью Твоя возможность"""
    # 01 ПОЛУЧИТЬ ТОТ САМЫЙ ОПЫТ
    # 02 ПОРАБОТАТЬ В КОМАНДЕ
    # 03 СОЗДАТЬ ПРОЕКТ С НУЛЯ
    # 04 ПОПОЛНИТЬ ПОРТФОЛИО
    # + РАЗВИТЬ SOFT SKILLS

    page = YourOpportunity(web_browser)
    page.WAIT_LOAD()
    text_list = page.TEXT_UNDER_YOUR_OPPORTUNITY.get_text()
    text_soft_skills = page.TEXT_UNDER_YOUR_OPPORTUNITY_SOFT_SKILLS
    for i in range(len(text_list)):
        assert page.TEXT_UNDER_YOUR_OPPORTUNITY[i].is_displayed()
    assert 'ПОЛУЧИТЬ ТОТ САМЫЙ ОПЫТ' in text_list[0]
    assert 'ПОРАБОТАТЬ В КОМАНДЕ' in text_list[1]
    assert 'СОЗДАТЬ ПРОЕКТ С НУЛЯ' in text_list[2]
    assert 'ПОПОЛНИТЬ ПОРТФОЛИО' in text_list[3]
    assert page.TEXT_UNDER_YOUR_OPPORTUNITY_SOFT_SKILLS.is_visible()
    assert 'РАЗВИТЬ SOFT SKILLS' in page.TEXT_UNDER_YOUR_OPPORTUNITY_SOFT_SKILLS.get_text()


def test_h1_about_us(web_browser):
    """Отображение надписи О нас"""

    page = AboutUs(web_browser)
    page.WAIT_LOAD()
    for_scroll(page=AboutUs(web_browser))
    #page.H1_ABOUT_US.highlight_and_make_screenshot()  #scroll_to_element()
    page.H1_ABOUT_US.scroll_to_element_js()
    time.sleep(1)
    assert page.H1_ABOUT_US.is_presented(), 'нет элемента заголовок О нас '
    assert page.H1_ABOUT_US.is_visible(), 'Элемент Заголовок О нас не видно'
    assert 'О нас' in page.H1_ABOUT_US.get_text(), 'Элемент заголовка не содержит текст:О нас'


def test_text_about_us(web_browser):
    """Отображение текста под надписью О нас"""

    page = AboutUs(web_browser)
    page.WAIT_LOAD()

    for_scroll(page=AboutUs(web_browser))
    page.H1_ABOUT_US.scroll_to_element_js()
    time.sleep(1)
    assert page.TEXT_ABOUT_US.is_presented(), 'Нет элемента текст под надписью О нас'
    assert page.TEXT_ABOUT_US.is_visible(), 'Элемент текст поднадписбю О нас не видно'
    assert page.TEXT_ABOUT_US.get_text != '', 'Нет текста внутри элемента текст под надписью О нас'


def test_h1_why_exlab(web_browser):
    """Отображение надписи Почему ExLab?"""

    page = AboutUs(web_browser)
    page.WAIT_LOAD()
    for_scroll(page=AboutUs(web_browser))
    page.H1_WHY_EXLAB.scroll_to_element_js()
    time.sleep(1)
    assert page.H1_WHY_EXLAB.is_presented(), 'Нет элемента Почему ExLab?'
    assert page.H1_WHY_EXLAB.is_visible(), 'Элемента Почему ExLab? не видно'
    assert 'Почему ExLab' in page.H1_WHY_EXLAB.get_text(), 'Элемент заголовка  не содержит текст:Почему ExLab?'


def test_text_why_exlab(web_browser):
    """Отображение текста под надписью Почему ExLab?"""

    page = AboutUs(web_browser)
    page.WAIT_LOAD()
    for_scroll(page=AboutUs(web_browser))
    page.H1_WHY_EXLAB.scroll_to_element_js()
    time.sleep(1)
    text_list_why_exlab = page.TEXT_WHY_EXLAB.count()
    for i in range(text_list_why_exlab):
        assert page.TEXT_WHY_EXLAB[i].is_displayed(), 'Элементв списке элемента не видно'
        assert page.TEXT_WHY_EXLAB[i].text != '', 'Нет текста внутри списка элементов с текстом'


def test_button_join_body(web_browser):
    """Кнопка [Присоединиться] в body"""

    page = AboutUs(web_browser)
    page.WAIT_LOAD()
    for_scroll(page=AboutUs(web_browser))
    page.BUTTON_JOIN.scroll_to_element_js()
    time.sleep(1)
    assert page.BUTTON_JOIN.is_visible(), 'Элемента кнопка Присоедениться не видно'
    assert page.BUTTON_JOIN.is_clickable(), 'Кнопка Присоедениться не кликабельна'
    page.BUTTON_JOIN.click()
    page.WAIT_LOAD()
    page.SWITCH_WINDOW()
    assert 'ExLab_registration_bot' in page.GET_URL(), 'Нет перехода на страницу с ссылкой на ТГ Бот проекта'









































