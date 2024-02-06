from PIL import Image

hiddenText1 = Image.open("hiddenText1.png")
hiddenText2 = Image.open("hiddenText2.png")
hiddenText3 = Image.open("hiddenText3.png")
hiddenText4 = Image.open("hiddenText4.png")
hiddenImage1 = Image.open("hiddenImage1.png")
hiddenImage2 = Image.open("hiddenImage2.png")
hiddenImage3 = Image.open("hiddenImage3.png")
hiddenImage4 = Image.open("hiddenImage4.png")
gladius = Image.open("Gladius.jpg")
zeusMK2CL = Image.open("Zeus MKII CL.jpeg")


def imageToArray(image):
    array = []
    for pixel in image.getdata():
        array.append(pixel[0])
        array.append(pixel[1])
        array.append(pixel[2])
    return array


def getLength(imageArray, nbBitsForLength, index=0):
    length, i = 0, nbBitsForLength - 1
    for len in range(index, index + nbBitsForLength):
        length += imageArray[len] % 2 * (2 ** i)
        i -= 1
    return length


def getChar(imageArray, index):
    binN, i = 0, 6
    for j in range(index, index + 7):
        binN += (imageArray[j] % 2) * (2 ** i)
        i -= 1
    return chr(binN)


def getHiddenTextWithDelimiter(image, delimiter):
    imageArray = imageToArray(image)
    hiddenText = ""
    i = 0
    while getChar(imageArray, i) != delimiter:
        hiddenText += getChar(imageArray, i)
        i += 7
    return hiddenText


def getHiddenTextOfLength(image, nbBitsForLength):
    imageArray = imageToArray(image)
    hiddenText = ""
    for i in range(nbBitsForLength, ((getLength(imageArray, nbBitsForLength) * 7) + nbBitsForLength), 7):
        hiddenText += getChar(imageArray, i)
    return hiddenText


def getListLastKBits(image, k):
    list_pixel = list(image.getdata())
    list_bit = []
    for t in list_pixel:
        for ind in range(3):
            b_pixel = '{0:08b}'.format(t[ind])
            list_bit.append(b_pixel[-k::])
    return list_bit


def parseDimensions(list_bit, nbBitsForSize, nbLastBits):
    first_bits = list_bit[:nbBitsForSize // nbLastBits:]
    second_bits = list_bit[nbBitsForSize // nbLastBits: 2 * (nbBitsForSize // nbLastBits):]
    width = int("".join(first_bits), 2)
    height = int("".join(second_bits), 2) - 1
    return width, height


def parseRGB(binarie):
    r = int(binarie[:8:], 2)
    g = int(binarie[8:16:], 2)
    b = int(binarie[16:32:], 2)
    return r, g, b


def getHiddenImage(image, nbBitsForSize, nbLastBits):
    list_bit = getListLastKBits(image, nbLastBits)
    bin = ""

    width, height = parseDimensions(list_bit, nbBitsForSize, nbLastBits)

    secret_image = Image.new("RGB", (width, height), (0, 0, 0))
    col = -1
    row = -1

    for k in range(2 * (nbBitsForSize // nbLastBits), len(list_bit)):
        bin += list_bit[k]
        if len(bin) == 24:
            if col == width:
                col = 0
                row += 1
            if row == height:
                return secret_image

            r, g, b = parseRGB(bin)
            secret_image.putpixel((col, row), (r, g, b))
            col += 1
            bin = ""


def setHiddenTextWithDelimiter(image, text, delimiter):
    imageArray = imageToArray(image)
    for i in range(len(text)):
        char = ord(text[i])
        for j in range(7):
            imageArray[i * 7 + j] = (imageArray[i * 7 + j] & 0b11111110) | ((char >> (6 - j)) & 1)
    for j in range(7):
        imageArray[len(text) * 7 + j] = (imageArray[len(text) * 7 + j] & 0b11111110) | (ord(delimiter) >> (6 - j) & 1)
    image.putdata([(imageArray[i], imageArray[i + 1], imageArray[i + 2]) for i in range(0, len(imageArray), 3)])
    return image


def setHiddenTextOfLength(image, text, nbBitsForLength):
    imageArray = imageToArray(image)
    length = len(text)
    for i in range(nbBitsForLength):
        imageArray[i] = (imageArray[i] & 0b11111110) | ((length >> (nbBitsForLength - 1 - i)) & 1)
    for i in range(len(text)):
        char = ord(text[i])
        for j in range(7):
            imageArray[i * 7 + nbBitsForLength] = (imageArray[i * 7 + nbBitsForLength] & 0b11111110) | ((char >> (6 - j)) & 1)
    image.putdata([(imageArray[i], imageArray[i + 1], imageArray[i + 2]) for i in range(0, len(imageArray), 3)])
    return image
