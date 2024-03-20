import sys

string = ""
while "stop" not in string:
    word = input("Введите слово:\t")
    if "stop" in word:
        print(string)
        sys.exit(0)
    string += str(word) + " "
