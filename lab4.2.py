def devision():
    try:
        denominator = float(input("Введите делитель: "))
        res = 100 / denominator
        print("Ответ: ", res)
    except ValueError:
        print("Не число!")
    except ZeroDivisionError:
        print("На 0 делить нельзя!")
devision()
        