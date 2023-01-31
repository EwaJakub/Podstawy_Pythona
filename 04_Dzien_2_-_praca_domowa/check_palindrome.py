def check_palindrome(word):
    return word.lower() == word[::-1].lower()

word_1 = "ala"
print(check_palindrome(word_1))
word_2 = "kot"
print(check_palindrome(word_2))
word_3 = "Ala"
print(check_palindrome(word_3))