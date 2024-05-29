from PIL import Image, ImageFilter
import os
import csv
def ex91():
    infolder = "/Users/ivanmanylov/Desktop/alg/91/"
    outfolder = "/Users/ivanmanylov/Desktop/alg/91/filtered/"
    if not os.path.exists(outfolder):
        os.makedirs(outfolder)
    for i in os.listdir(infolder):
        if i.endswith(".jpeg"):
            image = Image.open(infolder + i)
            filter = image.filter(ImageFilter.CONTOUR)
            filter.save(outfolder + "filtered_" + i)
"""ex91()"""

def ex93():
    file = open('данные.csv')
    data = list(csv.reader(file))
    data.pop(0)
    print("Нужно купить: ")
    for i in data:
        print(f"{i[0]} - {i[1]} шт. за {i[2]} руб")
    print(f"Итоговая цена: {sum([int(i[1]) * int(i[2]) for i in data])} руб.")
ex93()
