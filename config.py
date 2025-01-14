import random

# авторизация
log_in = "admin"
password = "masterkey"
servername = "192.168.25.153"
port_auth = "9777"

# Создание соединения керонг апи
address_input = "192.168.25.153"
port_api = "9991"

# Новый IP при редактировании карточки kerong api
address_input_1 = f"192.168.25.{random.randint(100, 999)}"
port_api_1 = "9991"
new_address_input_1 = f"192.168.25.{random.randint(100, 999)}"

# Новый IP при редактировании карточки kerong api
address_input_2 = f"192.168.25.{random.randint(100, 999)}"
port_api_2 = "9991"
new_address_input_2 = f"192.168.25.{random.randint(100, 999)}"


# Создание платы BU
name_BU_text = f"BU_тест_{random.randint(100, 999)}"
#name_BU_text = "BU_test"
ip_plata = "192.168.25.184"

# Создание и редактирование платы BU
edit_name_BU = f"Новая_BU_{random.randint(10, 99)}"
edit_ip_plata = f"192.168.25.{random.randint(100, 999)}"
# Редактирование
new_edit_name_BU = "Новая_плата_BU_тест"
new_edit_ip_plata = f"192.168.25.{random.randint(100, 999)}"


# Создание платы CU
name_CU_text = f"CU_тест_{random.randint(100, 999)}"
#name_CU_text = "CU_test"
number_in_chain = "0"

# Создание и редактирование платы CU
edit_name_CU = f"Новая_CU_{random.randint(10, 99)}"
edit_number_in_chain = f"{random.randint(0, 9)}"
# Редактирование
new_edit_name_CU = f"Новая_CU_{random.randint(10, 99)}"
new_edit_number_in_chain = f"{random.randint(0, 9)}"


# Создание зоны публичной
name_zone_publ = "Сейфовые ячейки"
num_from_publ = "16"
num_to_publ = "25"
# Создание набора замков
name_lock_publ = "Замки_тест_публ"


# Создание зоны приватной
name_zone_private = "VIP (приватные шкафы)"
num_from_private = "6"
num_to_private = "10"
# Создание набора замков
name_lock_priv = "Замки_тест_прив"


# Создание зоны корпоративной
name_zone_corp = "Мужская раздевалка"
num_from_corp = "11"
num_to_corp = "15"
# Создание набора замков
name_lock_corp = "Замки_тест_корп"


# Создание и удаление набора замков
zona_2 = f"Зона_тест_{random.randint(10, 99)}"
num_from_2 = "47"
num_to_2 = "48"
# Создание набора замков
new_name_lock = f"Замки_тест_{random.randint(100, 999)}"


# Создание типа идентификатора
name_type_identif = f"ТИ_тест_{random.randint(10, 99)}"

# Создание идентификатор
name_identif = f"Идентификатор_тест_{random.randint(10, 99)}"





