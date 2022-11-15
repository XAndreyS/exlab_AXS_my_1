#  3) Run tests:
#     python -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
from selenium import webdriver
from pages.exlab_locator import YourOpportunity, AboutUs, Projects,  Mentors, StartUpFor
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
    for_scroll(page=AboutUs(web_browser))  # Функция скролла доподвала и обратно
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

    for_scroll(page=AboutUs(web_browser))  # Функция скролла доподвала и обратно
    page.H1_ABOUT_US.scroll_to_element_js()
    time.sleep(1)
    assert page.TEXT_ABOUT_US.is_presented(), 'Нет элемента текст под надписью О нас'
    assert page.TEXT_ABOUT_US.is_visible(), 'Элемент текст поднадписбю О нас не видно'
    assert page.TEXT_ABOUT_US.get_text != '', 'Нет текста внутри элемента текст под надписью О нас'


def test_h1_why_exlab(web_browser):
    """Отображение надписи Почему ExLab?"""

    page = AboutUs(web_browser)
    page.WAIT_LOAD()
    for_scroll(page=AboutUs(web_browser))  # Функция скролла доподвала и обратно
    page.H1_WHY_EXLAB.scroll_to_element_js()
    time.sleep(1)
    assert page.H1_WHY_EXLAB.is_presented(), 'Нет элемента Почему ExLab?'
    assert page.H1_WHY_EXLAB.is_visible(), 'Элемента Почему ExLab? не видно'
    assert 'Почему ExLab' in page.H1_WHY_EXLAB.get_text(), 'Элемент заголовка  не содержит текст:Почему ExLab?'


def test_text_why_exlab(web_browser):
    """Отображение текста под надписью Почему ExLab?"""

    page = AboutUs(web_browser)
    page.WAIT_LOAD()
    for_scroll(page=AboutUs(web_browser))  # Функция скролла доподвала и обратно
    page.H1_WHY_EXLAB.scroll_to_element_js()
    time.sleep(1)
    text_list_why_exlab = page.TEXT_WHY_EXLAB.count()
    for i in range(text_list_why_exlab):
        assert page.TEXT_WHY_EXLAB[i].is_displayed(), 'Элемент в списке элемента не видно'
        assert page.TEXT_WHY_EXLAB[i].text != '', 'Нет текста внутри списка элементов с текстом'


def test_button_join_body(web_browser):
    """Кнопка [Присоединиться] в body"""

    page = AboutUs(web_browser)
    page.WAIT_LOAD()
    for_scroll(page=AboutUs(web_browser))  # Функция скролла доподвала и обратно
    page.BUTTON_JOIN.scroll_to_element_js()
    time.sleep(1)
    assert page.BUTTON_JOIN.is_visible(), 'Элемента кнопка Присоедениться не видно'
    assert page.BUTTON_JOIN.is_clickable(), 'Кнопка Присоедениться не кликабельна'
    page.BUTTON_JOIN.click()
    page.WAIT_LOAD()
    page.SWITCH_WINDOW()
    assert 'ExLab_registration_bot' in page.GET_URL(), 'Нет перехода на страницу с ссылкой на ТГ Бот проекта'


def test_h1_projects(web_browser):
    """Отображение надписи Проекты"""

    page = Projects(web_browser)
    page.WAIT_LOAD()
    for_scroll(page=Projects(web_browser))  # Функция скролла доподвала и обратно
    page.H1_PROJECTS.scroll_to_element_js()
    time.sleep(1)
    assert page.H1_PROJECTS.is_visible(), 'Элемент с надписью Проекты не виден'
    assert 'Проекты' in page.H1_PROJECTS.get_text(), 'Текст внутри элемента Проекты не совпадает с ожидаемым'

@pytest.mark.parametrize("h2_element", [
    'Exlab',
    'Healthy life',
    'Easyhelp',
],
                         ids=[
                             'Первый элемеент Exlab',
                             'Второй элемент Healthy life',
                             'Третий элемент Easyhelp',
                         ])
