
def rgb2hex(r, g, b):

    def f(color):
        result = format(color, 'x')
        if len(result) == 1:
            return f"0{result}"
        return result

    return f"#{f(r)}{f(g)}{f(b)}"


print(rgb2hex(r=84, g=63, b=171))
print(rgb2hex(r=1, g=16, b=8))

def hex2rgb(string16: str) -> dict:

    result = {}

    result["r"] = int(string16[1:3], base=16)
    result['g'] = int(string16[3:5], base=16)
    result['b'] = int(string16[5:], base=16)

    return result

print(hex2rgb('#24ab00'))

# BEGIN
from textwrap import wrap


def hex2rgb(color):
    r, g, b = map(lambda channel: int(channel, 16), wrap(color[1:], 2))
    return {'r': r, 'g': g, 'b': b}

def rgb2hex(r=None, g=None, b=None):
    return f'#{r:02x}{g:02x}{b:02x}'
# END