import random
import sys

number1 = int(random.random()*9)
number2 = int(random.random()*9)
answer = int(input(f"{number1} + {number2} = "))
errors = 0
while errors < 3:
    if answer != (number1+number2):
        errors += 1
        print("Ответ неверный")
        if errors == 3:
            sys.exit(0)
        answer = int(input(f"{number1} + {number2} = "))
    else:
        print("Правильно!")
        sys.exit(0)