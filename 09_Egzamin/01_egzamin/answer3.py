def check_palindrome(sentence):
    if sentence.lower().replace(" ", "") == sentence.lower()[::-1].replace(" ", ""):
        return True
    else:
        return False


print(check_palindrome("Kobyła ma mały bok"))
print(check_palindrome("radar"))
print(check_palindrome("kajak"))
