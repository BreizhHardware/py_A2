def calcul_mensualite():
    C = int(input("entrer le capital > "))
    while C < 0:
        print("Le capital ne peut pas être négatif")
        C = int(input("entrer le capital > "))
    n = int(input("entrer la duree > "))
    while n < 0:
        print('La duree ne peut pas être négative')
        n = int(input("entrer la duree > "))
    t = int(input("entrer le taux > "))
    while t < 0:
        print("Le taux ne peut pas être négatif")
        t = int(input("entrer le taux > "))
    print("liste retournée par la fonction emprunt")
    print(emprunt(C, n, t))


def mensualite(capital, duree, taux):
    numerateur = capital * (taux / 12)
    denominateur = 1 - ((1 + (taux / 12)) ** -duree)
    print(numerateur)
    print()
    print(denominateur)
    mensualite = numerateur / denominateur
    return mensualite


def emprunt(capital, duree, taux):
    i = duree
    interet = taux / 12
    interetCumul = 0
    bigL = []
    while i > 0:
        print(i)
        L = []
        interetPaye = capital * interet
        m = mensualite(capital, i, taux)
        capital = capital + interetPaye - m
        interetCumul += interet
        L.append(capital)
        L.append(interetCumul)
        L.append(interet)
        interet -= 0.27
        bigL.append(L)
        i -= 1
    return bigL


calcul_mensualite()
