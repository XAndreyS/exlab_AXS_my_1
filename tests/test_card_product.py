#  3) Run tests:
#     python -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
# pytest --driver Firefox --driver-path /path/to/geckodriver.exe
# --maxfail=2 -  остановить  после 2 упавших
# pytest -x --pdb   # вызывает отладчик при первом падении и завершает тестовую сессию
# pytest --pdb --maxfail=3  # вызывает отладчик для первых трех падений

from pages.labirint import CardProduct


def test_amount_product_book(web_browser):
    """Проверяем кол-во карточчек продукта в разделе Книги"""

    prod_card = CardProduct(web_browser)

    # В навигации нажать на раздел Книги
    prod_card.nav_book.click()
    # Проверить переход в раздел
    prod_card.nav_book_end.get_text()
    assert "Книги" in prod_card.nav_book_end.get_text(), "Не перешли в раздел книги"
    # Скролл до заголовка: Все в жанре «Книги»
    prod_card.product_list_h1.scroll_to_element()
    # Запрос кол-ва товара из страницы
    amount_product = prod_card.product_amount.get_text()
    amount_product = amount_product.replace('книг', '')  # Убираем слово книги, далее уберём и пробелы
    # список карточек
    # cards_product = prod_card.product_card.get_text()
    # Список кнопок пагинации
    res_pag = prod_card.pag_list.get_text()

    def paginatia(num):
        """Поиск максимального значения пагинации и приведения строк в числа"""
        pag_m = []  # переменная для хранения максимального значения пагинаии
        for i in num:
            if i == '':
                res_pag.pop(0)
            else:
                pag_m.append(int(i))
        return max(pag_m)
    # Записываем в переменную максимальное кол-во доступных страниц в пагинации
    pag_max = paginatia(res_pag)
    # Переменная для будущего подсчета карточек на сайте
    res_pag_list = []
    cards_product_count = 0
    for n in range(pag_max-1):  # Цикл для перелистывания страниц сайта и подсчета кол-вва карточек товара на сайте
        p = 0

        prod_card.pag_next.scroll_to_element()
        if p < pag_max:
            p += n
            prod_card.wait_load()
            prod_card.pag_next.wait_to_be_clickable()
            prod_card.wait_load()
            prod_card.pag_next.scroll_to_element()
            prod_card.pag_next.click()
            prod_card.pag_next.scroll_to_element()
            prod_card.wait_load()
            res_pag_list.append(prod_card.pag_num.get_text())
            cards_product_count += prod_card.product_card.count()
        else:
            f"Пагинация упала"
    amount_product_text = int(amount_product.replace(' ', ''))
    assert cards_product_count == int(amount_product.replace(' ', '')), \
        f'Кол-во товаров на сайте {cards_product_count} не равно колву товаров в поиске {amount_product_text}'
