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


def image_to_array(image):
    array = []
    for pixel in image.getdata():
        array.append(pixel[0])
        array.append(pixel[1])
        array.append(pixel[2])
    return array


def get_length(image_array, nb_bits_for_length, index=0):
    length, i = 0, nb_bits_for_length - 1
    for len in range(index, index + nb_bits_for_length):
        length += image_array[len] % 2 * (2 ** i)
        i -= 1
    return length


def get_char(image_array, index):
    binN, i = 0, 6
    for j in range(index, index + 7):
        binN += (image_array[j] % 2) * (2 ** i)
        i -= 1
    return chr(binN)


def get_hidden_text_with_delimiter(image, delimiter):
    image_array = image_to_array(image)
    hidden_text = ""
    i = 0
    while get_char(image_array, i) != delimiter:
        hidden_text += get_char(image_array, i)
        i += 7
    return hidden_text


def get_hidden_text_of_length(image, nb_bits_for_length):
    image_array = image_to_array(image)
    hidden_text = ""
    for i in range(nb_bits_for_length, ((get_length(image_array, nb_bits_for_length) * 7) + nb_bits_for_length), 7):
        hidden_text += get_char(image_array, i)
    return hidden_text


def get_list_last_k_bits(image, k):
    list_pixel = list(image.getdata())
    list_bit = []
    for t in list_pixel:
        for ind in range(3):
            b_pixel = '{0:08b}'.format(t[ind])
            list_bit.append(b_pixel[-k::])
    return list_bit


def parse_dimensions(list_bit, nb_bits_for_size, nb_last_bits):
    first_bits = list_bit[:nb_bits_for_size // nb_last_bits:]
    second_bits = list_bit[nb_bits_for_size // nb_last_bits: 2 * (nb_bits_for_size // nb_last_bits):]
    width = int("".join(first_bits), 2)
    height = int("".join(second_bits), 2) - 1
    return width, height


def parse_RGB(binary):
    r = int(binary[:8:], 2)
    g = int(binary[8:16:], 2)
    b = int(binary[16:32:], 2)
    return r, g, b


def get_hidden_image(image, nb_bits_for_size, nb_last_bits = 1):
    list_bit = get_list_last_k_bits(image, nb_last_bits)
    bin = ""

    width, height = parse_dimensions(list_bit, nb_bits_for_size, nb_last_bits)

    secret_image = Image.new("RGB", (width, height), (0, 0, 0))
    col = -1
    row = -1

    for k in range(2 * (nb_bits_for_size // nb_last_bits), len(list_bit)):
        bin += list_bit[k]
        if len(bin) == 24:
            if col == width:
                col = 0
                row += 1
            if row == height:
                return secret_image

            r, g, b = parse_RGB(bin)
            secret_image.putpixel((col, row), (r, g, b))
            col += 1
            bin = ""


def set_hidden_text_with_delimiter(image, text, delimiter):
    image_array = image_to_array(image)
    for i in range(len(text)):
        char = ord(text[i])
        for j in range(7):
            image_array[i * 7 + j] = (image_array[i * 7 + j] & 0b11111110) | ((char >> (6 - j)) & 1)
    for j in range(7):
        image_array[len(text) * 7 + j] = (image_array[len(text) * 7 + j] & 0b11111110) | (ord(delimiter) >> (6 - j) & 1)
    image.putdata([(image_array[i], image_array[i + 1], image_array[i + 2]) for i in range(0, len(image_array), 3)])
    return image


def set_hidden_text_of_length(image, text, nb_bits_for_length):
    image_array = image_to_array(image)
    length = len(text)
    for i in range(nb_bits_for_length):
        image_array[i] = (image_array[i] & 0b11111110) | ((length >> (nb_bits_for_length - 1 - i)) & 1)
    for i in range(length * 7):
        char = ord(text[i // 7])
        image_array[i + nb_bits_for_length] = (image_array[i + nb_bits_for_length] & 0b11111110) | ((char >> (6 - (i % 7))) & 1)
    image.putdata([(image_array[i], image_array[i + 1], image_array[i + 2]) for i in range(0, len(image_array), 3)])
    return image


def set_hidden_image(image_original, image_to_hide, nb_bits_for_size, nb_last_bits = 1):
    list_bit = get_list_last_k_bits(image_original, nb_last_bits)
    bin = ""
    width, height = image_to_hide.size
    for i in range(nb_bits_for_size // nb_last_bits):
        bin += '{0:08b}'.format(width)[i * nb_last_bits:(i + 1) * nb_last_bits:]
        bin += '{0:08b}'.format(height + 1)[i * nb_last_bits:(i + 1) * nb_last_bits:]
    for i in range(height):
        for j in range(width):
            r, g, b = image_to_hide.getpixel((j, i))
            bin += '{0:08b}'.format(r)
            bin += '{0:08b}'.format(g)
            bin += '{0:08b}'.format(b)
    for k in range(len(bin)):
        list_bit[k] = list_bit[k][:-nb_last_bits:] + bin[k]
    image_original.putdata([(int(list_bit[i], 2), int(list_bit[i + 1], 2), int(list_bit[i + 2], 2)) for i in range(0, len(list_bit), 3)])
    return image_original
