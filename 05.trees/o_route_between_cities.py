from c_Display_filter_collapse import map_tree

def make_flat(tree3, dictionary, parent=None):
    [node, branches] = tree3
    children = []
    dictionary[node] = (parent, children)
    for branch in branches:
        name = make_flat(branch, dictionary, parent=node)
        children.append(name)
        return node


# def build_itinerary(tree, start_city, finish_city):

    # def way_to_center(tree1, city):
        # path = []
        # def inner(tree2):
        #     # path.append(tree2[0])
        #     for item in tree2:
        #         if isinstance(item, str):
        #             path.append(item)
        #             if item == city:
        #                 break
        #             else:
        #                 path = []
        #
        #
        #         else:
        #             if len(item) == 1:
        #             inner(item)






tree4 = ['Moscow', [
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
print(map_tree(lambda node: node, [] if node == [_] else node), tree4)

flat = {}
print(make_flat(tree, flat))

# build_itinerary(tree, 'Dubna', 'Kostroma')
#     # ['Dubna', 'Tver', 'Moscow', 'Ivanovo', 'Kostroma']
#
# build_itinerary(tree, 'Borisovka', 'Kurchatov')
#     # ['Borisovka', 'Belgorod', 'Kursk', 'Kurchatov']