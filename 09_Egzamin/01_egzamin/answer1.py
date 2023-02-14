def shorten(sentence):
    sent_list = sentence.split()
    abbrev_list = [el[0] for el in sent_list]
    return ''.join(abbrev_list).upper()


shortened = shorten("Don't repeat yourself")
print(shortened)
shortened = shorten("Read the fine manual")
print(shortened)
shortened = shorten("All terrain armoured transport")
print(shortened)
