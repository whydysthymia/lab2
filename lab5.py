import random
import re

def ex51():
    spisok = [random.randint(1, 10) for x in range(0, 5)]
    user_num = input()
    print(spisok)
    if int(user_num) in spisok:
        print(spisok)
        print(user_num)
        print("Verno")
    else:
        print("chisla net")


'''ex51()'''

def ex52():

    newOne = []
    spisok = [random.randint(1, 10) for x in range(0, 50)]
    for i in range(len(spisok)):
        if (spisok[i] in spisok[i+1:]) and spisok[i] not in newOne:
            newOne.append(spisok[i])
    print(newOne)
    print(spisok)
'''ex52()'''

def ex53():

    week = ("Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье")
    weekends = int(input("Введите количество выходных\t"))
    print("Ваши выходные дни - ", list(week[-weekends:]))
    week = list(week[:-weekends])
    print("Ваши рабочие дни - ", week)


'''ex53()'''

def ex54():
    myStudents = ["Семенов", "Рогозный", "Манылов", "Ярмолаш", "Федосеева", "Абдурахимов", "Зарецкая", "Болтрукевич", "Бутузова", "Печинская"]
    otherStudents = ["Петров", "Иванов", "Добриков", "Иванов", "Силантьева", "Иванов", "Соменков", "Иванов", "Сорокина", "Иванов"]

    team = []
    indexI = []
    indexJ = []
    while len(team) != 5:
        i = random.randint(0,9)
        if (myStudents[i] not in team) or ((myStudents[i] in team) and (i not in indexI)):
            indexI.append(i)
            team.append(myStudents[i])
    while len(team) != 10:
        j = random.randint(0,9)
        if (otherStudents[j] not in team) or ((otherStudents[j] in team) and (j not in indexJ)):
            indexJ.append(j)
            team.append(otherStudents[j])

    team = tuple(sorted(team))
    print(myStudents, "\n", otherStudents)
    print(team, "\n", len(team))
    if "Иванов" in team:
        print(len(re.findall("Иванов", str(team))))
ex54()
