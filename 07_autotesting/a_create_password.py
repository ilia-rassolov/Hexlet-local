import random



def generate_password(length=5, include_uppercase=False, include_digits=False, include_special=False):
    length = max(length, 5)
    lowercase_letters = string.ascii_lowercase
    capital_letters = string.ascii_uppercase
    digits = string.digits
    simbols = string.punctuation
    dict_elements_others = {capital_letters: include_uppercase,
                            digits: include_digits,
                            simbols: include_special}
    required_elements = [chars for chars, bool in dict_elements_others.items() if bool]
    all_elements = ''.join([lowercase_letters, capital_letters, digits, simbols])
    password = ''.join([random.choice(all_elements) for i in range(length)])

    for chars in required_elements:
        if not set(chars) & set(password):
            password = generate_password(length, include_uppercase, include_digits, include_special)
    return password


def test_generate_password_min_len():
    password = generate_password()
    assert len(password) == 5


# BEGIN (write your solution here)
import string


def test_generate_password_true():
    password = generate_password(8, include_uppercase=True, include_digits=True, include_special=True)
    test_include_uppercase = set(string.ascii_uppercase) & set(password)
    test_include_digits = set(string.digits) & set(password)
    test_include_special = set(string.punctuation) & set(password)

    assert len(test_include_uppercase) > 0
    assert len(test_include_digits) > 0
    assert len(test_include_special) > 0
    assert len(password) == 8
    assert ' ' not in password
# END