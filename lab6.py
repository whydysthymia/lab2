def ex61():
    slovar = {"USA": "WASHINGTONE", "RUSSIA": "MOSCOW", "FRANCE": "PARIS", "ITALY": "ROME"}

    for key, value in slovar.items():
        print("{}: {}".format(key, value))
    country = input("Введите название страны: ").upper()
    print("Столица", country, "-", slovar.get(country))
    sorted_slovar = sorted(slovar.items(), key=lambda f: f[1])
    print(sorted_slovar)
    sorted_slovar = dict(sorted_slovar)
    for key, value in sorted_slovar.items():
        print("{}: {}".format(key, value))
'''ex61()'''

def ex62():
    alphabet = {
    'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
    'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
    'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
    'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
    'Ш': 8, 'Э': 8, 'Ю': 8,
    'Щ': 10, 'Ъ': 10, 'Ф': 10
    }
    value = 0
    word = input("Введите слово: ")
    word = word.upper()
    splitted = list(word)
    for i in range(len(splitted)):
        if splitted[i] in alphabet:
            value += alphabet.get(splitted[i])
    print(value)
"""ex62()"""

def ex63():
    students_languages = {
        'Иванов': ['английский', 'французский', 'немецкий'],
        'Петров': ['английский', 'китайский'],
        'Сидоров': ['испанский', 'итальянский'],
        'Козлов': ['китайский', 'японский'],
        'Смирнов': ['французский'],
        'Алексеев': ['английский', 'немецкий', 'китайский']
    }
    allLang = set()
    for languages in students_languages.values():
        allLang.update(languages)
    print(len(allLang))
    print(sorted(allLang))
    print(students_languages.get('китайский'))
    chinese_speakers = [key for key, languages in students_languages.items() if 'китайский' in languages]
    print(chinese_speakers)
ex63()

