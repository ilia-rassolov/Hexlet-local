**00_capitalize.py**

my tests can be called with the command:

~/PycharmProjects/Hexlet-exerсise/venv/lib/module-2/test-course
"PYTHONPATH=package-func python3 tests/test_capitalize.py"


**01_tdd_fill.py**

В этом упражнении вам предстоит попрактиковаться в подходе «Разработка через тестирование». Вам нужно написать и тесты, и реализацию функции. Сначала напишите тесты и запуcтите тестирование. Тесты должны упасть. Затем напишите решение, которое будет проходить тесты.

tests/test_fill.py
Напишите тесты для функции fill(coll, value, begin, end), которая заполняет элементы списка переданным значением, начиная со старта и заканчивая конечной позицией (при этом не включая ее). Обратите внимание, что функция меняет исходный список. Функция работает только с положительными позициями.

Функция принимает следующие аргументы:

coll – список, элементы которого будут заполнены
value – значение, которым будут заполнены элементы списка
begin – стартовая позиция, по умолчанию равна нулю
end – конечная позиция, по умолчанию равна длине списка
Так функция выглядит в коде:

# Все вызовы нужно рассматривать, как независимые
coll =  [1, 2, 3, 4]
 
fill(coll, '*', 1, 3)
print(coll)  # => [1, '*', '*', 4]
 
fill(coll, '*')
print(coll)  # => ['*', '*', '*', '*']
 
fill(coll, '*', 4)
print(coll)  # => [1, 2, 3, 4]
 
fill(coll, '*', 0, 10)
print(coll)  # => ['*', '*', '*', '*']
src/solution.py
Реализуйте функцию fill(coll, value, begin, end), основываясь на описании и примерах ее работы.

Подсказки
Один из тестов уже написан в упражнении. Используйте его как образец при написании своих тестов.

