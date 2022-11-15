#!/usr/bin/python3
# -*- encoding=utf8 -*-

import time
from termcolor import colored

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebElement(object):

    _locator = ('', '')
    _web_driver = None
    _page = None
    _timeout = 10
    _wait_after_click = False  # TODO: how we can wait after click? TODO: как мы можем ждать после клика?

    def __init__(self, timeout=10, wait_after_click=False, **kwargs):
        self._timeout = timeout
        self._wait_after_click = wait_after_click

        for attr in kwargs:
            self._locator = (str(attr).replace('_', ' '), str(kwargs.get(attr)))

    def find(self, timeout=10):
        """ Find element on the page.
         Найти элемент на странице"""

        element = None

        try:
            element = WebDriverWait(self._web_driver, timeout).until(
               EC.presence_of_element_located(self._locator)
            )
        except:
            print(colored('Element not found on the page!', 'red'))

        return element

    def wait_to_be_clickable(self, timeout=10, check_visibility=True):
        """ Wait until the element will be ready for click.
         Подождите, пока элемент будет готов к клику."""

        element = None

        try:
            element = WebDriverWait(self._web_driver, timeout).until(
                EC.element_to_be_clickable(self._locator)
            )
        except:
            print(colored('Element not clickable!', 'red'))

        if check_visibility:
            self.wait_until_not_visible()

        return element

    def is_clickable(self):
        """ Check is element ready for click or not.
         Проверить, готов ли элемент к клику или нет."""

        element = self.wait_to_be_clickable(timeout=0.1)
        return element is not None

    def is_presented(self):
        """ Check that element is presented on the page.
         Убедитесь, что элемент представлен на странице."""

        element = self.find(timeout=0.1)
        return element is not None

    def is_visible(self):
        """ Check is the element visible or not.
         Проверить, виден элемент или нет."""

        element = self.find(timeout=0.1)

        if element:
            return element.is_displayed()

        return False

    def wait_until_not_visible(self, timeout=10):
        """ подожди пока не будет видно"""

        element = None

        try:
            element = WebDriverWait(self._web_driver, timeout).until(
                EC.visibility_of_element_located(self._locator)
            )
        except:
            print(colored('Element not visible!', 'red'))

        if element:
            js = ('return (!(arguments[0].offsetParent === null) && '
                  '!(window.getComputedStyle(arguments[0]) === "none") &&'
                  'arguments[0].offsetWidth > 0 && arguments[0].offsetHeight > 0'
                  ');')
            visibility = self._web_driver.execute_script(js, element)
            iteration = 0

            while not visibility and iteration < 10:
                time.sleep(0.5)

                iteration += 1

                visibility = self._web_driver.execute_script(js, element)
                print('Element {0} visibility: {1}'.format(self._locator, visibility))

        return element

    def send_keys(self, keys, wait=2):
        """ Send keys to the element.
        Ввеести текст"""

        keys = keys.replace('\n', '\ue007')

        element = self.find()

        if element:
            element.click()
            element.clear()
            element.send_keys(keys)
            time.sleep(wait)
        else:
            msg = 'Element with locator {0} not found'
            raise AttributeError(msg.format(self._locator))

    def get_text(self):
        """ Get text of the element.
         Получить текст элемента."""

        element = self.find()
        text = ''

        try:
            text = str(element.text)
        except Exception as e:
            print('Error: {0}'.format(e))

        return text

    def get_attribute(self, attr_name):
        """ Get attribute of the element.
         Получить атрибут элемента"""

        element = self.find()

        if element:
            return element.get_attribute(attr_name)

    def _set_value(self, web_driver, value, clear=True):
        """ Set value to the input element.
         Установите значение для элемента ввода."""

        element = self.find()

        if clear:
            element.clear()

        element.send_keys(value)

    def click(self, hold_seconds=0, x_offset=1, y_offset=1):
        """ Wait and click the element.
         Подождите и щелкните элемент."""

        element = self.wait_to_be_clickable()

        if element:
            action = ActionChains(self._web_driver)
            action.move_to_element_with_offset(element, x_offset, y_offset).\
                pause(hold_seconds).click(on_element=element).perform()
        else:
            msg = 'Element with locator {0} not found'
            raise AttributeError(msg.format(self._locator))

        if self._wait_after_click:
            self._page.wait_page_loaded()

    def right_mouse_click(self, x_offset=0, y_offset=0, hold_seconds=0):
        """ Click right mouse button on the element.
         Щелкните правой кнопкой мыши по элементу."""

        element = self.wait_to_be_clickable()

        if element:
            action = ActionChains(self._web_driver)
            action.move_to_element_with_offset(element, x_offset, y_offset). \
                pause(hold_seconds).context_click(on_element=element).perform()
        else:
            msg = 'Element with locator {0} not found'
            raise AttributeError(msg.format(self._locator))

    def highlight_and_make_screenshot(self, file_name='element.png'):
        """ Highlight element and make the screen-shot of all page.
         Выделите элемент и сделайте скриншот всей страницы."""

        element = self.find()

        # Scroll page to the element:
        self._web_driver.execute_script("arguments[0].scrollIntoView();", element)

        # Add red border to the style:
        self._web_driver.execute_script("arguments[0].style.border='3px solid red'", element)

        # Make screen-shot of the page:
        self._web_driver.save_screenshot(file_name)

    def scroll_my_down(self):
        element = self.find()
        element.send_keys(Keys.END)

    def scroll_my_up(self):
        element = self.find()
        element.send_keys(Keys.HOME)

    def scroll_to_element(self):
        """ Scroll page to the element.
         Прокрутите страницу до элемента."""

        element = self.find()

        # Scroll page to the element(Прокрутить страницу до элемента:):
        # Option #1 to scroll to element(Вариант №1 для прокрутки до элемента:):
        # self._web_driver.execute_script("arguments[0].scrollIntoView();", element)

        # Option #2 to scroll to element(Вариант №2 для прокрутки до элемента:):
        try:
            element.send_keys(Keys.DOWN)
        except Exception as e:#
            pass  # Just ignore the error if we can't send the keys to the element -  Просто игнорируйте ошибку, если мы не можем отправить ключи к элементу

    def scroll_to_element_js(self):
        """ Scroll page to the element.
         Прокрутите страницу до элемента."""

        element = self.find()

        # Scroll page to the element(Прокрутить страницу до элемента:):
        # Option #1 to scroll to element(Вариант №1 для прокрутки до элемента:):
        # element.send_keys(Keys.DOWN)

        # Option #2 to scroll to element(Вариант №2 для прокрутки до элемента:):
        try:
            self._web_driver.execute_script("arguments[0].scrollIntoView();", element)
        except Exception as e:#
            pass  # Just ignore the error if we can't send the keys to the element -  Просто игнорируйте ошибку, если мы не можем отправить ключи к элементу

    def delete(self):
        """ Deletes element from the page.
         Удаляет элемент со страницы."""

        element = self.find()

        # Delete element(Удалить элемент:):
        self._web_driver.execute_script("arguments[0].remove();", element)

    def finds(self, timeout=10):
        """ Find elements on the page. Моя добавка, с целью получения списка"""

        elements = []

        try:
            elements = WebDriverWait(self._web_driver, timeout).until(
               EC.presence_of_all_elements_located(self._locator)
            )
        except:
            print(colored('Elements not found on the page!', 'red'))

        return elements

    def move_mouse_on_element(self, hold_seconds=0, x_offset=1, y_offset=1):
        """ Wait and click the element.
         Подождите и щелкните элемент."""

        element = self.wait_to_be_clickable()

        if element:
            action = ActionChains(self._web_driver)
            action.move_to_element_with_offset(element, x_offset, y_offset).\
                pause(hold_seconds).perform()
        else:
            msg = 'Element with locator {0} not found'
            raise AttributeError(msg.format(self._locator))

        if self._wait_after_click:
            self._page.wait_page_loaded()

    def get_property(self, attr_name):
        """ Тестирование моей новой функции"""
        results = []
        element = self.find()

        results= element.get_property(attr_name)

        return results

    def get_css(self, attr_name):
        """ Тестирование моей новой функции, получение css"""
        results = []
        element = self.find()

        results= element.value_of_css_property(attr_name)

        return results


