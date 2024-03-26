class Test:
    def __init__(self, n):
        self.__n = n

    def afficher_n(self):
        print(self.__n)

    def __str__(self):
        return "n = " + str(self.__n)

    def __add__(self, other):
        return self.__n + other.__n


T1 = Test(2)
T1.afficher_n()
print(T1)
T2 = Test(3)
print(T1 + T2)