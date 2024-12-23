import string
import random

def generate_password(length=5, include_uppercase=True, include_digits=True, include_special=True):
    lowercase_letters = string.ascii_lowercase
    capital_letters = string.ascii_uppercase
    digits = string.digits
    simbols = string.punctuation
    dict_elements_others = {capital_letters: include_uppercase,
                            digits: include_digits,
                            simbols: include_special}
    lists_elements_others = [chars for chars, bool in dict_elements_others.items() if bool]
    print(lists_elements_others)

    all_elements_for_password = f"{''.join(lists_elements_others)}{lowercase_letters}"
    print(all_elements_for_password)

    password = ''.join([random.choice(all_elements_for_password) for i in range(length)])
    print(password)

    for chars in lists_elements_others:
        if not set(chars) & set(password):
            password = generate_password(length, include_uppercase, include_digits, include_special)
    return password


print(generate_password(6))