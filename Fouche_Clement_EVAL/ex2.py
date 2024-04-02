class Personne:
    def __init__(self, name, age):
        self.__age = age
        self.__name = name

    def get_nom(self):
        return self.__name

    def get_age(self):
        return self.__age

    def increment_age(self):
        self.__age = self.__age + 1


class Eleve(Personne):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section


class Prof(Personne):
    def __init__(self, name, age, matiere):
        super().__init__(name, age)
        self.matiere = matiere


def calcule_moyenne_age(personnes):
    total = 0
    for personne in personnes:
        total += personne.get_age()
    return total / len(personnes)

if __name__ == '__main__':
    eleve1 = Eleve('eleve1', 19, 'CIR2')
    print(f"l'élève {eleve1.get_nom()} de la section {eleve1.section} a {eleve1.get_age()} ans")
    eleve1.increment_age()
    print(f"l'élève {eleve1.get_nom()} de la section {eleve1.section} a maintenant {eleve1.get_age()} ans")
    prof1 = Prof('prof1', 40, 'java')
    prof2 = Prof('prof2', 50, 'python')
    print(f"l'âge moyen des profeseurs est {calcule_moyenne_age((prof1, prof2))} ans")
    print(f"l'âge moyen des profeseurs et étudiants est {calcule_moyenne_age((prof1, prof2, eleve1)) : 0.2f} ans")
