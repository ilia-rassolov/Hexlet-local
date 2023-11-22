**a_make_flatten**

Реализуйте функцию flatten(), которая делает плоским вложенный список.

from solution import flatten
flatten([])  # []
flatten([2, [3, 5], [[4, 3], 2]])  # [2, 3, 5, 4, 3, 2]


**b_JSON stringify**

Реализуйте функцию stringify(), похожую на JSON.stringify(), но со следующими отличиями:

ключи и строковые значения должны быть без кавычек;
строчка (линия) в строке заканчивается самим значением, без запятой.
Синтаксис:

stringify(value[, replacer[, spaces_count]])
Параметры:

value
Значение, преобразуемое в строку.
replacer, необязательный
Строка – отступ для ключа; Значение по умолчанию – один пробел.
spacesCount, необязательный
Число – количество повторов отступа ключа. Значение по умолчанию – 1.
from solution import stringify

stringify('hello')  # значение приведено к строке, но не имеет кавычек
# hello
stringify(True)
# True
stringify(5)
# 5

data = {"hello": "world", "is": True, "nested": {"count": 5}}
stringify(data)  # то же самое что stringify(data, ' ', 1)
# {
#  hello: world
#  is: True
#  nested: {
#   count: 5
#  }
# }

stringify(data, '|-', 2)  # символ, переданный вторым аргументом повторяется столько раз, сколько указано третьим аргументом
# {
# |-|-hello: world
# |-|-is: True
# |-|-nested: {
# |-|-|-|-count: 5
# |-|-}
# }
Подсказки
чтобы лучше понять как работает JSON.stringify(), запускайте его с разными данными и параметрами в консоли браузера.
проверки в тестах идут от простого к сложному:

проверка на примитивных типах;
проверка на "плоских" данных;
проверка на "вложенных" данных.
реализуйте функцию так же пошагово, проверяя, что изменения для сложных кейсов не сломали более простые;

документация по JSON.stringify на MDN. https://developer.mozilla.org/ru/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify


**c_Display_filter_collapse**

В курсе Python: Функции мы проходили три основные функции высшего порядка по работе с коллекциями: map, filter и reduce.

В этом испытании вам предстоит написать собственную реализацию этих функций, только работать они будут с файловыми деревьями.

map_tree принимает на вход функцию-обработчик и дерево, а возвращает отображенное дерево.

filter_tree принимает в качестве параметров предикат и дерево, а возвращает отфильтрованное дерево по предикату.

reduce_tree кроме основных параметров (функция-обработчик и дерево) принимает также начальное значение аккумулятора.

from hexlet import fs

tree = fs.mkdir('/', [
  fs.mkdir('src', [
    fs.mkfile('solution.py', meta={'size': 12})
  ]),
])
Приводим имена всех директорий и файлов к верхнему регистру:

import copy

def to_upper(node):
    name = fs.get_name(node)
    new_meta = copy.deepcopy(fs.get_meta(node))
    if fs.is_file(node):
      return fs.mkfile(name.upper(), new_meta)
    return fs.mkdir(name.upper(), fs.get_children(node), new_meta)

map_tree(to_upper, tree)
# {'name': '/',
#  'children': [{'name': 'SRC',
#    'children': [{'name': 'SOLUTION.PY', 'meta': {'size': 12}, 'type': 'file'}],
#    'meta': {},
#    'type': 'directory'}],
#  'meta': {},
#  'type': 'directory'}
Отфильтровываем директории:

filter_tree(is_directory, tree)
# {'name': '/',
#  'children': [{'name': 'src',
#    'children': [],
#    'meta': {},
#    'type': 'directory'}],
#  'meta': {},
#  'type': 'directory'}
Подсчитываем количество узлов в дереве:

reduce_tree(lambda _, acc: acc + 1, tree, 0)
# 3
Подсказки
Документация python-immutable-fs-trees https://github.com/hexlet-components/python-immutable-fs-trees
Манипуляции с виртуальной файловой системой 


**d_Dependency_tracking**

Управление зависимостями - это очень важная задача при разработке программного обеспечения. Обычно в приложениях 
задействовано множество сторонних компонентов, которые, в свою очередь, тоже могут полагаться на сторонние компоненты. 
Одной из задач менеджера зависимостей является подключение зависимостей в правильном порядке. Библиотеки, от которых 
зависят другие, должны подключаться раньше. Определение этой последовательности сводится к задаче сортировки графа.

solution.py
Реализуйте функцию sort_deps(), которая принимает на вход словарь зависимостей и возвращает список отсортированных узлов.

deps = {
  'mongo': [],
  'tzinfo': ['thread_safe'],
  'uglifier': ['execjs'],
  'execjs': ['thread_safe', 'json'],
  'redis': [],
}

print(sort_deps(deps1))
# => ['mongo', 'thread_safe', 'tzinfo', 'json', 'execjs', 'uglifier', 'redis']
Независимые библиотеки и цепочки библиотек должны быть в порядке, соответствующему порядку элементов в графе зависимостей.

Подсказки
Об алгоритме: топологическая сортировка 
https://ru.wikipedia.org/wiki/%D0%A2%D0%BE%D0%BF%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D1%81%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0


