# Права доступа. Добавить пользователя. User_1
# Права доступа. Добавить пользователя. User_2
# Права доступа. Добавить пользователя. User_3
# Права доступа. Добавить пользователя. User_4
# Права доступа. Добавить пользователя. User_5
# Права доступа. Добавить пользователя. User_6
# Права доступа. Активные / Неактивные пользователи
# Права доступа. Поле поиск
# Права доступа. Добавить пользователя, отредактировать
# Права доступа. Удалить пользователя
# Права доступа. Удалить всех пользователей




from browser_setup import browser
from test_auth.test_authorization import authorization
from test_access.test_func_access.test_func_add_user_1 import user_1
from test_access.test_func_access.test_func_add_user_2 import user_2
from test_access.test_func_access.test_func_add_user_3 import user_3
from test_access.test_func_access.test_func_add_user_4 import user_4
from test_access.test_func_access.test_func_add_user_5 import user_5
from test_access.test_func_access.test_func_add_user_6 import user_6
from test_access.test_func_access.test_func_active_inactive_user import active_inactive_user
from test_access.test_func_access.test_func_search_access import search_access
from test_access.test_func_access.test_func_edit_user import edit_user
from test_access.test_func_access.test_func_delete_user import delete_user
from test_access.test_func_access.test_func_delete_all_user import delete_all_user
from termcolor import cprint


def test_set_user_access(browser):

    cprint("Авторизация", "green")
    authorization(browser)
    print()

    cprint("Права доступа. Добавить пользователя. User_1", "green")
    user_1(browser)
    print()

    cprint("Права доступа. Добавить пользователя. User_2", "green")
    user_2(browser)
    print()

    cprint("Права доступа. Добавить пользователя. User_3", "green")
    user_3(browser)
    print()

    cprint("Права доступа. Добавить пользователя. User_4", "green")
    user_4(browser)
    print()

    cprint("Права доступа. Добавить пользователя. User_5", "green")
    user_5(browser)
    print()

    cprint("Права доступа. Добавить пользователя. User_6", "green")
    user_6(browser)
    print()

    cprint("Права доступа. Активные / Неактивные пользователи", "green")
    active_inactive_user(browser)
    print()

    cprint("Права доступа. Поле поиск", "green")
    search_access(browser)
    print()

    cprint("Права доступа. Добавить пользователя, отредактировать", "green")
    edit_user(browser)
    print()

    cprint("Права доступа. Удалить пользователя", "green")
    delete_user(browser)
    print()

    cprint("Права доступа. Удалить всех пользователейь", "green")
    delete_all_user(browser)
    print()