def test_h2_projects(web_browser, h2_element):
    """Отображение заголовков проектов"""
    dict_projects = {'Exlab': 0, 'Healthy life': 1,  'Easyhelp': 2}
    page = Projects(web_browser)
    page.WAIT_LOAD()
    for_scroll(page=Projects(web_browser))  # Функция скролла доподвала и обратно
    #page.H1_PROJECTS.scroll_to_element_js()
    list_h2_projects = page.H2_PROJECTS
    page.SCROLL_TO_WEB_ELEMENT(list_h2_projects[dict_projects.get(h2_element)])
    time.sleep(1)
    assert list_h2_projects[dict_projects.get(h2_element)].is_displayed(),\
        f'Не видно элементa с названием проекта {h2_element}'
    assert list(dict_projects.keys())[0] or list(dict_projects.keys())[1] or \
           list(dict_projects.keys())[2] in list_h2_projects[dict_projects.get(h2_element)].text,\
        f'Не соввпадает название проекта {h2_element}'


@pytest.mark.parametrize("logo_element", [
    'Exlab',
    'Healthy life',
    'Easyhelp',
],
                         ids=[
                             'Первый элемеент Exlab',
                             'Второй элемент Healthy life',
                             'Третий элемент Easyhelp',
                         ])
def test_logo_projects(web_browser, logo_element):  # Добавить ссылки картинок в проверку?
    """Отображение логотипов ExLab, HealthyLife, Easyhelp в блоке"""
    dict_projects = {'Exlab': 0, 'Healthy life': 1, 'Easyhelp': 2}
    page = Projects(web_browser)
    page.WAIT_LOAD()
    for_scroll(page=Projects(web_browser))  # Функция скролла доподвала и обратно
    page.H1_PROJECTS.scroll_to_element_js()
    time.sleep(1)
    list_logo_projects = page.IMG_PROJECTS
    page.SCROLL_TO_WEB_ELEMENT(list_logo_projects[dict_projects.get(logo_element)])
    time.sleep(1)
    list_atributte_logo = page.IMG_PROJECTS.get_attribute('src')
    name_projects = ['Exlab', 'Healthy life', 'Easyhelp']
    img_link =['http://test.exlab.team/images/projects/logoExlab.png',
               'http://test.exlab.team/images/projects/logoHealth.svg',
               'http://test.exlab.team/images/projects/logoEasyhelp.svg']
    assert list_logo_projects[dict_projects.get(logo_element)].is_displayed(), \
        f'Не видно элементa с логотипом проекта {logo_element}'
    assert list_atributte_logo[dict_projects.get(logo_element)] != '', \
        f'Отсутствует или не правильная ссылка на лого проекта {logo_element}'


@pytest.mark.parametrize("text_owner_element", [
    'Exlab',
    'Healthy life',
    'Easyhelp',
],
                         ids=[
                             'Первый элемеент Exlab',
                             'Второй элемент Healthy life',
                             'Третий элемент Easyhelp',
                         ])
def test_text_projects(web_browser, text_owner_element):
    """Отображение текста в описании проекта ExLab, HealthyLife, Easyhelp"""
    dict_projects = {'Exlab': 0, 'Healthy life': 1, 'Easyhelp': 2}
    page = Projects(web_browser)
    page.WAIT_LOAD()
    for_scroll(page=Projects(web_browser))  # Функция скролла доподвала и обратно
    page.H1_PROJECTS.scroll_to_element_js()
    time.sleep(1)
    list_text_projects = page.TEXT_PROJECTS_DESCRIPT  # текст в описании проекта
    list_text_product_owner = page.TEXT_PRODUCT_OWNER  # Текст-Руководители проектов
    page.SCROLL_TO_WEB_ELEMENT(list_text_projects[dict_projects.get(text_owner_element)])
    time.sleep(1)
    name_projects = ['Exlab', 'Healthy life', 'Easyhelp']

    assert list_text_projects[dict_projects.get(text_owner_element)].is_displayed(), \
        f'Не видно элементa с логотипом проекта {text_owner_element}'

    assert list_text_projects[dict_projects.get(text_owner_element)].text != '', \
        f'Отсутствует или не правильная ссылка на лого проекта {text_owner_element}'
    assert list_text_product_owner[dict_projects.get(text_owner_element)].text != '', \
        f'Отсутствует или не правильная ссылка на лого проекта {text_owner_element}'


