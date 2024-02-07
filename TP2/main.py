from tp2 import *
from tp2_optionnel import *
from tp_steganographie import *
from sys import argv as args


def __main__():
    if len(args) == 2:
        if args[1] == "tp2":
            __tp2__()
        elif args[1] == "tp2_optionnel":
            __tp2_optionnel__()
        elif args[1] == "tp_steganographie_text":
            __tp_steganographie_text__()
        elif args[1] == "tp_steganographie_image":
            __tp_steganographie_image__()
        elif args[1] == "tp_steganographie_hide":
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
    hiddenText1 = Image.open("hiddenText1.png")
    hiddenText2 = Image.open("hiddenText2.png")
    hiddenText3 = Image.open("hiddenText3.png")
    hiddenText4 = Image.open("hiddenText4.png")
    decrypt_felix = Image.open("DecryptFelix.png")
    textImage = Image.open("textImage.png")
    print(get_hidden_text_with_delimiter(hiddenText1, "\0"))
    print(get_hidden_text_with_delimiter(hiddenText2, "\0"))
    print(get_hidden_text_of_length(hiddenText3, 4))
    print(get_hidden_text_of_length(hiddenText4, 16))
    print(get_hidden_text_with_delimiter(decrypt_felix, "\0"))
    print(get_hidden_text_with_delimiter(textImage, "\0"))


def __tp_steganographie_image__():
    hiddenImage1 = Image.open("hiddenImage1.png")
    hiddenImage2 = Image.open("hiddenImage2.png")
    hiddenImage3 = Image.open("hiddenImage3.png")
    hiddenImage4 = Image.open("hiddenImage4.png")
    hidden1 = get_hidden_image(hiddenImage1, 8)
    hidden1.show()
    hidden2 = get_hidden_image(hiddenImage2, 8)
    hidden2.show()
    hidden3 = get_hidden_image(hiddenImage3, 8, 2)
    hidden3.show()
    hidden4 = get_hidden_image(hiddenImage4, 16, 2)
    hidden4.show()


def __tp_steganographie_hide__():
    gladius = Image.open("Gladius.png")
    zeusMK2CL = Image.open("Zeus-MKII-CL.png")
    small = Image.open("small.png")
    zeusMK2CL_with_hidden_text = set_hidden_text_with_delimiter(small, "Flop, nigger !", "\0")
    zeusMK2CL_with_hidden_text.save("OuvreMoi.png")
    '''
    gladius_with_hidden_text_delimiter = set_hidden_text_with_delimiter(gladius, "Vive Star Citizen!", "\0")
    gladius_decoded_delimiter = get_hidden_text_with_delimiter(gladius_with_hidden_text_delimiter, "\0")
    print(gladius_decoded_delimiter)
    zeus_with_hidden_text_length = set_hidden_text_of_length(zeusMK2CL, "I Held the line !", 4)
    zeus_decoded_length = get_hidden_text_of_length(zeus_with_hidden_text_length, 4)
    print(zeus_decoded_length)
    '''
    gladius_with_hidden_image = set_hidden_image(gladius, small, 8)
    print(type(gladius_with_hidden_image))
    gladius_with_hidden_image.show()
    '''
    gladius_decoded_image = get_hidden_image(gladius_with_hidden_image, 8)
    print(type(gladius_decoded_image))
    gladius_decoded_image.show()
    '''


if __name__ == "__main__":
    __main__()
