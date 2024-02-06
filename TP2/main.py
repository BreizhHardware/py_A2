from tp2 import *
from tp2_optionnel import *
from tp_steganographie import *
from sys import argv as args


def __main__():
    if len(args) == 2:
        if (args[1] == "tp2"):
            __tp2__()
        elif (args[1] == "tp2_optionnel"):
            __tp2_optionnel__()
        elif (args[1] == "tp_steganographie_text"):
            __tp_steganographie_text__()
        elif (args[1] == "tp_steganographie_image"):
            __tp_steganographie_image__()
        elif (args[1] == "tp_steganographie_hide"):
            __tp_steganographie_hide__()
        else:
            print("Usage: python3 main.py")
            return
    else:
        print("Usage: python3 main.py")
        return


def __tp2__():
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


def __tp2_optionnel__():
    lena = Image.open("lena.png")
    lena.show()
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


def __tp_steganographie_text__():
    print(getHiddenTextWithDelimiter(hiddenText1, "\0"))
    print(getHiddenTextWithDelimiter(hiddenText2, "\0"))
    print(getHiddenTextOfLength(hiddenText3, 4))
    print(getHiddenTextOfLength(hiddenText4, 16))


def __tp_steganographie_image__():
    hidden1 = getHiddenImage(hiddenImage1, 8, 1)
    hidden1.show()
    hidden2 = getHiddenImage(hiddenImage2, 8, 1)
    hidden2.show()
    hidden3 = getHiddenImage(hiddenImage3, 8, 2)
    hidden3.show()
    hidden4 = getHiddenImage(hiddenImage4, 16, 2)
    hidden4.show()

def __tp_steganographie_hide__():
    gladiusWithHiddenTextDelimiter = setHiddenTextWithDelimiter(gladius, "Vive Star Citizen!", "\0")
    gladiusWithHiddenTextDelimiter.show()
    gladuisDecodedDelimiter = getHiddenTextWithDelimiter(gladiusWithHiddenTextDelimiter, "\0")
    print(gladuisDecodedDelimiter)
    zeusWithHiddenTextLength = setHiddenTextOfLength(zeusMK2CL, "I Held the line !", 4)
    zeusWithHiddenTextLength.show()
    zeusDecodedLength = getHiddenTextOfLength(zeusWithHiddenTextLength, 4)
    print(zeusDecodedLength)


if __name__ == "__main__":
    __main__()
