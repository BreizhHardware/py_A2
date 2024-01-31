from PIL import Image

hiddenText1 = Image.open("hiddenText1.png")
hiddenText2 = Image.open("hiddenText2.png")
hiddenText3 = Image.open("hiddenText3.png")
hiddenText4 = Image.open("hiddenText4.png")
hiddenImage1 = Image.open("hiddenImage1.png")
hiddenImage2 = Image.open("hiddenImage2.png")
hiddenImage3 = Image.open("hiddenImage3.png")
hiddenImage4 = Image.open("hiddenImage4.png")


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


def getLenghtTuple(imageArray, nbBitsForLength, index=0):
    length = 0, nbBitsForLength - 1
    i = nbBitsForLength - 1
    while i >= 0:
        length += imageArray[index] % 2 * (2 ** i)
        i -= 1
        index += 1
    print(length)
    return length


def imageToArrayTuple(image):
    array = []
    for pixel in image.getdata():
        array.append((pixel[0], pixel[1], pixel[2]))
    return array


def getHiddenImage(image, nbBitsForSize):
    imageArray = imageToArrayTuple(image)
    print(imageArray[0:10])
    width = getLenghtTuple(imageArray, nbBitsForSize)
    height = getLenghtTuple(imageArray, nbBitsForSize, nbBitsForSize * 2)
    print(width)
    print(height)
    totalPixel = width * height * 3
    hiddenImagePixel = [imageArray[i:i + 3] for i in range(nbBitsForSize * 2, nbBitsForSize * 2 + totalPixel, 3)]
    hiddenImagePixel = [value for pixel in hiddenImagePixel for value in pixel]
    hiddenImagePixel = [(hiddenImagePixel[i], hiddenImagePixel[i + 1], hiddenImagePixel[i + 2]) for i in
                        range(0, len(hiddenImagePixel), 3)]
    hiddenImage = Image.new("RGB", (width, height))
    hiddenImage.putdata(hiddenImagePixel)
    return hiddenImage


def getHiddenImageInLastBits(image, nbBitsForSize, nbLastBits):
    #To Do
    return None
