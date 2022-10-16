Introduction
------------

This repository contains basic example of usage PageObject
pattern with Selenium and Python (PyTest + Selenium).

Video screencast with the description ot this code:
https://www.youtube.com/watch?v=BRxp1Kn1G7w


Files
-----

[conftest.py](conftest.py) содержит весь необходимый код для отлова неудачных тестовых случаев и создания снимка экрана
страницы на случай, если какой-либо тест не пройдёт.

[settings.py] - содержит тестовые данные

[pages/base.py](pages/base.py) содержит реализацию шаблона PageObject для Python.

[pages/elements.py](pages/elements.py) содержит вспомогательный класс для определения веб-элементов на веб-страницах.

[tests/](tests/test_general_searh.py, test_header_menu.py, test_per_area.py, test_card_product)
 содержат Web UI тесты для Лабиринт (https://labirint.ru/)
test_general_searh.py  - проверки общей поисково строки (

)
test_header_menu.py - прокликивание навигационного меню в шапке(
Книги, Главное2022, Школа, Канцтовары, клуб
)
test_per_area.py - проверка Личного кабинета(
Проверка иконки Личного кабинета- клик на иконку, прокликивание  всплывающего меню.
Проверка входа в Личный кабинет- по  использованю почты(пока ток позитивные для почты ) и подтверждению при помощи
ключа-кода, вход используя код-ключ
)
test_card_product - проверка количества карточек товара на сайте
Подробнее про проверки см:
 _https://docs.google.com/document/d/1ZKM_i8HUbqVC75ZVe15vxBol_cG5VryAaGYNORmcTzE/edit?usp=sharing_ 


How To Run Tests
----------------

1) Install all requirements:

    ```bash
    pip3 install -r requirements
    ```

2) Download Selenium WebDriver from https://chromedriver.chromium.org/downloads (choose version which is compatible with your browser)
https://pypi.org/project/webdriver-manager/ - ссылка на установку  драверачерез pip
3) Run tests:

    ```bash
    python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
    ```

   ![alt text](example.png)

Note:
~/chrome in this example is the file of Selenium WebDriver downloaded and unarchived on step #2.
