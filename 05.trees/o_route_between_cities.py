def make_dict(tree_d):     # представление дерева словарём связей - {узел: (предок, [потомки])...}
    dictionary = {}

    def inner(tree_d, parent=None):
        if len(tree_d) == 1:
            dictionary[tree_d[0]] = (parent, [])
        else:
            [node, branches] = tree_d
            children = [branch[0] for branch in branches]
            dictionary[node] = (parent, children)
            for branch in branches:
                inner(branch, node)
    inner(tree_d)
    return dictionary


def make_path_city_moscow(city, tree_m):     # создать путь узел - корень (от города до Москвы)
    dictionary = make_dict(tree_m)
    path = [city]
    parent = dictionary[city][0]
    while parent:
        path.append(parent)
        parent = dictionary[path[-1]][0]
    return path


def build_itinerary(tree, start_city, finish_city):
    path_start_city_moscow = make_path_city_moscow(start_city, tree)
    path_moscow_finish_city = make_path_city_moscow(finish_city, tree)[::-1]
    result = []
    for city in path_start_city_moscow:
        if city not in path_moscow_finish_city:
            result.append(city)
        else:
            result.append(city)
            break
    for city in path_moscow_finish_city:
        if city not in path_start_city_moscow:
            result.append(city)
    return result


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

print(build_itinerary(tree, 'Borisovka', 'Kurchatov'))
#     # ['Dubna', 'Tver', 'Moscow', 'Ivanovo', 'Kostroma']
#
# build_itinerary(tree, 'Borisovka', 'Kurchatov')
#     # ['Borisovka', 'Belgorod', 'Kursk', 'Kurchatov']
