

def convert(complex_list):
    result = {}

    def walk(pair):
        (key, value) = pair
        if isinstance(value, list):
            value = convert(value)
        result[key] = value
    for item in complex_list:
        walk(item)
    return result


print(convert([
  ('key', [('key2', [('key4', 'anotherValue'), ('key5', 'anotherValue5')])]),
  ('key2', 'value2'),
('key3', 'value3')
])
)
