def celsius_fahrenheit(celcius):
    return celcius * 9 / 5 + 32


def mention(note):
    if note < 0:
        return "Note hors échelle"
    if note < 10:
        return "Insuffisant"
    elif note < 12:
        return "Passable"
    elif note < 14:
        return "Assez bien"
    elif note < 16:
        return "Bien"
    elif note < 18:
        return "Très bien"
    elif note < 20:
        return "Note hors échelle"
    else:
        return "Note hors échelle"


def nombres_pairs(n):
    return [i for i in range(n) if i % 2 == 0]


def remplacer(texte, caractere, nouveau_caractere):
    return "".join([nouveau_caractere if c == caractere else c for c in texte])


def est_palindrome(texte):
    return texte == texte[::-1]


def triplets_pythagoriciens(n):
    return [(a, b, c) for a in range(1, n) for b in range(a, n) for c in range(b, n) if a ** 2 + b ** 2 == c ** 2]


def diviseurs(n):
    return [i for i in range(1, n + 1) if n % i == 0]


def est_parfait(n):
    return sum(diviseurs(n)) == n * 2


def occurrences_lettres(mot):
    return {c: mot.count(c) for c in mot}


points_lettres = {
    1 : ["E", "A", "I", "N", "O", "R", "S", "T", "U", "L"],
    2 : ["D", "M", "G"],
    3 : ["B", "C", "P"],
    4 : ["F", "H", "V"],
    8 : ["J", "Q"],
    10 : ["K", "W", "X", "Y", "Z"]
}


def calculer_score(mot, points_lettres):
    return sum([points for points, lettres in points_lettres.items() for lettre in mot.upper() if lettre in lettres])
