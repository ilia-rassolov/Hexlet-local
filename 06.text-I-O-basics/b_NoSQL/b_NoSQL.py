

def get_(file, key):
    if len(key) != KEY_LEN:
        return None
    data = open(file)     # вид БД принял как строку "key0: value0, key1: value1, ... "
    text = data.read()
    print('text = ', text)
    if key not in text:
        return None
    # position = data.tell()  # не смог применить tell(), курсор после read() уходит в конец
    position = text.index(key)
    print('position = ', position)
    print('VALUE = V')
    return text[position + 2 + KEY_LEN: position + 2 + KEY_LEN + VALUE_LEN]


def set_(file, key, value):
    if len(key) != KEY_LEN or len(value) != VALUE_LEN:
        return None
    data = open(file)
    text = data.read()
    print('text = ', text)
    if key not in text:
        return None
    position_key = text.index(key)
    print('pos_key = ', position_key)
    # position_now = data.tell()
    # print('pos_now = ', position_now)
    data = open(file, "w")
    data.seek(position_key + 2 + KEY_LEN)
    print('text = ', text)
    data.write(value)    # почему-то всё меняет на null и удаляет, кроме value
    data.close()


KEY_LEN = 4
VALUE_LEN = 6

print(get_("nosql.db", 'key3'))
print(set_("nosql.db", 'key6', 'valueX'))
