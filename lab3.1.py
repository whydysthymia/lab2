wordCount = input("Введите количество слов\t")
counter = 0
string = ""
while counter < int(wordCount):
    counter += 1
    word = input("Введите слово:\t")
    string += str(word) + " "
print(string)