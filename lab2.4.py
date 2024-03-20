import sys

primaryColors = {"синий", "красный", "желтый"}
firstColor = input("Введите первый цвет:\t")
lowFirstColor = firstColor.lower()
if lowFirstColor not in primaryColors:
    print("Error")
    sys.exit(0)
secondColor = input("Введите второй цвет:\t")
lowSecondColor = secondColor.lower()
if lowSecondColor not in primaryColors:
    print("Error")
    sys.exit(0)
if lowFirstColor in primaryColors and lowSecondColor in primaryColors and lowFirstColor != lowSecondColor:
    if lowFirstColor == "синий" and lowSecondColor == "красный" or lowFirstColor == "красный" and lowSecondColor == "синий":
        print("Вторичный цвет: фиолетовый")
    if lowFirstColor == "желтый" and lowSecondColor == "красный" or lowFirstColor == "красный" and lowSecondColor == "желтый":
        print("Вторичный цвет: оранжевый")
    if lowFirstColor == "желтый" and lowSecondColor == "синий" or lowFirstColor == "синий" and lowSecondColor == "желтый":
        print("Вторичный цвет: зеленый")
