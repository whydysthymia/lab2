from PIL import Image
def ex71():
    image_path = '/Users/ivanmanylov/Desktop/image.jpg'
    image = Image.open(image_path)
    width, height = image.size
    print("Размер изображения: {}x{}".format(width, height))
    print("Формат изображения:", (image.format))
    print("Цветовая модель:", (image.mode))
    image.show()
ex71()
