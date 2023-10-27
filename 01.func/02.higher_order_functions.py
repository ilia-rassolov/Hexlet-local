

def get_first_name(full_name: str) -> str:

    name = ''
    i = 0
    while full_name[i] != '_':
        name += full_name[i]
        i += 1
    return name


def sort_by(func, users):

    copy_of_users = users.copy()
    copy_of_users.sort(key=func)
    print(copy_of_users)
    return copy_of_users


users = ["Vader_Darth", "Luke_Skywalker", "Boba_Fett"]

sort_by(get_first_name, users)







