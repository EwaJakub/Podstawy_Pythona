from datetime import date
from calendar import month_name

# solution 1
def format_date(day, month, year):
    '''
    date(year, month, day) returns the date
    for year (1970–…), month (1–12), day (1–31),
    ValueError if any of parametres is out of range
    for exact year and month
    '''
    try:
        # print(str(day) + " " + month_name[month] + " " + str(year))
        return date(year, month, day).strftime("%d %B %Y")
    except ValueError:
        return None

# solution 2
def format_date2(day, month, year):
    month_list_31 = [1, 3, 5, 7, 8, 10, 12]
    month_list_30 = [4, 6, 9, 11]
    month_list_28 = [2]
    if month in month_list_31 and day <= 31 \
            or month in month_list_30 and day <= 30 \
            or month in month_list_28 and day <= 28:
        if day > 0:
            result = (str(day), month_name[month], str(year))
            return " ".join(result)
    else:
        return None


print(format_date(26, 2, 2037))
print(format_date2(26, 2, 2037))