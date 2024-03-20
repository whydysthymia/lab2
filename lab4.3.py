def magic():
    day = ""
    month = ""
    year = ""
    date = input("Введите дату: ")
    day += date[0:2]
    month += date[3:5]
    year = year + date[-2] + date[-1]
    if int(day)*int(month) == int(year):
        return True
    else:
        return False
print(magic())