def test_h1_mentors(web_browser):
    """Отображение надписи Менторы"""
    page = Projects(web_browser)
    page.WAIT_LOAD()
    for_scroll(page=Projects(web_browser))  # Функция скролла доподвала и обратно
    page.H1_MENTORS.scroll_to_element_js()
    time.sleep(2)
    assert page.H1_MENTORS.is_presented(), 'Нет элемента  Менторы'
    assert page.H1_MENTORS.is_visible(), 'Не видно элемента Менторы'
    assert 'Менторы' in page.H1_MENTORS.get_text(), 'В элементе нет текста Менторы'


@pytest.mark.parametrize('mentors_list', [
    'mentor_1',
    'mentor_2',
    'mentor_3',
    'mentor_4'
    ],
                        ids=[
                            'Ментор_1',
                            'Ментор_2',
                            'Ментор_3',
                            'Ментор_4'
                        ])
def test_mentors_text(web_browser, mentors_list):
    """При нажатии на область ментора , открывается спойлер"""
    dict_mentors = {'mentor_1': 0,
    'mentor_2': 1,
    'mentor_3': 2,
    'mentor_4': 3,
               }
    settings = BasePageSet()
    page = Mentors(web_browser)
    page.WAIT_LOAD()
    for_scroll(page=Projects(web_browser))  # Функция скролла доподвала и обратно

    mentor = page.MENTORS_LIST
    mentor_close = page.MENTORS_LIST_CLOSE
    page.SCROLL_TO_WEB_ELEMENT(mentor[dict_mentors.get(mentors_list)])
    assert mentor[dict_mentors.get(mentors_list)] is not None, f'Нет элемента {mentors_list}'
    assert mentor[dict_mentors.get(mentors_list)].is_displayed(), f'Не видно элемента {mentors_list}'
    assert not page.MENTOR_SPOLER.is_visible(), f'Видно сполер до открытия элемента {mentors_list}'
    mentor[dict_mentors.get(mentors_list)].click()
    time.sleep(2)
    assert page.MENTOR_SPOLER.is_visible(), f'Не видно сполера после открытия {mentors_list}'
    mentor_close[dict_mentors.get(mentors_list)].click()
    assert not page.MENTOR_SPOLER.is_visible(), f'Видно сполер до открытия элемента {mentors_list}'


@pytest.mark.parametrize('mentors_list', [
    'mentor_1',
    'mentor_2',
    'mentor_3',
    'mentor_4'
    ],
                        ids=[
                            'Ментор_1',
                            'Ментор_2',
                            'Ментор_3',
                            'Ментор_4'
                        ])
def test_mentors_photo(web_browser, mentors_list):  # Добавить проверку соответствия фото
    """В элементе фото ментора корректная ссылкана фото"""
    dict_mentors = {'mentor_1': 0,
    'mentor_2': 1,
    'mentor_3': 2,
    'mentor_4': 3,
                    }
    settings = BasePageSet()
    page = Mentors(web_browser)
    page.WAIT_LOAD()
    for_scroll(page=Projects(web_browser))  # Функция скролла доподвала и обратно
    dict_photo = settings.mentors_link_photo
    mentor = page.MENTORS_LIST
    mentor_close = page.MENTORS_LIST_CLOSE
    page.SCROLL_TO_WEB_ELEMENT(mentor[dict_mentors.get(mentors_list)])
    assert mentor[dict_mentors.get(mentors_list)] is not None, f'Нет элемента {mentors_list}'
    assert mentor[dict_mentors.get(mentors_list)].is_displayed(), f'Не видно элемента {mentors_list}'
    assert not page.MENTOR_SPOLER.is_visible(), f'Видно сполер до открытия элемента {mentors_list}'
    mentor[dict_mentors.get(mentors_list)].click()
    time.sleep(2)
    assert page.MENTOR_SPOLER.is_visible(), f'Не видно сполера после открытия {mentors_list}'
    mentors_photo = page.IMG_MENTORS
    with open("namefile.txt", 'w', encoding="utf=8") as myFile:
        print(f'{mentors_photo[dict_mentors.get(mentors_list)].get_attribute("src")} == {dict_photo.get(mentors_list)}', file=myFile)
    assert mentors_photo[dict_mentors.get(mentors_list)].get_attribute("src") == dict_photo.get(mentors_list),\
        f'Ссылкана фото не совпадает {mentors_list}'
    mentor_close[dict_mentors.get(mentors_list)].click()

    assert not page.MENTOR_SPOLER.is_visible(), f'Видно сполер после закрытия элемента элемента {mentors_list}'


