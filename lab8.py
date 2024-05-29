from PIL import Image, ImageFont, ImageDraw
def ex81():
    image = Image.open('/Users/ivanmanylov/Desktop/alg/otkr1.jpeg')
    area = (70, 400, 800, 1000)
    cropped = image.crop(area)
    cropped.save('/Users/ivanmanylov/Desktop/alg/' + "cropped_" + "otkr1.jpeg")
"""ex81()"""

def ex82():
    cards = {
        "Birthday": "/Users/ivanmanylov/Desktop/alg/otkr1.jpeg",
        "New Year": "/Users/ivanmanylov/Desktop/alg/otkr2.jpeg",
        "Valentine's Day": "/Users/ivanmanylov/Desktop/alg/otkr3.jpeg"
    }
    holiday = input("For which holiday do you need a card? ")
    if holiday in cards:
            card = Image.open(cards.get(holiday))
            card.show()
    else:
        print("No cards for this holiday")
"""ex82()"""

def ex83():
    cards = {
        "Birthday": "/Users/ivanmanylov/Desktop/alg/otkr1.jpeg",
        "New Year": "/Users/ivanmanylov/Desktop/alg/otkr2.jpeg",
        "Valentine's Day": "/Users/ivanmanylov/Desktop/alg/otkr3.jpeg"
    }
    holiday = input("For which holiday do you need a card? ")
    name = input("Name? ")
    if holiday in cards:
        card = Image.open(cards.get(holiday))
        draw_text = ImageDraw.Draw(card)
        font = ImageFont.truetype("Arial.ttf", 50)
        draw_text.text((100, 100), f'{name}, Congratulations!', font=font, fill='red', stroke_fill='red', stroke_width=3)
        card.save("/Users/ivanmanylov/Desktop/alg/" + "card.png")
    else:
        print("No cards for this holiday")
ex83()