from collections import Counter
from datetime import datetime


def date_string_to_year(date_string):
    dt = datetime.strptime(date_string, '%Y-%m-%d')
    return dt.year


def get_men_counted_by_year(users):
    men = filter(lambda user: user['gender'] == 'male', users)
    birth_years = map(lambda man: date_string_to_year(man['birthday']), men)
    return dict(Counter(birth_years))




users = [
    {'name': 'Bronn', 'gender': 'male', 'birthday': '1973-03-23'},
    {'name': 'Reigar', 'gender': 'male', 'birthday': '1973-11-03'},
    {'name': 'Eiegon', 'gender': 'male', 'birthday': '1963-11-03'},
    {'name': 'Sansa', 'gender': 'female', 'birthday': '2012-11-03'},
    {'name': 'Jon', 'gender': 'male', 'birthday': '1980-11-03'},
    {'name': 'Robb', 'gender': 'male', 'birthday': '1980-05-14'},
    {'name': 'Tisha', 'gender': 'female', 'birthday': '2012-11-03'},
    {'name': 'Rick', 'gender': 'male', 'birthday': '2012-11-03'},
    {'name': 'Joffrey', 'gender': 'male', 'birthday': '1999-11-03'},
    {'name': 'Edd', 'gender': 'male', 'birthday': '1973-11-03'},
]
print(get_men_counted_by_year(users))

