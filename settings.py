

class AuthPersonalAreaSettings:

    # Вход по №тел пока отложен, нужно понять как получть код
    # valid_num_phone = '+79068080311'
    valid_num_phone_text = 'Валидный №телефона #1'

    # Вадидные emails, и текст для ids (Личный кабинет — Код скидки 2728-4DD2-B96E)
    valid_email_v1 = 'alone.test1@mail.ru'
    valid_email_v2 = 'alone.test2@mail.ru'
    valid_email_v1_text = 'Валидный email #1'
    valid_email_v2_text = 'Валидный email #2'

    # Невалидные emails, и текст для ids
    invalid_email_v1 = 'фдщту.еуые1@mail.ru'
    invalid_email_v2 = 'фдщту.еуые1@маил.рф'
    invalid_email_v3 = '~!@#$%^&*()_+{}|:”>?<!”}№;%:?*()_+\/,/.,;’[]|.@mail.ru'
    invalid_email_v4 = 'dd@mail..ri'
    invalid_email_v5 = ('a' * 256) + '@mail.ru'
    invalid_email_v6 = ''

    invalid_email_v1_text = "Кириллица в логин почты(до @)"
    invalid_email_v2_text = "Кириллица логина почты(до @) и домена(после @)"
    invalid_email_v3_text = "Латиница логин и домен, в домене лишняя точка"
    invalid_email_v4_text = "Только спецсимволы в логин почты"
    invalid_email_v5_text = "Длинна логина почты 256 букв"
    invalid_email_v6_text = "Пустая сторока"

    # Валидные кодовые номера для входа к акк
    valid_code = '2728-4DD2-B96E'  # Код для акк alone.tests1@mail.ru
    valid_code_v2 = 'DD2B4A95934A'  # Код для акк alone.tests2@mail.ru
    valid_code_text = 'Валидный код #1'
    valid_code_v2_text = 'Валидный код #2 без -, len(10)'
    # Не валидные кодовые номера для входа к акк
    invalid_code_v1 = '2728-4DD2-B96R'
    invalid_code_v2 = '0000-0000-0000'
    invalid_code_v3 = '2' * 256
    invalid_code_v4 = '2728-4DD2-B96R' * 1000
    invalid_code_v5 = '2728-4DD2B96R len(11)'
    invalid_code_v6 = '~!@#$%^&*()_+{}|:”>?<!”}№;%:?*()_+\/,/.,;’[]|'
    invalid_code_v7 = '2728_4DD2_B96E'
    invalid_code_v8 = '2#.28-4DD2-B96!'
    invalid_code_v9 = ''
    invalid_code_v10 = '2728-4DD2-B96'
    invalid_code_v11 = '27284DD2-B96R'

    invalid_code_v1_text = 'Не существующий код'  # Извенен последний символ
    invalid_code_v2_text = 'Проверка на ноль-все '
    invalid_code_v3_text = 'строка 256 символов'
    invalid_code_v4_text = 'строка 12000 символов'
    invalid_code_v5_text = '2728-4DD2B96R len(11) валидный 10 или 12'
    invalid_code_v6_text = 'все спецсимволы в строку'
    invalid_code_v7_text = 'вариант кода вместо - ставим _'
    invalid_code_v8_text = 'Смешанный вариант, часть кода заменил на #.!'
    invalid_code_v9_text = 'Пустая строка'
    invalid_code_v10_text = 'Валибнй без одной цифры'
    invalid_code_v11_text = '27284DD2-B96R len(11) валидный 10 или 12'


