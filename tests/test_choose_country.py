import pytest
from main import choose_country, unique_id, max_volume

FIXTURES = [([
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
    ], 'Россия', [{'visit1': ['Москва', 'Россия']},
 {'visit3': ['Владимир', 'Россия']},
 {'visit7': ['Тула', 'Россия']},
 {'visit8': ['Тула', 'Россия']},
 {'visit9': ['Курск', 'Россия']},
 {'visit10': ['Архангельск', 'Россия']}]),
    ([
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
    ], 'Индия', [{'visit2': ['Дели', 'Индия']}]),
    ([
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
    ], 'Португалия', [{'visit4': ['Лиссабон', 'Португалия']},
                      {'visit6': ['Лиссабон', 'Португалия']}])]

FIXTURES_GEO = [({'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}, [98, 35, 15, 213, 54, 119]),
                ({'user1': [213, 213, 213, 15],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35, 88]}, [98, 35, 15, 213, 54, 119, 88])]

FIXTURES_STATS = [({'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98},
                   'yandex'),
                  ({'telegram': 121, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98},
                   'telegram')]

@pytest.mark.parametrize('a, b, etalon', FIXTURES)
def test_choose_country(a, b, etalon):
    result = choose_country(a, b)
    assert result == etalon

@pytest.mark.parametrize('a, etalon', FIXTURES_GEO)
def test_unique_id(a, etalon):
    result = unique_id(a)
    assert result == etalon

@pytest.mark.parametrize('a, etalon', FIXTURES_STATS)
def test_max_volume(a, etalon):
    result = max_volume(a)
    assert result == etalon
