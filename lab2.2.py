seatNum = int(input("Введите номер своего места:\t"))
if seatNum >= 1 and seatNum <= 36 and seatNum % 2 == 0 :
    print("Верхнее в купе")
if seatNum >= 1 and seatNum <= 36 and seatNum % 2 != 0:
    print("Нижнее в купе")
if seatNum >= 37 and seatNum <= 54 and seatNum % 2 == 0:
    print("Верхнее сбоку")
if seatNum >= 37 and seatNum <= 54 and seatNum % 2 != 0:
    print("Нижнее сбоку")
