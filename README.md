В этом репозитории собраны UI автотесты написанные с помощью Selenium и Python, с применением Pytest. 
Тесты покрывают примерно 80-85% функционала сайта и имеют в основном "позитивные" сценарии.

Файловая структура:

test-selenium-kerong
|- config.py
|- browser_setup.py
|- pytest.ini
|- requirements.txt
|- test_set_add_all.py
|- test_set_client.py
|- test_set_identif.py
|
|-- test_access
|	|--test_func_access
|   		|- __init__.py
|   		|- test_func_add_user_1
|   		|- test_func_delete_all_user
|	|--test_add_user_1
|	|- test_delete_all_user
|
|
|-- test_client
|	|--test_func_client
|   		|- __init__.py
|   		|- test_func_add_client
|   		|- test_func_delete_client
|	|--test_add_client
|	|- test_delete_client


Корневой каталог test-selenium-kerong:
В файле config.py прописаны все переменные используемые в тестах. 
В файле browser_setup.py прописаны настройки браузера для запуска тестов.
Файл requirements.txt содержит список всех библиотек и их версий, необходимых для корректной работы приложения. 
Файл pytest.ini используется для настройки поведения тестового фреймворка pytest. 
Он позволяет определить параметры конфигурации, которые будут применяться при выполнении тестов.
В директориях test_access, test_client и т.д. находятся файлы для запуска отдельных тестовых сценариев. 
В подкаталоге test_func_access, test_func_client расположены файлы с описанием структуру тестов. 
В файлах с названием test_set..py (например, test_set_client.py) содержатся наборы тестовых сценариев.
