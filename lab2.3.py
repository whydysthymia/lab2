def leapYear():
    year = int(input("Введите год:\n"))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f"Год {year} - високосный")
    else:
        print("Этот год не високосный")
leapYear()


