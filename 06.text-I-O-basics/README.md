**a_Global_search**

Реализуйте функцию grep, принимающую на вход два параметра: подстроку для сопоставления и шаблон в формате glob, по которому будет происходить поиск.

Функция должна вернуть список всех строк файлов, в которых содержится подстрока. Поиск должен производиться по всем файлам переданного шаблона. Поиск не должен учитывать файлы в поддиректориях.

len(grep('test', './*'))  # 3
Подсказки
glob — модуль для работы с путями в формате glob
isdir - функция модуля os для проверки того, что путь является директорией


**b_NoSQL**

В этом испытании вам предстоит реализовать простой интерфейс NoSQL базы данных, основанной на текстовом файле. Функция get_() принимает на вход путь к файлу и ключ (любая строка) и возвращает значение по этому ключу. Если значение отсутствует, то возвращается None. Фунция set_() принимает также путь к файлу, ключ и значение (любая строка), и записывает по ключу значение в базу.

Размеры ключа и значений заданы константами KEY_LEN и VALUE_LEN.

db = open('./nosql.db', 'w')
path = db.name  # ./nosql.db
set_(path, 'key1', 'value1')
get_(path, 'key1')  # 'value1'
set_(path, 'key1', 'value2')
get_(path, 'key1')  # 'value2'
Подсказки
Для работы с файлом используйте смещения с помощью метода .seek()
Получить текущую позицию файлового указателя можно с помощью метода .tell()
Помните, что разные режимы открытия файлов (r, r+, w, w+, a, a+) ставят позицию указателя в разные места


**c_Removing_directories**

Реализуйте функцию rrmdir(), удаляющую директорию рекурсивно, то есть вместе со всем своим содержимым.

Для решения можете использовать функцию os.scandir() для получения итератора содержимого директории.

import os

list(os.scandir('.'))

# [<DirEntry 'Makefile'>,
#  <DirEntry 'tests'>,
#  <DirEntry '.pytest_cache'>,
#  <DirEntry 'pyproject.toml'>,
#  <DirEntry 'src'>]
И os.remove() для удаления файлового пути. Для удаления директорий используется os.rmdir()

import os

os.remove('./Makefile')
list(os.scandir('.'))

# [<DirEntry 'tests'>,
#  <DirEntry '.pytest_cache'>,
#  <DirEntry 'pyproject.toml'>,
#  <DirEntry 'src'>]
Подсказки
Не забывайте, что файловая система представляет из себя дерево.

https://ru.hexlet.io/courses/python-trees/lessons/manipulations/theory_unit


**f_transform_letter.py**

Реализуйте функцию transform(input_file, output_file, rules), которая принимает на вход путь до текстового файла, путь по которому нужно записать результат и обрабатывает текст согласно словарю rules следующим образом:

word_min_len - отфильтровывает слова меньше минимальной длины
censored_words - список слов, которые нужно удалить из текста
capital_letters - список букв, которые нужно привести к заглавным, если слово на них начинается
The Python language was not named after a long snake but after the British comedy show Monty Python Flying Circus
rules = {
    'word_min_len': 3,
    'censored_words': ['language', 'show'],
    'capital_letters': ['l', 'a'],
}
 
transform('python.txt', 'out.txt', rules=rules)
print(open('out.txt').read())
 
# => The Python was not named After Long snake but After the British comedy Monty Python Flying Circus
Если в результате преобразования получилась пустая строка, то ее не нужно записывать в выходной файл.

Подсказки
Используйте потоковую обработку
Каждое правило трансформера можно описать отдельной функцией и в итоговой собрать пайплайн обработки


**g_merge(file1, file2, out)**

В этом упражнении вам предстоит реализовать функцию merge(file1, file2, out), 
которая мержит (совмещает) два текстовых файла file1 и file2 и записывает результат по 
указаному пути out.

В случае, если в файлах не совпадают строки, то в нужно:

вывести строки первого файла, отметив их как >>>file1>>>
вывести разделитель =====
вывести строки второго, отметив их как <<<file2<<<
Например,

cat file1.txt
 
Hello from Hexlet
Python is awesome
Javascript is not about coffee
Use context managers
 
cat file2.txt
 
Hello from Hexlet
Python is a snake
Javascript is a language
Use context managers

merge('file1.txt', 'file2.txt', 'out.txt')

cat out.txt
 
Hello from Hexlet
>>>file1>>>
Python is awesome
Javascript is not about coffee
=====
Python is a snake
Javascript is a language
<<<file2<<<
Use context managers
 
Подсказки
Используйте контекстные менеджеры для управления открытием и закрытием файлов
Для упрощения предположим, что файлы имеют одинаковое количество строк