class ManyWebElements(WebElement):

    def __getitem__(self, item):
        """ Get list of elements and try to return required element.
         Получить список элементов и попытаться вернуть требуемый элемент."""

        elements = self.find()
        return elements[item]

    def find(self, timeout=10):
        """ Find elements on the page.
         Найдите элементы на странице.(список)"""

        elements = []

        try:
            elements = WebDriverWait(self._web_driver, timeout).until(
               EC.presence_of_all_elements_located(self._locator)
            )
        except:
            print(colored('Elements not found on the page!', 'red'))  # Элементы не найдены на странице!

        return elements

    def _set_value(self, web_driver, value):
        """ Note: this action is not applicable for the list of elements.
         Примечание: это действие неприменимо для списка элементов."""
        raise NotImplemented('This action is not applicable for the list of elements')

    def click(self, hold_seconds=0, x_offset=0, y_offset=0):
        """ Note: this action is not applicable for the list of elements.
         Примечание: это действие неприменимо для списка элементов."""
        raise NotImplemented('This action is not applicable for the list of elements')

    def count(self):
        """ Get count of elements.
         Получить количество элементов."""

        elements = self.find()
        return len(elements)

    def get_text(self):
        """ Get text of elements.
         Получить текст элементов."""

        elements = self.find()
        result = []

        for element in elements:
            text = ''

            try:
                text = str(element.text)
            except Exception as e:
                print('Error: {0}'.format(e))

            result.append(text)

        return result

    def get_attribute(self, attr_name):
        """ Get attribute of all elements.
         Получить атрибут всех элементов"""

        results = []
        elements = self.find()

        for element in elements:
            results.append(element.get_attribute(attr_name))

        return results

    def highlight_and_make_screenshot(self, file_name='element.png'):
        """ Highlight elements and make the screen-shot of all page.
         Выделите элементы и сделайте скриншот всей страницы."""

        elements = self.find()

        for element in elements:


            # Add red border to the style(Добавьте красную рамку к стилю:):
            self._web_driver.execute_script("arguments[0].style.border='3px solid red'", element)

        # Make screen-shot of the page(Сделайте скриншот страницы:):
        self._web_driver.save_screenshot(file_name)