@pytest.mark.xfail
@pytest.mark.parametrize('mentors_param', [
    'mentor_1',
    'mentor_2',
    'mentor_3',
    'mentor_4'
    ],
                        ids=[
                            'Ментор_1',
                            'Ментор_2',
                            'Ментор_3',
                            'Ментор_4'
                        ])
def test_mentors_info(web_browser,mentors_param):
    """При открытом спойлере отображается информации о менторе"""
    dict_mentors = {'mentor_1': 0,
                    'mentor_2': 1,
                    'mentor_3': 2,
                    'mentor_4': 3,
                    }
    settings = BasePageSet()
    page = Mentors(web_browser)
    page.WAIT_LOAD()
    for_scroll(page=Projects(web_browser))  # Функция скролла доподвала и обратно
    dict_photo = settings.mentors_link_photo
    mentor = page.MENTORS_LIST
    mentor_close = page.MENTORS_LIST_CLOSE
    mentor_info = page.INFO_MENTORS
    page.SCROLL_TO_WEB_ELEMENT(mentor[dict_mentors.get(mentors_param)])
    mentor[dict_mentors.get(mentors_param)].click()
    time.sleep(2)
    mentor_info_text = mentor_info[dict_mentors.get(mentors_param)].text
    mentor_info_text_clear = mentor_info_text.split('\n')
    for i in range(len(mentor_info_text_clear)):
        assert mentor_info_text_clear[i] in data_mentors_list[dict_mentors.get(mentors_param)].get("quality")[i], \
            f'Не соответствие информации о менторее {mentors_param}'

#
def test_h1_start_up_for(web_browser):
    """Отображение Заголовка StartUp для """
    page = StartUpFor(web_browser)
    page.WAIT_LOAD()
    for_scroll(page=Projects(web_browser))  # Функция скролла доподвала и обратно
    page.START_UP_FOR_H1.scroll_to_element_js()
    time.sleep(2)
    assert page.START_UP_FOR_H1.is_presented(), 'Нет элемента  StartUp для'
    assert page.START_UP_FOR_H1.is_visible(), 'Не видно элемента StartUp для'
    assert 'StartUp для' in page.START_UP_FOR_H1.get_text(), 'В элементе нет текста StartUp для '


def test_h2_start_up_for_juniors(web_browser):
    """Отображение Заголовка h2 Juniors """
    page = StartUpFor(web_browser)
    page.WAIT_LOAD()
    for_scroll(page=Projects(web_browser))  # Функция скролла доподвала и обратно
    page.START_UP_FOR_JUNIORS_H2.scroll_to_element_js()
    time.sleep(2)
    assert page.START_UP_FOR_JUNIORS_H2.is_presented(), 'Нет элемента  Juniors'
    assert page.START_UP_FOR_JUNIORS_H2.is_visible(), 'Не видно элемента Juniors'
    assert 'Juniors' in page.START_UP_FOR_JUNIORS_H2.get_text(), 'В элементе нет текста Juniors'


def test_text_start_up_for_juniors(web_browser):
    """Отображение текста под h2 Juniors"""
    page = StartUpFor(web_browser)
    page.WAIT_LOAD()
    for_scroll(page=Projects(web_browser))  # Функция скролла доподвала и обратно
    page.START_UP_FOR_JUNIORS_H2.scroll_to_element_js()
    time.sleep(2)
    text_h2_juniors = page.START_UP_FOR_JUNIORS_H2
    for text in text_h2_juniors:
        page.SCROLL_TO_WEB_ELEMENT(text)
        assert text is not None, 'Нет элемента  текста Juniors'
        assert text.is_displayed(), 'Не видно элемента текста Juniors'
        #assert '' in page.START_UP_FOR_JUNIORS_H2.get_text(), 'В элементе нет текста под h2 Juniors'




























