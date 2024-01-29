from PIL import Image


def negatif(image):
    largeur, hauteur = image.size
    img = Image.new("RGB", (largeur, hauteur), (0, 0, 0))
    for x in range(largeur):
        for y in range(hauteur):
            r, g, b = image.getpixel((x, y))
            img.putpixel((x, y), (255 - r, 255 - g, 255 - b))
    return img


def niveaux_gris(image):
    largeur, hauteur = image.size
    img = Image.new("RGB", (largeur, hauteur), (0, 0, 0))
    for x in range(largeur):
        for y in range(hauteur):
            r, g, b = image.getpixel((x, y))
            gris = (r + g + b) // 3
            img.putpixel((x, y), (gris, gris, gris))
    return img


def rotation90(image, sens_trigo):
    largeur, hauteur = image.size
    img = Image.new("RGB", (hauteur, largeur), (0, 0, 0))
    for x in range(largeur):
        for y in range(hauteur):
            r, g, b = image.getpixel((x, y))
            if sens_trigo:
                img.putpixel((hauteur - y - 1, x), (r, g, b))
            else:
                img.putpixel((y, largeur - x - 1), (r, g, b))
    return img


def contours(image, s):
    largeur, hauteur = image.size
    img = Image.new("RGB", (largeur, hauteur), (255, 255, 255))
    for x in range(largeur):
        for y in range(hauteur):
            r, g, b = image.getpixel((x, y))
            if x == 0 or x == largeur - 1 or y == 0 or y == hauteur - 1:
                img.putpixel((x, y), (r, g, b))
            else:
                r1, g1, b1 = image.getpixel((x - 1, y))
                r2, g2, b2 = image.getpixel((x + 1, y))
                r3, g3, b3 = image.getpixel((x, y - 1))
                r4, g4, b4 = image.getpixel((x, y + 1))
                if abs(r - r1) > s or abs(r - r2) > s or abs(r - r3) > s or abs(r - r4) > s:
                    img.putpixel((x, y), (0, 0, 0))
                else:
                    img.putpixel((x, y), (255, 255, 255))
    return img
