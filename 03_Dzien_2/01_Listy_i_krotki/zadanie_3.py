def find_short_words(list):
    return [word for word in list if len(word) < 5]

l = find_short_words(['Litwo', 'ojczyzno', 'moja', 'ty', 'jesteś', 'jak', 'zdrowie'])

print(l)  # ['moja', 'ty', 'jak']
