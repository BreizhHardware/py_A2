def calculer_nb_lignes(nom_fichier) :
    file = open(nom_fichier, "r")
    nb_lignes = 0
    for line in file:
        nb_lignes += 1
    file.close()
    return nb_lignes


def recopier_fichier(nom_fichier_source, nom_fichier_destination):
    file_source = open(nom_fichier_source, "r")
    file_destination = open(nom_fichier_destination, "w")
    for line in file_source:
        file_destination.write(line)
    file_source.close()
    file_destination.close()


def inverser_fichier(nom_fichier_source, nom_fichier_destination) :
    file_source = open(nom_fichier_source, "r")
    fichier_destination = open(nom_fichier_destination, "w")
    lignes = file_source.readlines()
    lignes.reverse()
    for ligne in lignes:
        fichier_destination.write(ligne)
    file_source.close()
    fichier_destination.close()


def extraire_personnes_majeures(nom_fichier_source, nom_fichier_destination):
    file_source = open(nom_fichier_source, "r")
    file_destination = open(nom_fichier_destination, "w")
    lignes = file_source.readlines()
    file_destination.write(lignes[0])
    for ligne in lignes[1:]:
        age = int(ligne.split(";")[2])
        if age >= 18:
            file_destination.write(ligne)
    file_source.close()
    file_destination.close()


def extraire_notes_matiere(nom_fichier_source, nom_fichier_destination, nom_matiere):
    file_source = open(nom_fichier_source, "r")
    file_destination = open(nom_fichier_destination, "w")
    lignes = file_source.readlines()
    matieres = lignes[0].split(";")
    matieres[-1] = matieres[-1][:-1]
    index_matiere = -1
    nom_matiere = nom_matiere.upper()
    for i in range(len(matieres)):
        if matieres[i] == nom_matiere:
            index_matiere = i
            break
    if index_matiere == -1:
        print("La matière n'a pas été trouvée")
        return
    file_destination.write(matieres[0] + ";" + nom_matiere + "\n")
    for ligne in lignes[1:]:
        print(ligne)
        notes = ligne.split(";")
        file_destination.write(notes[0] + ";" + notes[index_matiere] + "\n")
    file_source.close()
    file_destination.close()