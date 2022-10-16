#  3) Run tests:
#     python -m pytest -v --driver Chrome --driver-path ~/chrome tests/*

# import time
import pytest
from pages.labirint import MainPage, GeneralSearch
res = None


@pytest.mark.parametrize("search_input", [
        'площадь',
        'ПЛОЩАДЬ',
        'ПлОщаДь',
        'плошад',
        'площаж',
        'плашадь',
        'gkjoflm',
        'square',
        ' площадь ',
        ' площадь',
        'площадь ',
                         ], ids=[
        'поиск работает и ищет, нижний регистр',
        'поиск верхний регистр',
        'поиск смешанны регистр',
        'поиск по включчению слова (плошад)',
        'поиск опечатки v2(площаж)',
        'поиск опечатки v3(плашодь)',
        'поиск не правильная раскладка (площадь)',
        'поиск языки английский',
        'Тримаются  ли открывающие и закрывающие пробелы',
        'Тримаются  ли открывающие и пробелы ',
        'Тримаются  ли закрывающие пробелы '
         ]
)
def test_general_search_pozitiv(web_browser, search_input):
    """Тестирование главного поиска, позитивные проверки"""
    page = GeneralSearch(web_browser)
    page.wait_load()
    page.general_search = search_input
    page.button_search.click()
    page.wait_load()
    result_h1 = page.search_result_h1.get_text()
    card_product = page.card.get_text()
    if search_input == 'square':
        assert 'squar' in result_h1.lower()
        assert 'square' in card_product.lower()
    else:
        assert 'площадь' in result_h1.lower()
        assert 'площадь' in card_product.lower()


@pytest.mark.parametrize("search_input_empty", ['', '          '],
                         ids=['поиск пустое поле (тестирование нуля)',
                              'поиск пустое поле пробелы_10 (тестирование нуля)'])
def test_general_search_empty(web_browser, search_input_empty):
    """Тестирование пустой строки и пробелов(тестирование нуля)"""

    page = GeneralSearch(web_browser)
    page.wait_load()
    page.general_search = search_input_empty
    page.button_search.click()
    page.wait_load()
    result_h1 = page.search_result_h1.get_text()
    if search_input_empty == '':
        assert 'https://www.labirint.ru/' == page.get_url()
    else:
        assert 'Мы ничего не нашли по вашему запросу! Что делать?' in result_h1.lower()


@pytest.mark.parametrize('search_input_symbol',
                         [
                             '~`!@#$%^&*() +{}|:”>?<!”№;%:?*() +/,/.,;’[]\|',
                             'Пока, лосось!',
                             'Иметь или быть?'
                         ],
                         ids=[
                             'специсимволы все ~`!@#$%^&*() +{}|:”>?<!”№;%:?*() +/,/.,;’[]\|',
                             'спецсимволы смешанные, норм поиск где в названии содержится спецсимвол (Пока, лосось!)',
                             'спецсимволы смешанные, норм поиск где в названии содержится спецсимвол (Иметь или быть?)'
                         ])
def test_general_search_symbols(web_browser, search_input_symbol):
    """Тестирование спецсимволов, всех - воспринимает ли их строка,
        и смешанный тип - ищет ли запрос если в запросе есть спецсимвол, и в ответе тоже"""
    page = GeneralSearch(web_browser)
    page.wait_load()
    page.general_search = search_input_symbol
    page.button_search.click()
    page.wait_load()
    result_h1 = page.search_result_h1.get_text()
    card_product = page.card.get_text()

    if search_input_symbol == '~`!@#$%^&*() +{}|:”>?<!”№;%:?*() +/,/.,;’[]\|':
        assert result_h1 == 'Мы ничего не нашли по вашему запросу! Что делать?'
    else:
        assert search_input_symbol.strip().lower() in result_h1.lower()
        assert search_input_symbol.strip().lower() in card_product.lower()


@pytest.mark.parametrize('search_input_emoji',
                         [
                             '🐻',
                             '😀',
                             '🧝‍♀',
                             'ヅ♋'
                             ],
                         ids=[
                             'эмодзи v1',
                             'эмодзи v2',
                             'эмодзи v3',
                             'эмодзи v4'
                         ])
def test_general_search_symbols(web_browser, search_input_emoji):
    """Тестирование спецсимволов, всех - воспринимает ли их строка,
        и смешанный тип - ищет ли запрос если в запросе есть спецсимвол, и в ответе тоже"""
    page = GeneralSearch(web_browser)
    page.wait_load()
    page.general_search = search_input_emoji
    page.button_search.click()
    page.wait_load()
    result_h1 = page.search_result_h1.get_text()

    assert result_h1 == 'Мы ничего не нашли по вашему запросу! Что делать?'


# Верхняя произвольная граница
# 20
# 50
# 100
# 500
# 1000
# 11к)Нижняя граница
# По
# По ворон
# 12л)поиск технологической границы
# 100 000
# 100 миллионов
# 100 миллионов с пробелами
