from PIL import Image


def creer_drapeau_francais():
    img = Image.new("RGB", (450, 300), (255, 255, 255))
    for x in range(150):
        for y in range(300):
            img.putpixel((x, y), (0, 0, 255))
    for x in range(300, 450):
        for y in range(300):
            img.putpixel((x, y), (255, 0, 0))
    return img


def creer_degrade_vertical():
    img = Image.new("RGB", (300, 300), (0, 0, 0))
    for x in range(300):
        for y in range(300):
            img.putpixel((y, x), (x, x, x))
    return img


def miroir(image):
    largeur, hauteur = image.size
    img = Image.new("RGB", (largeur, hauteur), (0, 0, 0))
    for x in range(largeur):
        for y in range(hauteur):
            r, g, b = image.getpixel((x, y))
            img.putpixel((largeur - x - 1, y), (r, g, b))
    return img