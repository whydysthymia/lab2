import sys

string = ""
while "stop" not in string:
    word = input("Введите слово:\n")
    string += str(word)
    if "stop" in string:
        sys.exit(0)
    if "Ф" in word or "ф" in word:
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")

