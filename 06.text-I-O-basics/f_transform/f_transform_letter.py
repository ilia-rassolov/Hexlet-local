def transform(input_file, output_file, rules):
    def filter_min_len(list_words):
        return filter(lambda word: len(word) >= rules['word_min_len'], list_words)

    def delete_censored_words(list_words):
        return filter(lambda word: word not in rules['censored_words'], list_words)

    def replace_capital_letter(word):
        if word[0] in rules['capital_letters']:
            return word[0].upper() + word[1:]
        return word
    in_file = open(input_file)
    out_file = open(output_file, "w")
    for line in in_file:
        # data = in_file.readline()
        # print(data, ' - data')
        print(line, ' - line')
        words_list = line.split()
        print(words_list, ' - words_list')
        out_list = list(map(replace_capital_letter, delete_censored_words(filter_min_len(words_list))))
        print(out_list, ' - out_list')
        if out_list:
            out_file.write(' '.join(out_list) + '\n')
    in_file.close()
    out_file.close()


rules1 = {
    'capital_letters': ['n', 'c'], 'censored_words': ['better', 'pass'], 'word_min_len': 3
}
transform('python.txt', 'f_transform/out.txt', rules1)
print(open('out.txt').read())
