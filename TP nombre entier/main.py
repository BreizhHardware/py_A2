from sys import argv as args
from tp_nombres_entiers import *

def is_equal(a, b):
    return a == b

def __main__():
    if len(args) == 2:
        if args[1] == "tp_nombres_entiers":
            print("=======================binary_to_int=======================")
            print(binary_to_int('11'))
            print(binary_to_int('101010'))
            print("=======================get_nb_bits=======================")
            print(get_nb_bits(3))
            print(get_nb_bits(32))
            print("=======================int_to_bits=======================")
            print(int_to_bits(3))
            print(int_to_bits(32))
            print("=======================initialisation en binaire=======================")
            i = 42
            j = 0b101010
            print(i)
            print(j)
            print(is_equal(i, j))
            print("=======================masque=======================")
            i = 183
            mask = 0b10010001
            j = i & mask
            print(j)
            print("=======================positive_or_negative_4_bytes_int_to_bits=======================")
            print(positive_or_negative_4_bytes_int_to_bits(0))
            print(positive_or_negative_4_bytes_int_to_bits(1))
            print(positive_or_negative_4_bytes_int_to_bits(2))
            print(positive_or_negative_4_bytes_int_to_bits(3))
            print(positive_or_negative_4_bytes_int_to_bits(4))
            print(positive_or_negative_4_bytes_int_to_bits(5))
            print(positive_or_negative_4_bytes_int_to_bits(6))
            print(positive_or_negative_4_bytes_int_to_bits(7))
            print(positive_or_negative_4_bytes_int_to_bits(-1))
            print(positive_or_negative_4_bytes_int_to_bits(-2))
            print(positive_or_negative_4_bytes_int_to_bits(-3))
            print(positive_or_negative_4_bytes_int_to_bits(-4))
            print(positive_or_negative_4_bytes_int_to_bits(-5))
            print(positive_or_negative_4_bytes_int_to_bits(-6))
            print(positive_or_negative_4_bytes_int_to_bits(-7))
            print(positive_or_negative_4_bytes_int_to_bits(-8))
            print("=======================get_bits=======================")
            print(get_bits('10110', 1))
            print(get_bits('10110', 2))
            print(get_bits('10110', 3))
            print(get_bits('10110', 4))
            print(get_bits('10110', 5))
            print(get_bits('10110', 6))
            print("=======================add=======================")
            print(add('010101', '100111'))
            print(add('1', '1'))
        else:
            print("Usage: python main.py <nombre>")
            return
    else:
        print("Usage: python main.py <nombre>")
        return

if __name__ == "__main__":
    __main__()