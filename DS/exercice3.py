import matplotlib.pyplot as plot
import numpy as np
import math


def probabilite_differents():
    L = []
    for n in range(0, 90):
        eq = (math.factorial(365) / math.factorial(365 - n)) * (1 / (365 ** n))
        L.append(eq)
    return L


def probabilite_identique():
    L = []
    probaDiff = probabilite_differents()
    for n in range(len(probaDiff)):
        eq = 1 - probaDiff[n]
        L.append(eq)
    return L


def tracer_courbe_proba():
    probaDiff = probabilite_differents()
    probaInde = probabilite_identique()
    plot.plot(0, probaDiff)
    plot.show()


def calculer_nb_lignes(nom_fichier):
    file = open(nom_fichier, "r")
    nb_lignes = 0
    for line in file:
        nb_lignes += 1
    file.close()
    return nb_lignes


def nombre_eleves_par_classe(nom_fichier):
    fichier = open(nom_fichier, "r")
    dico = {}
    for ligne in fichier:
        classe = ligne.split(',')[1][:-1]
        if classe in dico:
            dico[classe] += 1
        else:
            dico[classe] = 1
    fichier.close()
    return dico


def check_same_birthday(promo, nom_fichier):
    fichier = open(nom_fichier, "r")
    BDayList = []
    for ligne in fichier:
        classe = ligne.split(',')[1][:-1]
        if classe == promo:
            BDay = ligne.split(',')[0]
            BDayList.append(BDay)
    for i in range(len(BDayList) - 1):
        j = i + 1
        while j < len(BDayList):
            if BDayList[i] == BDayList[j]:
                fichier.close()
                return True, BDayList[i]
            j += 1
    fichier.close()
    return False, None


def nb_days_identical(promo, nom_fichier):
    fichier = open(nom_fichier, "r")
    dico = {}
    BDayList = []
    for ligne in fichier:
        classe = ligne.split(',')[1][:-1]
        if classe == promo:
            BDay = ligne.split(',')[0]
            BDayList.append(BDay)
    for i in range(len(BDayList) - 1):
        if(BDayList[i] in dico):
            dico[BDayList[i]] += 1
        else:
            dico[BDayList[i]] = 1
    fichier.close()
    return dico


def get_identical_days(dico):
    '''
    for i in dico:
        if dico[i].key >= 2:
    '''
    return


print(nombre_eleves_par_classe("anniversaires_eleves_isen.txt"))
# tracer_courbe_proba()
classes = ('CSI1', 'CSI2', 'CIR1', 'CIR2', 'A3', 'M1', 'M2')
same_bithday_class = []
for c in classes:
    same_bithday_class.append(check_same_birthday(c, "anniversaires_eleves_isen.txt"))
print(same_bithday_class)
for c in classes:
    d = nb_days_identical(c, "anniversaires_eleves_isen.txt")
    print(d)
    #print(f"nombre de jours avec plus d'un anniversaire {get}")