**e_List_as_a_dictionary**

src/solution.py
Реализуйте функцию convert(), которая принимает на вход список определённой структуры и возвращает словарь, полученный из этого списка.

Список устроен таким образом, что с помощью него можно представлять словари. Каждый элемент списка — кортеж из двух элементов, где первый элемент — ключ, а второй — значение. Значение тоже может быть списком. Любой список внутри исходного списка всегда рассматривается как данные, которые нужно конвертировать в словарь.

from solution import convert
convert([])
# {}
convert([('key2', 'value2'), ('key', 'value')])
# {'key2': 'value2', 'key': 'value'}
convert([
  ('key', [('key2', 'anotherValue')]),
  ('key2', 'value2')
])
# {'key': {'key2': 'anotherValue'}, 'key2': 'value2'}
Подсказки
Работа с иерархическими структурами данных https://www.youtube.com/watch?v=95_U0FfM26Q


**f_remove_first_level**

В этом задании под деревом понимается любой список элементов, которые в свою очередь могут быть также деревьями или списками. Например:

[
  3, # Лист
  [5, 3], # Узел
  [[2]] # Узел
]
Больше примеров вы можете найти в тестах.

solution.py
Реализуйте функцию remove_first_level(). Она должна принимать на вход дерево и возвращать новое дерево, элементами которого являются потомки вложенных узлов:

from solution import remove_first_level
 
tree1 = [[5], 1, [3, 4]]
remove_first_level(tree1)  # [5, 3, 4]
tree2 = [1, 2, [3, 5], [[4, 3], 2]]
remove_first_level(tree2)  # [3, 5, [4, 3], 2]
Подсказки
Подключенный в модуле пакет itertools можно использовать, но это необязательно

**g_generate_tree**

Реализуйте функцию generate, которая создает такую файловую структуру:

# Обратите внимание на метаданные ниже
 
python-package  # Директория (метаданные: {'hidden': True})
├── Makefile  # Файл
├── README.md  # Файл
├── dist  # Пустая директория
├── tests  # Директория
│   └── test_solution.py  # Файл
├── pyproject.toml  # Файл
└── .venv  # Директория (метаданные: {'owner': 'root', 'hidden': False})
    └── lib  # Директория
        └── python3.6  # Директория
            └── site-packages  # Директория
                └── hexlet-python-package.egg-link  # Файл
from hexlet.fs import mkdir, mkfile


**h_compress_size_images**

Реализуйте функцию compress_images(). Она должна принимать на вход директорию, находить внутри нее картинки и 
уменьшать свойство size в их метаданных в два раза. Функция должна вернуть обновленную директорию со сжатыми картинками 
и всеми остальными данными, которые были внутри этой директории.

Картинками считаются все файлы, заканчивающиеся на .jpg:

from hexlet.fs import mkdir, mkfile
from solution import compress_images
tree = mkdir(
    'my documents',
    [
        mkfile('avatar.jpg', {'size': 100}),
        mkfile('photo.jpg', {'size': 150}),
    ],
    {'hide': False}
)
compress_images(tree)
# {
#     'name': 'my documents',
#     'type': 'directory',
#     'children': [
#         {'name': 'avatar.jpg', 'meta': {'size': 50}, 'type': 'file'},
#         {'name': 'photo.jpg', 'meta': {'size': 75}, 'type': 'file'},
#     ],
#     'meta': {'hide': False},
# }

import copy

from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile



**i_change_owner**

Допустим, мы хотим реализовать функцию, которая меняет владельца для всего дерева, то есть всех директорий и файлов.

Для этого нам придется соединить две вещи:

Рекурсию, разобранную выше
Код обновления узлов из прошлого урока

import copy
from hexlet import fs


**j_change_name_file_tree**

Реализуйте функцию downcase_file_names(). Она должна принимать на вход директорию (объект-дерево) и приводить имена всех файлов к нижнему регистру, причем в корневой директории и во всех вложенных. Функция должна возвращать результат в виде обработанной директории:

from hexlet.fs import mkdir, mkfile, get_children, get_name
from solution import downcase_file_names
tree = mkdir('/', [
    mkdir('eTc', [
        mkdir('NgiNx', [], {'size': 4000}),
        mkdir(
            'CONSUL',
            [mkfile('config.JSON', {'uid': 0})],
        ),
    ]),
    mkfile('HOSTS'),
])
new_tree = downcase_file_names(tree)
new_file = get_children(new_tree)[1]
get_name(new_file)  # hosts

import copy

from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile


**k_get_nodes_count**

Рассмотрим агрегацию с использованием рекурсивного процесса на примере подсчета общего количества узлов в дереве. Другими словами, попробуем выяснить, сколько всего файлов и директорий содержится в нашем файловом дереве:

from hexlet import fs

tree = fs.mkdir('/', [
    fs.mkdir('etc', [
        fs.mkfile('bashrc'),
        fs.mkfile('consul.cfg'),
    ]),
    fs.mkfile('hexletrc'),
    fs.mkdir('bin', [
        fs.mkfile('ls'),
        fs.mkfile('cat'),
    ]),
])


