# Открыть зону
# Открыть ячейку (со стартовой страницы)
# Открыть ячейку (внутри ячейки)
# Снять все аренды (будущие и текущие)
# Добавить аренду к существ.аренде
# Создать аренду (внутри зоны)
# Создать аренду (внутри ячейки)
# Снять аренду (внутри ячейки)
# Открыть арендованную ячейку
# Установить статус Авария в свободной ячеейке
# Снятие статуса Авария
# Открытие ячейки (одну)
# Открытие ячейки (несколько)
# Открытие ячейки (по статусу - занятые)
# Открытие ячейки (по статусу - свободные)
# Открытие ячейки (по статусу - все)
# Поле Поиск
# Фильтр
# Будущие аренды. Создать
# Будущие аренды. Снять аренду


from browser_setup import browser
from test_auth.test_authorization import authorization
from test_monitoring.test_func_monitoring.test_func_open_zone_monitoring import open_monitor
from test_monitoring.test_func_monitoring.test_func_open_lock import open_lock
from test_monitoring.test_func_monitoring.test_func_open_lock_in_lock import open_lock_in_lock
from test_monitoring.test_func_monitoring.test_func_delete_all_rent import delete_all_rent
from test_monitoring.test_func_monitoring.test_func_double_rental import double_rental
from test_monitoring.test_func_monitoring.test_func_create_rent_in_zona import create_rent_in_zona
from test_monitoring.test_func_monitoring.test_func_create_rent_in_cell import create_rent_in_cell
from test_monitoring.test_func_monitoring.test_func_open_lock_rent_in_cell import open_lock_rent_in_cell
from test_monitoring.test_func_monitoring.test_func_delete_rent_in_cell import delete_rent_in_cell
from test_monitoring.test_func_monitoring.test_func_status_of_accident_in_free_cell import status_of_accident_in_free_cell
from test_monitoring.test_func_monitoring.test_func_remove_accident_status import remove_accident_status
from test_monitoring.test_func_monitoring.test_func_open_lock_one_in_zona import open_lock_one
from test_monitoring.test_func_monitoring.test_func_open_some_lock_in_zona import open_lock_some
from test_monitoring.test_func_monitoring.test_func_open_rent_lock_in_zona import open_lock_rent
from test_monitoring.test_func_monitoring.test_func_open_free_lock_in_zona import open_lock_free
from test_monitoring.test_func_monitoring.test_func_open_all_lock_in_zona import open_lock_all
from test_monitoring.test_func_monitoring.test_func_search_monitoring import search_monitoring
from test_monitoring.test_func_monitoring.test_func_filter_accident_lock_monitoring import filter_accident_lock_monitoring
from test_monitoring.test_func_monitoring.test_func_filter_free_lock_monitoring import filter_free_lock_monitoring
from test_monitoring.test_func_monitoring.test_func_filter_rent_lock_monitoring import filter_rent_lock_monitoring
from test_monitoring.test_func_monitoring.test_func_filter_all_lock_monitoring import filter_all_lock_monitoring
from test_monitoring.test_func_monitoring.test_func_future_rent_monitoring import future_rent_monitoring
from test_monitoring.test_func_monitoring.test_func_delete_future_rent_monitoring import delete_future_rent_monitoring
from termcolor import cprint





def test_set_motitoring(browser):

    cprint("Авторизация", "green")
    authorization(browser)
    print()

    cprint("Открыть зону", "green")
    open_monitor(browser)
    print()

    cprint("Открыть ячейку (со стартовой страницы)", "green")
    open_lock(browser)
    print()

    cprint("Открыть ячейку (внутри ячейки)", "green")
    open_lock_in_lock(browser)
    print()

    cprint("Снять все аренды (будущие и текущие)", "green")
    delete_all_rent(browser)
    print()

    # Добавить аренду к существ.аренде
    cprint("Добавить аренду к существ.аренде", "green")
    double_rental(browser)
    print()

    cprint("Создать аренду (внутри зоны)", "green")
    create_rent_in_zona(browser)
    print()

    cprint("Создать аренду (внутри ячейки)", "green")
    create_rent_in_cell(browser)
    print()

    cprint("Открыть арендованную ячейку", "green")
    open_lock_rent_in_cell(browser)
    print()

    cprint("Снять аренду (внутри ячейки)", "green")
    delete_rent_in_cell(browser)
    print()

    cprint("Установить статус Авария в свободной ячеейке", "green")
    status_of_accident_in_free_cell(browser)
    print()

    cprint("Снятие статуса Авария", "green")
    remove_accident_status(browser)
    print()

    cprint("Открытие ячейки (одну)", "green")
    open_lock_one(browser)
    print()

    cprint("Открытие ячейки (несколько)", "green")
    open_lock_some(browser)
    print()

    cprint("Открытие ячейки (по статусу - занятые)", "green")
    open_lock_rent(browser)
    print()

    cprint("Открытие ячейки (по статусу - свободные)", "green")
    open_lock_free(browser)
    print()

    cprint("Открытие ячейки (по статусу - все)", "green")
    open_lock_all(browser)
    print()

    cprint("Поле Поиск", "green")
    search_monitoring(browser)
    print()

    cprint("Фильтр", "green")
    filter_accident_lock_monitoring(browser)
    print()
    filter_free_lock_monitoring(browser)
    print()
    filter_rent_lock_monitoring(browser)
    print()
    filter_all_lock_monitoring(browser)
    print()

    cprint("Будущие аренды. Создать", "green")
    future_rent_monitoring(browser)
    print()

    cprint("Будущие аренды. Снять аренду", "green")
    delete_future_rent_monitoring(browser)

