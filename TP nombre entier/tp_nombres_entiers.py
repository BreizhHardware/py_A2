def binary_to_int(b):
    n = 0
    for i in range(len(b)):
        n = n * 2 + int(b[i])
    return n


def get_nb_bits(i):
    n = 0
    while 2 ** n <= i:
        n += 1
    return n


def int_to_bits(i):
    b = ""
    while i > 0:
        b = str(i % 2) + b
        i = i // 2
    return b


def positive_or_negative_4_bytes_int_to_bits(i):
    if i < 0:
        i = 2 ** 32 + i
    b = ""
    while i > 0:
        b = str(i % 2) + b
        i = i // 2
    b = "0" * (4 - len(b)) + b
    return b


def get_bits(b, i):
    if i <= len(b):
        return int(b[len(b) - i])
    else:
        return 0


def add(b1, b2):
    n = max(len(b1), len(b2))
    b1 = "0" * (n - len(b1)) + b1
    b2 = "0" * (n - len(b2)) + b2
    retenue = 0
    somme = ""
    for i in range(n - 1, -1, -1):
        s = int(b1[i]) + int(b2[i]) + retenue
        somme = str(s % 2) + somme
        retenue = s // 2
    if retenue > 0:
        somme = "1" + somme
    return somme


