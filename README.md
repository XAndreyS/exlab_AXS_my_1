Версия v.1 - пункты чек листас 1 по 10

ссылка на чек лист:docs.google.com/spreadsheets/d/1VrgvQVA5jsMJJyTWQWoBctUGF6ClUg3lkx3vL6Mr574/edit?pli=1#gid=888275549
Адрес тестового веб приложения: ExLab Landing http://test.exlab.team/#

Files
-----

[conftest.py](conftest.py) содержит весь необходимый код для отлова неудачных тестовых случаев и создания снимка экрана
страницы на случай, если какой-либо тест не пройдёт.

[settings.py] - содержит тестовые данные

[pages/base.py](pages/base.py) содержит реализацию шаблона PageObject для Python.

[pages/elements.py](pages/elements.py) содержит вспомогательный класс для определения веб-элементов на веб-страницах.

[tests/]
test_base_page_head.py


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
