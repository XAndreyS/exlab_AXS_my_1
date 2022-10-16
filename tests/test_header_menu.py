#  3) Run tests:
#     python -m pytest -v --driver Chrome --driver-path ~/chrome tests/*


from pages.labirint import MainPage
res = None


def test_nav_menu_click_book(web_browser):

    """Тестирование меню навигации в шапке, прокликивание, раздел Книги"""

    page = MainPage(web_browser)
    page.nav_book.click()
    page.wait_load()
    book_end_h1 = page.nav_book_end.get_text()
    assert 'https://www.labirint.ru/books/' == page.get_url(), "Что то с ссылкой, раздела книги"
    assert "книги" in book_end_h1.lower(), "В заголовке h1 нет слова книги"


def test_nav_menu_click_general(web_browser):
    """Тестирование меню навигации в шапке, прокликивание, раздел Главное 2022"""

    page = MainPage(web_browser)

    page.nav_general.click()
    page.wait_load()
    general_end_h1 = page.nav_general_end.get_text()
    assert 'https://www.labirint.ru/best/' == page.get_url(), "Что то с ссылкой, раздела главное 2022"
    assert 'глав' in general_end_h1.lower(), "В заголовке нет чати слова главное(глав)"


def test_nav_menu_click_shool(web_browser):
    """Тестирование меню навигации в шапке, прокликивание, раздел школа"""

    page = MainPage(web_browser)

    page.nav_shool.click()
    page.wait_load()
    shool_end_h1 = page.nav_shool_end.get_text()
    assert 'https://www.labirint.ru/school/' == page.get_url(), "что то с ссылкой, раздела школа"
    assert 'учебники' in shool_end_h1.lower(), "В заголовке нет слова учебники"


def test_nav_menu_click_game(web_browser):
    """Тестирование меню навигации в шапке, прокликивание, раздел игрушки"""

    page = MainPage(web_browser)

    page.nav_game.click()
    page.wait_load()
    game_end_h1 = page.nav_game_end.get_text()
    assert 'https://www.labirint.ru/games/' == page.get_url(), "что  то с ссылкой раздела игры"
    assert 'игры' in game_end_h1.lower(), "В заголовке нет слова игры"


def test_nav_menu_click_office(web_browser):
    """Тестирование меню навигации в шапке, прокликивание, раздел канцтовары"""

    page = MainPage(web_browser)

    page.nav_office.click()
    page.wait_load()
    office_end_h1 = page.nav_office_end.get_text()
    assert 'https://www.labirint.ru/office/' == page.get_url(), "Что то с ссылкой, раздела канцтовары"
    assert 'канц' in office_end_h1.lower(), "В заголовке нет части cлова канцтовары или ка то так(канц)"


def test_nav_menu_click_club(web_browser):
    """Тестирование меню навигации в шапке, прокликивание, раздел клуб"""

    page = MainPage(web_browser)

    page.nav_club.click()
    page.wait_load()
    club_end_h1 = page.nav_club_end.get_text()
    assert 'https://www.labirint.ru/club/' == page.get_url(), "Что то с ссылкой, раздела клуб"
    assert 'клуб' in club_end_h1.lower(), "В заголовке нет слова клуб"



