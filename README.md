Версия v.1 - пункты чек листас 1 по 10
Версия v.2 - пункты чек листас 10 по 20
Версия v.3 - пункты чек листас 20 по 30
Версия v.4 - пункты чек листас 30 по 40


ссылка на чек лист:
docs.google.com/spreadsheets/d/1VrgvQVA5jsMJJyTWQWoBctUGF6ClUg3lkx3vL6Mr574/edit?pli=1#gid=888275549
ссылка на чек лист(черновик,для вопросов и правок):
https://docs.google.com/spreadsheets/d/180ZKiMlL9kQ_tkrXBGC5p6YD4FjpuqMrD0YDs9e5ao0/edit#gid=888275549
Адрес тестового веб приложения: ExLab Landing http://test.exlab.team/#

Files
-----

[conftest.py](conftest.py) содержит весь необходимый код для отлова неудачных тестовых случаев и создания снимка экрана
страницы на случай, если какой-либо тест не пройдёт.

[settings.py] - содержит тестовые данные(временные)- будет перенесено в папку [data/]

[pages/base.py](pages/base.py) содержит реализацию шаблона PageObject для Python.

[pages/elements.py](pages/elements.py) содержит вспомогательный класс для определения веб-элементов на веб-страницах.

[tests/]
test_base_page_head.py тесты начальной страницы - шапка
test_base_page_body.py тесты начальной страницы - тело
test_base_page_footer.py тесты начальной страницы - подвал

[data/] содержит тестовые данные(нуждается в доработке)
info_mentors.py


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
