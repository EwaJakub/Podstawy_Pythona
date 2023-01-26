def list_keys(d):
    keys = []
    for key in d:
        keys.append(key)
    return keys

def list_keys_2(d):
    return [key for key in d]


book = {
  "title": "Krzyżacy",
  "no_of_pages": 200,
  "characters": ["Jurand ze Spychowa",
          "Danusia",
          "Zbyszko z Bogdańca",
          "Jagienka"],
  "fun_to_read": True
}

print(list_keys(book))
print(list_keys_2(book))
