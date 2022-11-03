#!/usr/bin/python3
# -*- encoding=utf8 -*-

# This is example shows how we can manage failed tests
# and make screenshots after any failed test case.

import pytest
import allure
import uuid
import time


@pytest.fixture
def chrome_options(chrome_options):
    # chrome_options.binary_location = '/usr/bin/google-chrome-stable'
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--log-level=DEBUG')
    #chrome_options.add_argument('--arc-start-mode')
    #chrome_options.add_argument('--disable-glsl-translator')
    #chrome_options.add_argument('--disable-gl-extensions')
    #chrome_options.add_argument('--disable-gpu-memory-buffer-compositor-resources')
    #chrome_options.add_argument('--disable-gl-drawing-for-tests')
    return chrome_options


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # This function helps to detect that some test failed - Эта функция помогает обнаружить, что какой-то тест не пройден.
    # and pass this information to teardown: - и передать эту информацию для разборки:

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def web_browser(request, selenium):

    browser = selenium
    browser.set_window_size(1400, 1000)

    # Return browser instance to test case:
    # Вернуть экземпляр браузера в тестовый пример:
    yield browser

    # Do teardown (this code will be executed after each test):
    # Выполнить разборку (этот код будет выполняться после каждого теста):

    if request.node.rep_call.failed:
        # Make the screen-shot if test failed:
        # Сделать снимок экрана, если тест не пройден:
        try:
            browser.execute_script("document.body.bgColor = 'white';")

            # Make screen-shot for local debug:
            # Сделать скриншот для локальной отладки:
            browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')

            # Attach screenshot to Allure report:
            # Прикрепить скриншот к отчету Allure:
            allure.attach(browser.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)

            # For happy debugging:
            # Для удачной отладки:
            print('URL: ', browser.current_url)
            print('Browser logs:')
            for log in browser.get_log('browser'):
                print(log)

        except:
            pass # just ignore any errors here - просто игнорируйте любые ошибки здесь


def get_test_case_docstring(item):
    """ This function gets doc string from test case and format it
        to show this docstring instead of the test case name in reports.
        Эта функция получает строку документа из тест кейса и форматирует ее.
         чтобы отображать эту строку документации вместо имени тестового примера в отчетах.
    """

    full_name = ''

    if item._obj.__doc__:
        # Remove extra whitespaces from the doc string:
        # Удалить лишние пробелы из строки документа:
        name = str(item._obj.__doc__.split('.')[0]).strip()
        full_name = ' '.join(name.split())

        # Generate the list of parameters for parametrized test cases:
        # Генерируем список параметров для параметризованных тестов:
        if hasattr(item, 'callspec'):
            params = item.callspec.params

            res_keys = sorted([k for k in params])
            # Create List based on Dict:
            # Создать список на основе Dict(словаря):
            res = ['{0}_"{1}"'.format(k, params[k]) for k in res_keys]
            # Add dict with all parameters to the name of test case:
            # Добавляем dict со всеми параметрами к имени теста:
            full_name += ' Parameters ' + str(', '.join(res))
            full_name = full_name.replace(':', '')

    return full_name


def pytest_itemcollected(item):
    """ This function modifies names of test cases "on the fly"
        during the execution of test cases.
        Эта функция изменяет имена тестовых случаев «на лету».
         во время выполнения тестовых случаев.
    """

    if item._obj.__doc__:
        item._nodeid = get_test_case_docstring(item)


def pytest_collection_finish(session):
    """ This function modified names of test cases "on the fly"
        when we are using --collect-only parameter for pytest
        (to get the full list of all existing test cases).
        Эта функция изменяла имена тестовых случаев «на лету».
         когда мы используем параметр --collect-only для pytest
         (чтобы получить полный список всех существующих тестов).
    """

    if session.config.option.collectonly is True:
        for item in session.items:
            # If test case has a doc string we need to modify it's name to - Если в тестовом примере есть строка документа, нам нужно изменить ее имя на
            # it's doc string to show human-readable reports and to - это строка документа для отображения удобочитаемых отчетов и для
            # automatically import test cases to test management system. -  автоматически импортировать тестовые случаи в систему управления тестированием.
            if item._obj.__doc__:
                full_name = get_test_case_docstring(item)
                print(full_name)
        time.sleep(2)
        pytest.exit('Done!')
        #pytest.quit # мои мучения по предотвращению не  закрытия процессов браузера на моём ПК
        time.sleep(3) # # мои мучения по предотвращению не  закрытия процессов браузера на моём ПК