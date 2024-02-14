from sys import argv as args
from tp_fichier import *


def __main__():
    if len(args) == 2:
        if args[1] == "tp_fichier":
            __tp_fichier__()
        else:
            print("Usage: python3 main.py")
            return
    else:
        print("Usage: python3 main.py")
        return


def __tp_fichier__():
    nb_lignes = calculer_nb_lignes("lorem_ipsum.txt")
    print(nb_lignes)
    recopier_fichier("lorem_ipsum.txt", "lorem_ipsum_copie.txt")
    inverser_fichier("lorem_ipsum.txt", "lorem_ipsum_inv.txt")
    extraire_personnes_majeures("ages.csv", "ages_majeurs.csv")
    extraire_notes_matiere("notes.csv", "notes_matiere.csv", "PHYSIQUE")
    extraire_notes_matiere("notes.csv", "notes_matiere_maths.csv", "maths")
    extraire_notes_matiere("notes.csv", "notes_matiere_informatique.csv", "INFO")


if __name__ == "__main__":
    __main__()
