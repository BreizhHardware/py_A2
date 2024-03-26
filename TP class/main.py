from rational import Rational
def __main__():
    print("--------------------Rational--------------------")
    r1 = Rational()
    r1.set_numerator(15)
    r1.set_denominator(10)
    r2 = Rational()
    r2.set_numerator(1)
    r2.set_denominator(3)
    print("--------------------r1--------------------")
    print(r1)
    print("--------------------r2--------------------")
    print(r2)
    r1.simplify()
    r2.simplify()
    print("--------------------r1.simplify--------------------")
    print(r1)
    print("--------------------r2.simplify--------------------")
    print(r2)
    print("--------------------r1 == r2--------------------")
    print(r1 == r2)
    print("--------------------r1 * r2--------------------")
    r3 = r1 * r2
    print(r3)
    print("--------------------r1 / r2--------------------")
    r4 = r1 / r2
    print(r4)
    print("--------------------r1 + r2--------------------")
    r5 = r1 + r2
    print(r5)
    print("--------------------r3--------------------")
    r3 = Rational()
    r3.set_numerator(2346)
    r3.set_denominator(1548)
    print(r3)
    r3.simplify()
    print(r3)
    print("--------------------r4--------------------")
    r4 = Rational()
    r4.set_numerator(9745)
    r4.set_denominator(546)
    print(r4)
    r4.simplify()
    print(r4)
    print("--------------------r3 + r4--------------------")
    r5 = r3 + r4
    print(r5)



if __name__ == "__main__":
    __main__()