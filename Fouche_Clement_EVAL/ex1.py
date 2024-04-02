def checkIfPrimeNumber(n):
    if n % n == 0 & n % 1 == 0:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    else:
        return False

def circulaire(n):
    toTest = []
    toTest.append(n)
    for i in range(len(str(n)) - 1):
        toTest.append(int(str(toTest[i])[-1] + str(toTest[i])[:-1]))
    print(toTest)
    for number in toTest:
        if checkIfPrimeNumber(number) == False:
            return False
    return True

if __name__ == '__main__':
    print('719 est circulaire : ', circulaire(719))
    print('23 est circulaire : ', circulaire(23))
    print('6102 est circulaire : ', circulaire(6102))
