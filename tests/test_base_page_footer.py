#  3) Run tests:
#     python -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
from selenium import webdriver
from pages.exlab_locator import  Footer
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.print_page_options import PrintOptions
import re
import pytest
from settings import BasePageSet
from data.info_mentors import data_mentors_list


def for_scroll(page):
    page.WAIT_LOAD()
    page.BODY.scroll_my_down()
    page.WAIT_LOAD()
    page.BODY.scroll_my_up()
    page.WAIT_LOAD()


def test_logo_footer(web_browser):
    """Отображение логотипа ExLab"""

    page = Footer(web_browser)
    page.WAIT_LOAD()
    for_scroll(page=Footer(web_browser))  # Функция скролла доподвала и обратно
    page.LOGO_EXLAB.scroll_to_element_js()
    time.sleep(2)
    assert page.LOGO_EXLAB.is_presented(), 'Нет элемента логотип ExLab в подвале'
    assert page.LOGO_EXLAB.is_visible(), 'Элемент логотип ExLab в подвале не видно'
    img_logo_css = page.LOGO_EXLAB.get_css('background')
    # pattern_logo_name = r"\w+"
    img_logo_footer_url = re.split('[()]', img_logo_css)[3].replace('"', '')
    assert 'http://test.exlab.team/images/logo/logo_black.png' == img_logo_footer_url
    # Добавить проверку файла логотипа
    # Перенести тестовые данные в файл settings.py


def test_logo_footer_text(web_browser):
    """Отображение под логотипом ExLab текста"""

    page = Footer(web_browser)
    page.WAIT_LOAD()
    for_scroll(page=Footer(web_browser))  # Функция скролла доподвала и обратно
    page.LOGO_EXLAB_TEXT.scroll_to_element_js()
    time.sleep(1)
    assert page.LOGO_EXLAB_TEXT.is_presented(), 'Нет элемента текст под логотипом ExLab в подвале'
    assert page.LOGO_EXLAB_TEXT.is_visible(), 'Элемент текст под логотипом ExLab в подвале не видно'
    assert '© 2022. ExLab' in page.LOGO_EXLAB_TEXT.get_text(), 'Текст под логотипом Exlab в подвале'
    # Перенести тестовые данные в файл settings.py


def test_footer_link_lnkdn(web_browser):
    """Отображение ссылки LNKDN"""

    page = Footer(web_browser)
    page.WAIT_LOAD()
    for_scroll(page=Footer(web_browser))  # Функция скролла доподвала и обратно
    page.LOGO_EXLAB_TEXT.scroll_to_element_js()
    time.sleep(1)
    assert page.LINK_LNKDN.is_presented(), 'Нет элемента ссылка LNKDN в подвале'
    assert page.LINK_LNKDN.is_visible(), 'Элемент текст под логотипом ExLab в подвале не видно'
    assert 'LNKDN' in page.LINK_LNKDN.get_text(), 'Не соответствует Текст в ссылке LNKDN в подвале'
    assert page.LINK_LNKDN.is_clickable(), 'Не кликабельна ссылка LNKDN'
    page.LINK_LNKDN.click()
    page.WAIT_LOAD()
    page.SWITCH_WINDOW()
    assert 'https://www.linkedin.com/company/exlab-start-up/mycompany/' in page.GET_URL(), 'Нет перехода на страницу с ссылкой на ТГ Бот проекта'
    # Перенести тестовые данные в файл settings.py


def test_footer_link_instgrm(web_browser):
    """Отображение ссылки INSTGRM"""

    page = Footer(web_browser)
    page.WAIT_LOAD()
    for_scroll(page=Footer(web_browser))  # Функция скролла доподвала и обратно
    page.LOGO_EXLAB_TEXT.scroll_to_element_js()
    time.sleep(1)
    assert page.LINK_INSTGRM.is_presented(), 'Нет элемента ссылка INSTGRM в подвале'
    assert page.LINK_INSTGRM.is_visible(), 'Элемент ссылка INSTGRM в подвале не видно'
    assert 'INSTGRM' in page.LINK_INSTGRM.get_text(), 'Не соответствует Текст в ссылке INSTGRM в подвале'
    assert page.LINK_INSTGRM.is_clickable(), 'Не кликабельна ссылка INSTGRM'
    page.LINK_INSTGRM.click()
    page.WAIT_LOAD()
    page.SWITCH_WINDOW()
    assert 'https://www.instagram.com/exlab_startup/' in page.GET_URL(), 'Нет перехода на страницу с ссылкой на ТГ Бот проекта'
    # Перенести тестовые данные в файл settings.py


