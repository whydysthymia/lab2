from PIL import Image, ImageOps, ImageFilter

def ex71():
    image = Image.open('/Users/ivanmanylov/Desktop/image.jpg')
    width, height = image.size
    print("Размер изображения: {}x{}".format(width, height))
    print("Формат изображения:", (image.format))
    print("Цветовая модель:", (image.mode))
    image.show()
"""ex71()"""

def ex72():
    image = Image.open("/Users/ivanmanylov/Desktop/image.jpg")
    width, height = image.size
    small_image = image.resize((width // 3, height // 3))
    small_image.save("/Users/ivanmanylov/Desktop/alg/" + "smalLainux.jpeg")
    mirrored = ImageOps.mirror(image)
    mirrored.save("/Users/ivanmanylov/Desktop/alg/" + "mirroredLainux.jpeg")
    flipped = ImageOps.flip(mirrored)
    flipped.save("/Users/ivanmanylov/Desktop/alg/" + "flippedLainux.jpeg")
"""ex72()"""

def ex73():

    infolder = "/Users/ivanmanylov/Desktop/alg/"
    outfolder = "/Users/ivanmanylov/Desktop/alg/filtered/"
    images = ["1.jpeg", "2.jpeg", "3.jpeg", "4.jpeg", "5.jpeg"]

    for i in images:
        image = Image.open(infolder + i)
        filter = image.filter(ImageFilter.CONTOUR)
        filter.save(outfolder + "filtered_" + i)
"""ex73()"""

def ex74():
    image = Image.open('/Users/ivanmanylov/Desktop/image.jpg')
    waterMark = Image.open("/Users/ivanmanylov/Desktop/alg/4.jpeg")
    width, height = waterMark.size
    smallWaterMark = waterMark.resize((width // 5, height // 5))
    smallWaterMark.putalpha(40)
    newImage = Image.new('RGBA', image.size)
    newImage.paste(image)
    newImage.paste(smallWaterMark, (100, 200), mask=smallWaterMark)
    newImage.show()
ex74()