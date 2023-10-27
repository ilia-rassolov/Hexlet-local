import math

def make(numer, denom):
    gcd = math.gcd(int(numer), int(denom))
    return {"numer": int(numer / gcd), "denom": int(denom / gcd)}

print(make(121, 132))

def get_numer(rational):
    return rational["numer"]

def get_denom(rational):
    return rational["denom"]

def add(rat1, rat2):
    numer = get_numer(rat1) * get_denom(rat2) + get_numer(rat2) * get_denom(rat1)
    denom = get_denom(rat1) * get_denom(rat2)
    return make(numer, denom)

print(add({'numer': 2.0, 'denom': 6.0}, {'numer': 3.0, 'denom': 12.0}))

def sub(rat1, rat2):
    numer = get_numer(rat1) * get_denom(rat2) - get_numer(rat2) * get_denom(rat1)
    denom = get_denom(rat1) * get_denom(rat2)
    return make(numer, denom)

print(sub({'numer': 2.0, 'denom': 6.0}, {'numer': 3.0, 'denom': 12.0}))


def to_str(rat):
    return f"{get_numer(rat)}/{get_denom(rat)}"