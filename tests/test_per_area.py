#  3) Run tests:
#     python -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
# pytest --driver Firefox --driver-path /path/to/geckodriver.exe
# --maxfail=2 -  остановить  после 2 упавших
# pytest -x --pdb   # вызывает отладчик при первом падении и завершает тестовую сессию
# pytest --pdb --maxfail=3  # вызывает отладчик для первых трех падений

import time
import pytest
from settings import AuthPersonalAreaSettings
from pages.labirint import AuthPersonalArea, PersonalAreaIcon
# MainPage, PersonalArea,


@pytest.mark.parametrize("icon", [
    'Дарим_50р',
    'баллы_за_отзывы',
    'постоянная_скидка',
    'вход',
    'иконка'
], ids=[
    'Дарим 50р',
    'баллы за отзывы',
    'постоянная скидка',
    'вход или регистрация',
    'Клик по самой  иконке личного кабинета'
])
def test_personal_area_icon_no_auth(web_browser, icon):
    """Проверка иконки линого кабинета, не авторизован"""

    per_area = PersonalAreaIcon(web_browser)

    per_area.wait_load()
    per_area.per_area_icon.move_mouse_on_element()
    time.sleep(1)
    per_x = per_area.page_per_area_icon.get_text()

    if icon == 'Дарим_50р':
        assert per_area.donate_50.get_text() in per_x
        per_area.donate_50.click()
        per_area.wait_load()
        assert 'Полный доступ к Лабиринту' in per_area.window_log_reg_h1.get_text()
    elif icon == 'баллы_за_отзывы':
        assert per_area.points_reviews.get_text() in per_x
        per_area.points_reviews.click()
        per_area.wait_load()
        assert per_area.get_url() == 'https://www.labirint.ru/top/bonus-za-recenziyu/'
    elif icon == 'постоянная_скидка':
        assert per_area.permanent_discount.get_text() in per_x
        per_area.permanent_discount.click()
        per_area.wait_load()
        assert per_area.get_url() == 'https://www.labirint.ru/help/?cardhelp=103'
    elif icon == 'вход':
        assert per_area.login_register.get_text() in per_x
        per_area.login_register.click()
        per_area.wait_load()
        assert 'Полный доступ к Лабиринту' in per_area.window_log_reg_h1.get_text()
    elif icon == 'иконка':
        per_area.per_area_icon.click()
        per_area.wait_load()
        assert 'Полный доступ к Лабиринту' in per_area.window_log_reg_h1.get_text()


def test_window_login_register_text(web_browser):
    """Проверка текста формы окна входа/регистрации"""
    window_auth = AuthPersonalArea(web_browser)

    window_auth.wait_load()
    window_auth.per_area_icon.click()
    window_auth.wait_load()
    window_x = window_auth.window_login_register.get_text()
    assert window_auth.window_log_reg_h1.get_text() in window_x
    assert window_auth.field_input_h1.get_text() in window_x
    assert window_auth.button_auth_h1.get_text() in window_x
    assert window_auth.field_input.get_text() in window_x
    assert window_auth.other_login_methods.get_text() in window_x
    assert window_auth.user_agreement.get_text() in window_x
    assert window_auth.rules_agreement.get_text() in window_x
    msg = 'Ошибка в тексте пользовательского соглашения "{}"'.format(window_auth._web_driver.save_screenshot
                                                                     ('screenshot/window_login_register.png'))
    assert 'Авторизируясь в Лабиринте, я подтверждаю' in window_x, msg
    window_auth._web_driver.save_screenshot('screenshot/window_login_register.png')


auth_data_value = AuthPersonalAreaSettings


