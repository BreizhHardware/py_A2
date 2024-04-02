def transform_letter_in_number(letter):
    return ord(letter) - 64


def isNumberValid(idNumber):
    strIdNumberWith2First = ""
    for i in range(len(idNumber)):
        if i == 0 or i == 1:
            strIdNumberWith2First += str(transform_letter_in_number(idNumber[i]))
        else:
            strIdNumberWith2First += str(idNumber[i])
    idNumberWith2First = int(strIdNumberWith2First)
    reste = idNumberWith2First % 9
    if reste == 7:
        return True
    else:
        return False


idNumber = "UF9052784116"
print(isNumberValid(idNumber))
