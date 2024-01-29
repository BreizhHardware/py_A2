from PIL import Image


def getHiddenTextWithDelimiter(image, delimiter="\0"):
    pixel = list(image.getdata())
    hidden_bits = []
    for i in range(len(pixel)):
        hidden_bits.append(str(pixel[i][0] & 1))
    binary_string = ''.join(hidden_bits)
    octets = [binary_string[i:i + 8] for i in range(0, len(binary_string), 8)]
    ascii_characters = ''.join([chr(int(octet, 2)) for octet in octets])
    hidden_text = ascii_characters.split(delimiter)[0]
    return hidden_text.split(delimiter)[0]


print("Image 1")
image = Image.open('hiddenText1.png')
print(getHiddenTextWithDelimiter(image))
print("Image 2")
image = Image.open('hiddenText2.png')
print(getHiddenTextWithDelimiter(image))