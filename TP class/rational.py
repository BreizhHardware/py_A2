class Rational:
    def __init__(self):
        self.__numerator = 0
        self.__denominator = 1

    def __pgcd(self, numerator, denominator):
        while denominator != 0:
            numerator, denominator = denominator, numerator % denominator
        return numerator

    def __ppcm(self, numerator, denominator):
        return numerator * denominator // self.__pgcd(numerator, denominator)

    def set_numerator(self, numerator):
        self.__numerator = numerator

    def set_denominator(self, denominator):
        if denominator == 0:
            print("Error: denominator can't be 0")
            return
        self.__denominator = denominator

    def get_numerateur(self):
        return self.__numerator

    def get_denominator(self):
        return self.__denominator

    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"

    def simplify(self):
        pgcd = self.__pgcd(self.__numerator, self.__denominator)
        self.__numerator //= pgcd
        self.__denominator //= pgcd

    def __eq__(self, other):
        return self.__numerator * other.__denominator == self.__denominator * other.__numerator

    def __mul__(self, other):
        numerator = self.__numerator * other.__denominator
        denominator = self.__denominator * other.__denominator
        r1 = Rational()
        r1.set_numerator(numerator)
        r1.set_denominator(denominator)
        return r1

    def __truediv__(self, other):
        numerator = self.__numerator * other.__denominator
        denominator = self.__denominator * other.__numerator
        r1 = Rational()
        r1.set_numerator(numerator)
        r1.set_denominator(denominator)
        return r1

    def __add__(self, other):
        numerator = (self.__numerator * (self.__ppcm(self.__denominator, other.__denominator) // self.__denominator) +
                     other.__numerator * (self.__ppcm(self.__denominator, other.__denominator) // other.__denominator))
        denominator = self.__ppcm(self.__denominator, other.__denominator)
        r1 = Rational()
        r1.set_numerator(numerator)
        r1.set_denominator(denominator)
        return r1
