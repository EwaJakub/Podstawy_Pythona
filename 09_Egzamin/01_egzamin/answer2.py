def name_sorter(names_list):
    male = []
    female = []
    for name in names_list:
        if name[-1] == 'a':
            female.append(name)
        else:
            male.append(name)
    names_dict = {
        'male': sorted(male),
        'female': sorted(female)
    }
    return names_dict

names = ["Andrzej", "Henryk", "Alicja", "Cezary", "Barbara"]
print(name_sorter(names))
