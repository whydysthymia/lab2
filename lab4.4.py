def luckyNumber():
    number = input("Введите число: ")
    firstHalf = number[:len(number)//2]
    secondHalf = number[len(number)//2:]
    summa1 = 0
    summa2 = 0
    for i in range(len(firstHalf)):
        summa1 += int(firstHalf[i])
        summa2 += int(secondHalf[i])
    if summa1 == summa2:
        print(f"Билет с номером {number} - счастливый")
    else:
        print(f"Билет с номером {number} - не является счастливым")
luckyNumber()
