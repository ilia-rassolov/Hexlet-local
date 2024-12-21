""" Задача 4
напишите декоратор который перезапускать функцию в случае ошибки.
Добавить вывод в консоль время выполнении функции func
Добавить интервал в МС между повторными вызовами функции

"""

def retry(limit=5):
    def inner(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < limit:
                try:
                    return func(*args, **kwargs)
                except:
                    retries += 1
                    if retries == limit:
                        raise

        return wrapper

    return inner


@retry(limit=10, interval=1)
def magic():
    raise ValueError('BOOM!')


magic()





