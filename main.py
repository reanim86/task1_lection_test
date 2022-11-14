from pprint import pprint

def choose_country(list_geo, country):
    """
    Функция фильтрует список по заданной стране посещения
    :param list_geo: список для фильтрации
    :param country: страна по которой необходимо отфильтровать
    :return: отфильтрованный список
    """
    write_list = []
    for log in list_geo:
        for geo in log.values():
            if geo[1] == country:
                write_list.append(log)
    return write_list

def unique_id(list_geo):
    """
    Функция выбирает уникальные гео id
    :param list_geo: список словарей
    :return: список с уникальными geo id
    """
    geo_ID = set()
    for unique in list_geo.values():
        geo_ID = geo_ID.union(unique)
    return list(geo_ID)

def max_volume(list_advertisement):
    max_sales = 0
    max_channel = ' '
    for channel, sales in list_advertisement.items():
        if max_sales < sales:
            max_sales = sales
            max_channel = channel
    return max_channel


if __name__ == '__main__':
    geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}
    stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
    pprint(max_volume(stats))
    pprint(unique_id(ids))
    pprint(choose_country(geo_logs, 'Россия'))


