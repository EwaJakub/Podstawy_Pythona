def message(dictionary):
    try:
        return f'In {dictionary["movie"]}, {dictionary["name"]} is a {dictionary["role"]}.'
    except KeyError:
        return None

def message_2(dictionary):
    if "name" in dictionary and "role" in dictionary and "movie" in dictionary:
        # return "In {movie}, {name} is a {role}".format(**dictionary) # rozpakowujemy elementy słownika jak niżej
        return "In {movie}, {name} is a {role}.".format(name=dictionary["name"],
                                                       role=dictionary["role"],
                                                       movie=dictionary["movie"])
    return None

input_dict = {
    "name": "Han Solo",
    "role": "smuggler",
    "movie": "Star Wars"
}

input_dict_2 = {
    "name": "Bilbo Baggins",
    "role": "burglar"
}

print(message(input_dict))
print(message(input_dict_2))

print(message_2(input_dict))
print(message_2(input_dict_2))