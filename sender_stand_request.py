import requests
import configuration
import data

def get_docs():
    # Выполняем GET-запрос к URL, который складывается из базового URL-адреса сервиса
    # и пути к документации, заданных в модуле конфигурации
    # Функция возвращает объект ответа от сервера
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

def get_logs():
    # Складываем базовый URL из конфигурационного файла и путь к основным логам,
    # чтобы сформировать полный URL для запроса.
    # Возвращает объект ответа, полученный от сервера после выполнения GET-запроса
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH)

def get_users_table():
    # Составление полного URL пути к данным таблицы пользователей
    # путем конкатенации базового URL сервиса и конечной точки таблицы пользователей
    # Возвращает объект ответа от сервера
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user(body):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    # URL_SERVICE и CREATE_USER_PATH объединяются для формирования полного URL для запроса
    # json=body используется для отправки данных пользователя в формате JSON
    # headers=data.headers устанавливает заголовки запроса из модуля data
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

def post_products_kits(ids):
    url = configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH
    return requests.post(url, headers=data.headers,
                         json=ids)
