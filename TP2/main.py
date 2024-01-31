from tp2 import *
from tp2_optionnel import *
from tp_steganographie import *


def __main__():
    '''x
    fond_bleu = Image.new("RGB", (450, 300), (0, 0, 255))
    fond_bleu.show()
    drapeau_fr = creer_drapeau_francais()
    drapeau_fr.show()
    degrade_vertical = creer_degrade_vertical()
    degrade_vertical.show()
    lena = Image.open("lena.png")
    lena.show()
    print(lena.size)
    r, g, b = lena.getpixel((0, 0))
    print(r, g, b)
    lena_miror = miroir(lena)
    lena_miror.show()
    lena_miror.save("lena_miror.png")
    lena_negatif = negatif(lena)
    lena_negatif.show()
    lena_niveaux_gris = niveaux_gris(lena)
    lena_niveaux_gris.show()
    lena_tournee = rotation90(lena, True)
    lena_tournee.show()
    lena_tournee = rotation90(lena, False)
    lena_tournee.show()
    lena_contours = contours(lena, 50)
    lena_contours.show()
    print(getHiddenTextWithDelimiter(hiddenText1, "\0"))
    print(getHiddenTextWithDelimiter(hiddenText2, "\0"))
    print(getHiddenTextOfLength(hiddenText3, 4))
    print(getHiddenTextOfLength(hiddenText4, 16))
    '''
    hidden1 = getHiddenImage(hiddenImage1, 8)
    hidden1.show()
    hidden2 = getHiddenImage(hiddenImage2, 8)
    hidden2.show()
    '''
    hidden3 = getHiddenImageInLastBits(hiddenImage3, 8, 2)
    hidden3.show()
    hidden4 = getHiddenImageInLastBits(hiddenImage4, 16, 2)
    hidden4.show()
    '''


if __name__ == "__main__":
    __main__()
