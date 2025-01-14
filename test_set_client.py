# Авторизация
# Добавление клиента
# Редактирование
# Снять активность
# Вернуть активность
# Поиск: По имени, По телефону, По идентификатору
# Фильтры: Пол, Дата рождения
# Печать данных
# Привязка клиенту идентификатора (Добавить)
# Привязка клиенту идентификатора (Выбрать)
# Удалить идентификатор
# Добавить доступ (аренда) по идентификатору (приватная аренда)
# Добавить доступ (аренда) по номеру + код (приватная аренда)
# Добавить доступ к корп.зонам
# Добавить доступ (аренда) по идентификатору (корп.аренда)
# Добавить доступ (аренда) телефон+код (корп.аренда)
# Удалить доступ к ячейкам
# Удалить доступ к корп.зонам
# Пароль приложение



from browser_setup import browser
from test_auth.test_authorization import authorization
from test_client.test_func_client.test_func_add_client import add_client
from test_client.test_func_client.test_func_client_activation import client_activation
from test_client.test_func_client.test_func_deactivating_client import deactivating_client
from test_client.test_func_client.test_func_search_client import search_client
from test_client.test_func_client.test_func_edit_client import edit_client
from test_client.test_func_client.test_func_filter_female import filter_female
from test_client.test_func_client.test_func_filter_male import filter_male
from test_client.test_func_client.test_func_filter_birthday import filter_birthday
from test_client.test_func_client.test_func_downloads_client import downloads_client
from test_client.test_func_client.test_func_add_ident_in_client import add_ident_in_client
from test_client.test_func_client.test_func_choose_indent_in_client_1 import choose_indent_in_client
from test_client.test_func_client.test_func_delete_ident_in_client import delete_ident_in_client
from test_client.test_func_client.test_func_add_privat_rent_ident_in_client import add_privat_rent_ident_in_client
from test_client.test_func_client.test_func_add_privat_rent_phone_in_client import add_privat_rent_phone_in_client
from test_client.test_func_client.test_func_access_corporate_zone import access_corporate_zone
from test_client.test_func_client.test_func_add_corp_rent_ident_in_client import add_corp_rent_ident_in_client
from test_client.test_func_client.test_func_add_corp_rent_phone_in_client import add_corp_rent_phone_in_client
from test_client.test_func_client.test_func_delete_rent_in_client import delete_rent_in_client
from test_client.test_func_client.test_func_delete_access_corporate_zone import delete_access
from test_client.test_func_client.test_func_add_password_in_client import add_password_in_client
from termcolor import cprint



def test_client(browser):

    # Вызов функции авторизации
    cprint("Авторизация", "green")
    authorization(browser)
    print()

    cprint("Добавление клиента", "green")
    add_client(browser)
    print()

    cprint("Редактирование клиента", "green")
    edit_client(browser)
    print()

    cprint("Снять активность", "green")
    deactivating_client(browser)
    print()

    cprint("Вернуть активность", "green")
    client_activation(browser)
    print()

    cprint("Поле Поиск", "green")
    search_client(browser)
    print()

    cprint("Фильтр: ж.пол", "green")
    filter_female(browser)
    print()

    cprint("Фильтр: м.пол", "green")
    filter_male(browser)
    print()


    cprint("Фильтр по дате рождения", "green")
    filter_birthday(browser)
    print()


    cprint("Печать данных", "green")
    downloads_client(browser)
    print()


    cprint("Привязка клиенту идентификатора (Добавить)", "green")
    add_ident_in_client(browser)
    delete_ident_in_client(browser)
    print()


    cprint("Привязка клиенту идентификатора (Выбрать)", "green")
    choose_indent_in_client(browser)
    delete_ident_in_client(browser)
    print()


    cprint("Добавить доступ (аренда) по идентификатору (приватная аренда)", "green")
    add_ident_in_client(browser)
    add_privat_rent_ident_in_client(browser)
    delete_rent_in_client(browser)
    delete_ident_in_client(browser)
    print()


    cprint("Добавить доступ (аренда) по номеру + код (приватная аренда)", "green")
    add_ident_in_client(browser)
    add_privat_rent_phone_in_client(browser)
    delete_rent_in_client(browser)
    delete_ident_in_client(browser)
    print()


    cprint("Добавить доступ к корп.зонам", "green")
    add_ident_in_client(browser)
    access_corporate_zone(browser)
    delete_ident_in_client(browser)
    print()

    cprint("Добавить доступ (аренда) по идентификатору (корп.аренда)", "green")
    add_ident_in_client(browser)
    access_corporate_zone(browser)
    add_corp_rent_ident_in_client(browser)
    delete_rent_in_client(browser)
    delete_ident_in_client(browser)
    print()


    cprint("Добавить доступ (аренда) телефон+код (корп.аренда)", "green")
    add_ident_in_client(browser)
    access_corporate_zone(browser)
    add_corp_rent_phone_in_client(browser)
    delete_rent_in_client(browser)
    delete_ident_in_client(browser)
    print()

    cprint("Удалить доступ к ячейкам", "green")
    add_ident_in_client(browser)
    add_privat_rent_ident_in_client(browser)
    delete_rent_in_client(browser)
    delete_ident_in_client(browser)
    print()

    cprint("Удалить доступ к корп.зонам", "green")
    add_ident_in_client(browser)
    access_corporate_zone(browser)
    delete_access(browser)
    delete_ident_in_client(browser)
    print()

    cprint("Пароль приложение", "green")
    add_ident_in_client(browser)
    add_password_in_client(browser)