def test_footer_link_tlgrm(web_browser):
    """Отображение ссылки TLGRM"""

    page = Footer(web_browser)
    page.WAIT_LOAD()
    for_scroll(page=Footer(web_browser))  # Функция скролла доподвала и обратно
    page.LINK_TLGRM.scroll_to_element_js()
    time.sleep(1)
    assert page.LINK_TLGRM.is_presented(), 'Нет элемента ссылка TLGRM в подвале'
    assert page.LINK_TLGRM.is_visible(), 'Элемент ссылка TLGRM в подвале не видно'
    assert 'TLGRM' in page.LINK_TLGRM.get_text(), 'Не соответствует Текст в ссылке TLGRM в подвале'
    assert page.LINK_TLGRM.is_clickable(), 'Не кликабельна ссылка TLGRM'
    page.LINK_TLGRM.click()
    page.WAIT_LOAD()
    page.SWITCH_WINDOW()
    assert 'https://t.me/ExLabChannel' in page.GET_URL(), 'Нет перехода на страницу с ссылкой на ТГ Бот проекта'
    # Перенести тестовые данные в файл settings.py


def test_footer_link_ytb(web_browser):
    """Отображение ссылки YTB"""

    page = Footer(web_browser)
    page.WAIT_LOAD()
    for_scroll(page=Footer(web_browser))  # Функция скролла доподвала и обратно
    page.LOGO_EXLAB_TEXT.scroll_to_element_js()
    time.sleep(1)
    assert page.LINK_YTB.is_presented(), 'Нет элемента ссылка YTB в подвале'
    assert page.LINK_YTB.is_visible(), 'Элемент ссылка YTB в подвале не видно'
    assert 'YTB' in page.LINK_YTB.get_text(), 'Не соответствует Текст ссылки YTB в подвале'
    assert page.LINK_YTB.is_clickable(), 'Не кликабельна ссылка YTB'
    page.LINK_YTB.click()
    page.WAIT_LOAD()
    page.SWITCH_WINDOW()
    assert 'https://www.youtube.com/channel/UC-TAnVYVN7qg5dgsYQJkuvA' in page.GET_URL(), 'Нет перехода на страницу с ссылкой на ТГ Бот проекта'
    # Перенести тестовые данные в файл settings.py


def test_footer_link_mail(web_browser):
    """Отображение ссылки mail:info@exlab.team"""

    page = Footer(web_browser)
    page.WAIT_LOAD()
    for_scroll(page=Footer(web_browser))  # Функция скролла доподвала и обратно
    page.LINK_MAIL_EXLAB.scroll_to_element_js()
    time.sleep(1)
    assert page.LINK_MAIL_EXLAB.is_presented(), 'Нет элемента ссылка info@exlab.team в подвале'
    assert page.LINK_MAIL_EXLAB.is_visible(), 'Элемент ссылка info@exlab.team в подвале не видно'
    assert 'info@exlab.team' in page.LINK_MAIL_EXLAB.get_text(), 'Не соответствует Текст ссылки info@exlab.team в подвале'
    assert page.LINK_MAIL_EXLAB.is_clickable(), 'Не кликабельна ссылка info@exlab.team'
    with open("namefile1.txt", 'a', encoding="utf=8") as myFile:
        print(f'{page.LINK_MAIL_EXLAB.get_attribute("href")}', file=myFile)
    assert 'mailto:info@exlab.team' in page.LINK_MAIL_EXLAB.get_attribute('href')
    # Перенести тестовые данные в файл settings.py