@pytest.mark.parametrize("code_data", [
    auth_data_value.valid_code,
    auth_data_value.invalid_code_v1,
    auth_data_value.invalid_code_v2,
    auth_data_value.invalid_code_v3,
    auth_data_value.invalid_code_v4,
    auth_data_value.invalid_code_v5,
    auth_data_value.invalid_code_v6,
    auth_data_value.invalid_code_v7,
    auth_data_value.invalid_code_v8,
    auth_data_value.invalid_code_v9,
    auth_data_value.invalid_code_v10,
    auth_data_value.invalid_code_v11
], ids=[
    auth_data_value.valid_code_text,
    auth_data_value.invalid_code_v1_text,
    auth_data_value.invalid_code_v2_text,
    auth_data_value.invalid_code_v3_text,
    auth_data_value.invalid_code_v4_text,
    auth_data_value.invalid_code_v5_text,
    auth_data_value.invalid_code_v6_text,
    auth_data_value.invalid_code_v7_text,
    auth_data_value.invalid_code_v8_text,
    auth_data_value.invalid_code_v9_text,
    auth_data_value.invalid_code_v10_text,
    auth_data_value.invalid_code_v11_text
])
@pytest.mark.parametrize("auth_data", [
    auth_data_value.valid_email_v1,
    auth_data_value.valid_email_v2,
], ids=[
    auth_data_value.valid_email_v1_text,
    auth_data_value.valid_email_v2_text,
])
def test_auth_personal_area_email_code(web_browser, auth_data, code_data):
    """Проверка входа/аунтетификации в личны кабинет, вход по:
    валидному email и валидному и не валидному коду"""
    # В целях сокращения кол-ва тестов принял решение разделить параметризацию
    # думаю нет смысла проверять код доступа, если почта не валидна, а проверку почты сделать отдельно
    per_auth = AuthPersonalArea(web_browser)

    per_auth.wait_load()
    per_auth.per_area_icon.click()
    per_auth.wait_load()
    window_x = per_auth.window_login_register.get_text()
    assert per_auth.window_log_reg_h1.get_text() in window_x
    per_auth.field_input.send_keys(auth_data)
    assert per_auth.button_auth.is_clickable() == True
    per_auth.button_auth.click()
    per_auth.wait_load()
    assert per_auth.window_enter_code.is_visible() == True
    per_auth.field_input_code.send_keys(code_data)
    if len(code_data) == 12 or len(code_data) == 14:
        assert per_auth.button_auth_code.is_clickable() == True
        per_auth.button_auth_code.click()
        per_auth.wait_load()
        if per_auth.window_well_come.is_visible() == True:
            assert 'Здравствуйте' and 'Ваш код авторизации' in per_auth.window_well_come.get_text()
            per_auth.wait_load()
            per_auth.per_area_icon.click()
            per_auth.wait_load()
            assert "Личный кабинет" in per_auth.page_auth_h1.get_text(), "Заголовок личчного кабинета отсутствует"
            per_auth.page_auth_my_data.click()
            per_auth.wait_load()
            assert per_auth.page_auth_my_data_email.get_attribute('value') == auth_data
        else:
            assert 'Сервис недоступен' or 'Введенного кода не существует' in per_auth.button_auth_h1.get_text(), \
                'Или какое то другое сообщение'
    else:
        assert per_auth.button_auth.is_clickable() is False,  "Проблема с определением НЕКЛИКАБЕЛЬНЫЙ"
        per_auth.wait_load()
        time.sleep(2)


@pytest.mark.parametrize("code_data", [
    auth_data_value.valid_code,
    auth_data_value.valid_code_v2,
    auth_data_value.invalid_code_v1,
    auth_data_value.invalid_code_v2,
    auth_data_value.invalid_code_v3,
    auth_data_value.invalid_code_v4,
    auth_data_value.invalid_code_v5,
    auth_data_value.invalid_code_v6,
    auth_data_value.invalid_code_v7,
    auth_data_value.invalid_code_v8,
    auth_data_value.invalid_code_v9
], ids=[
    auth_data_value.valid_code_text,
    auth_data_value.valid_code_v2_text,
    auth_data_value.invalid_code_v1_text,
    auth_data_value.invalid_code_v2_text,
    auth_data_value.invalid_code_v3_text,
    auth_data_value.invalid_code_v4_text,
    auth_data_value.invalid_code_v5_text,
    auth_data_value.invalid_code_v6_text,
    auth_data_value.invalid_code_v7_text,
    auth_data_value.invalid_code_v8_text,
    auth_data_value.invalid_code_v9_text
])
def test_auth_personal_area_code(web_browser, code_data):

    """Проверка входа/аунтетификации в личны кабинет, позитивные тесты
    вход по:код-скидки"""
    per_auth = AuthPersonalArea(web_browser)

    per_auth.wait_load()
    per_auth.per_area_icon.click()
    per_auth.wait_load()
    window_x = per_auth.window_login_register.get_text()
    assert per_auth.window_log_reg_h1.get_text() in window_x
    per_auth.field_input.send_keys(code_data)
    if len(code_data) == 12 or len(code_data) == 14:
        assert per_auth.button_auth.is_clickable() is True
        per_auth.button_auth.click()
        per_auth.wait_load()
        if per_auth.window_well_come.is_visible() is True:
            assert 'Здравствуйте' and 'Ваш код авторизации' in per_auth.window_well_come.get_text()
            per_auth.wait_load()
            per_auth.per_area_icon.click()
            per_auth.wait_load()
            assert "Личный кабинет" in per_auth.page_auth_h1.get_text(), "Заголовок личчного кабинета отсутствует"
        else:
            assert 'Сервис недоступен' or 'Введенного кода не существует' in per_auth.button_auth_h1.get_text(),\
                'Или какое то другое сообщение'
    else:
        assert 'Сервис недоступен' or 'Введенного кода не существует' in per_auth.button_auth_h1.get_text(),\
            'Или какое то другое сообщение'
















