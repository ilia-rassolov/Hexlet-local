def number_of_unique_letters(string):

    set_letters_lower = {x.lower() for x in string if x.isalpha()}
    print(set_letters_lower)
    print(len(set_letters_lower))


    return len(set_letters_lower)



st = "a,b_C  \nd"
number_of_unique_letters(st)
