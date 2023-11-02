from functools import reduce


def sort_deps(deps):
    result = []
    current_deps = {}
    k = current_deps.keys()
    values = deps.values()
    items = deps.items()
    keys = deps.keys()
    print(keys)
    for key, value in items:
        if not value:
            result.append(key)
        else:
            for v in value:
                if v not in keys:
                    if v not in result:
                        result.append(v)
                        result.append(key)
                        # if key in k:
                        #     result.append(current_deps[key])
                else:
                    current_deps[v] = key
                    print(current_deps)
    return result


deps1 = {
    'mongo': [],
    'tzinfo': ['thread_safe'],
    'uglifier': ['execjs'],
    'execjs': ['thread_safe', 'json'],
    'redis': [],
}

print(sort_deps(deps1))
# => ['mongo', 'thread_safe', 'tzinfo', 'json', 'execjs', 'uglifier', 'redis']
# expected2 = ['htmlentities', 'predicated', 'sexp_processor', 'wrong', 'nokogiri', 'xpath', 'virtus']