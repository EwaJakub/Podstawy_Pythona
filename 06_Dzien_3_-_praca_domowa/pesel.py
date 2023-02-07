def validate_pesel(checked_number):
    try:
        if len(checked_number) == 11 and isinstance(int(checked_number), int):
            i = 0
            summary = 0
            weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
            for number in checked_number[0:10]:
                summary += int(number) * weights[i]
                i += 1
            mod_value = summary % 10
            if 10 - mod_value == int(checked_number[-1]):
                return True
            else:
                return False
        else:
            return False
    except ValueError:
        return False


print(validate_pesel("93121960984"))
print(validate_pesel("931a1960b84"))
print(validate_pesel("9312145543460984"))
print(validate_pesel("63101800270"))
