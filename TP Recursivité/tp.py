def mystery1(a, b):
    if b == 0:
        return a
    return mystery1(a + 1, b - 1)


def mystery2(l1, l2=None):
    if l2 is None:
        l2 = []
    if len(l1) == 0:
        return l2
    if l1[0] not in l2:
        l2.append(l1[0])
    return mystery2(l1[1:], l2)


def modulo(x, y):
    """Computes x % y recursively """
    if y == 0:
        return "Error: Modulo by zero is not possible."
    if x < y:
        return x
    return modulo(x - y, y)


def reverseString(s, i=0):
    """Reverses the string s recursively """
    if i == len(s):
        return ""
    else:
        return reverseString(s, i + 1) + s[i]


def pow(x, n):
    """Computes x ** n recursively """
    if n == 0:
        return 1
    return x * pow(x, n - 1)


def listSum(l):
    """Computes the sum of the elements of a list recursively"""
    if len(l) == 0:
        return 0
    return l[0] + listSum(l[1:])


def product(a, b):
    """Computes the product of a and b recursively"""
    if b == 0:
        return 0
    return a + product(a, b - 1)


def even(n):
    """Returns True if n is even, False otherwise"""
    if n == 0:
        return True
    if n == 1:
        return False
    return even(n - 2)


def odd(n):
    """Returns True if n is odd, False otherwise"""
    if n == 0:
        return False
    if n == 1:
        return True
    return odd(n - 2)


def f1():
    i = f2(2)
    return i


def f2(j):
    k = f3(3 * j)
    return k


def f3(l):
    m = l + 1
    return m


def printNumber(i):
    print(i)
    printNumber(i - 1)


print(f1())
printNumber(3)

print(mystery1(5, 0))
print(mystery1(0, 3))
print(mystery1(2, 9))
print(mystery1(8, 6))

print(mystery2([]))
print(mystery2([1, 1, 1, ]))
print(mystery2([1, 2, 2, 3, 4, 3, 5, 1]))

# print(42 % 0)
print(modulo(42, 0))
print(modulo(6, 13))
print(modulo(37, 10))

print(reverseString(""))
print(reverseString("bonjour"))
print(reverseString("ressasser"))

print(pow(42, 0))
print(pow(1, 10))
print(pow(2, 5))

print(listSum([]))
print(listSum([42]))
print(listSum([3, 1, 5, 2]))

print(product(5, 2))
print(product(9, 3))

print(even(0))
print(even(1))
print(even(48))
print(even(49))

print(odd(0))
print(odd(1))
print(odd(48))
print(odd(49))
