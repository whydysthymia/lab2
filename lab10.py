import json
def ex101():
    file = open('products.json')
    data = json.load(file)
    for product in data['products']:
        print("Название:", product['name'])
        print("Цена:", product['price'])
        print("Вес:", product['weight'])
        if product['available']:
            print("В наличии")
        else:
            print("Нет в наличии!")
        print()
"""ex101()"""
def ex102():

    file = open('products.json')
    data = json.load(file)


    name = input("Введите название продукта: ")
    price = float(input("Введите цену продукта: "))
    weight = input("Введите вес продукта: ")

    new_product = {
        "name": name,
        "price": price,
        "weight": weight
    }

    data["products"].append(new_product)

    file = open('products.json', 'w')
    json.dump(data, file, indent=4)
"""ex102()"""

def ex103():
    file = open('en-ru.txt')
    lines = file.readlines()
    dict = []
    for line in lines:
        words = line.strip().split(' - ')
        english_word = words[0]
        russian_translations = words[1]
        dict.append(russian_translations + " - " + english_word)
    file = open('ru-en.txt', 'w')
    for words in dict:
        file.write(words + "\n")
ex103()