**l_hidden_files_counter**

Реализуйте функцию get_hidden_files_count(), которая считает количество скрытых файлов в директории и всех поддиректориях. В Linux-системах скрытыми считаются все файлы, название которых начинается с точки:

from hexlet.fs import mkdir, mkfile
from solution import get_hidden_files_count
 
tree = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('.nginx.conf', {'size': 800}),
        ]),
        mkdir('.consul', [
            mkfile('.config.json', {'size': 1200}),
            mkfile('data', {'size': 8200}),
            mkfile('raft', {'size': 80}),
        ]),
    ]),
    mkfile('.hosts', {'size': 3500}),
    mkfile('resolve', {'size': 1000}),
])
get_hidden_files_count(tree)  # 3

from hexlet.fs import get_children, get_name, is_file


**m_make_du**

В Linux, MacOS и многих операционных системах существует утилита du. Она умеет подсчитывать, сколько места занимают указанные файлы и директории. Например, так:

 tmp$ du -sh *
 97k    .venv
  0B    com.docker.vmnetd.socket
 10M    credo
4.0K    debug.mjs
  0B    filesystemui.socket
4.0K    index.py
 88K    poetry-lock.json
 22M    taxdome
Перед решением этого задания обязательно попрактикуйтесь с этой утилитой в терминале, посмотрите ее опции через man du. Экспериментировать нужно в локально установленной операционной системе.

solution.py
Реализуйте функцию du. Она должна принимать на вход директорию и возвращать:

Список всех директорий и файлов, которые вложены в указанную директорию на один уровень
Размер всей директории, который складывается из сумм всех размеров файлов, находящихся внутри во всех подпапках
Так это выглядит в коде:

from hexlet.fs import mkdir, mkfile
from solution import du
tree = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('nginx.conf', {'size': 800}),
        ]),
        mkdir('consul', [
            mkfile('.config.json', {'size': 1200}),
            mkfile('data', {'size': 8200}),
            mkfile('raft', {'size': 80}),
        ]),
    ]),
    mkfile('hosts', {'size': 3500}),
    mkfile('resolve', {'size': 1000}),
])
du(tree)  # [('etc', 10280), ('hosts', 3500), ('resolve', 1000)]
Примечания
Размер файла задается в метаданных, при этом сами папки размера не имеют
В структуре результирующего cписка каждый элемент является кортежем с двумя значениями — именем директории и размером файлов внутри
Результат отсортирован по размеру в обратном порядке — сверху тяжелые, снизу легкие
Подсказки
sort

from hexlet.fs import get_children, get_meta, get_name, is_file


**n_find_files_in_tree**

Реализуйте функцию find_files_by_name(). Она должна принимать на вход файловое дерево и подстроку, а затем возвращать список файлов, имена которых содержат эту подстроку. Функция должна вернуть полные пути файлам:

from hexlet.fs import mkdir, mkfile
from solution import find_files_by_name
tree = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('nginx.conf', {'size': 800}),
        ]),
        mkdir('consul', [
            mkfile('config.json'),
            mkfile('data'),
            mkfile('raft'),
        ]),
    ]),
    mkfile('hosts', {'size': 3500}),
    mkfile('resolve', {'size': 1000}),
])
find_files_by_name(tree, 'co')
# ['/etc/nginx/nginx.conf', '/etc/consul/config.json']
Подсказки
Для реализации этой логики вам понадобится аккумулятор, в котором будет храниться путь от корня до текущего узла. При проваливании внутрь директорий к нему добавляется имя текущей директории. В остальном логика работы идентична примеру из теории
Переменную с путем от корня до текущего узла можно назвать ancestry
Для построения путей используйте функцию os.path.join()

import os

from hexlet.fs import flatten, get_children, get_name, is_file


**o_route_between_cities**

Реализуйте функцию build_itinerary(), которая выстраивает маршрут между городами.

Функция принимает на вход 3 аргумента:

дерево городов
город старта
город окончания маршрута
и возвращает список городов, выстроенных в том же порядке, в котором они находятся на пути следования по маршруту.

tree = ['Moscow', [
    ['Smolensk'],
    ['Yaroslavl'],
    ['Voronezh', [
        ['Liski'],
        ['Boguchar'],
        ['Kursk', [
            ['Belgorod', [
                ['Borisovka'],
            ]],
            ['Kurchatov'],
        ]],
    ]],
    ['Ivanovo', [
        ['Kostroma'], ['Kineshma'],
    ]],
    ['Vladimir'],
    ['Tver', [
        ['Klin'], ['Dubna'], ['Rzhev'],
    ]],
]]

build_itinerary(tree, 'Dubna', 'Kostroma')
# ['Dubna', 'Tver', 'Moscow', 'Ivanovo', 'Kostroma']

build_itinerary(tree, 'Borisovka', 'Kurchatov')
# ['Borisovka', 'Belgorod', 'Kursk', 'Kurchatov']
Подсказки
Работа с иерархическими структурами данных
Используйте возможности модулей itertools и functools из стандартной библиотеки


