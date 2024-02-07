from PIL import Image

MAX_COLOR_VALUE = 255
MAX_BIT_VALUE = 8


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


def get_hidden_image(image, nb_bits_for_size, nb_last_bits=1):
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
            image_array[i * 7 + j] = ((image_array[i * 7 + j] & 0b11111110) |
                                      ((char >> (6 - j)) & 1))
    for j in range(7):
        image_array[len(text) * 7 + j] = ((image_array[len(text) * 7 + j] & 0b11111110) |
                                          (ord(delimiter) >> (6 - j) & 1))
    image.putdata([(image_array[i], image_array[i + 1], image_array[i + 2]) for i in range(0, len(image_array), 3)])
    return image


def set_hidden_text_of_length(image, text, nb_bits_for_length):
    image_array = image_to_array(image)
    length = len(text)
    for i in range(nb_bits_for_length):
        image_array[i] = (image_array[i] & 0b11111110) | ((length >> (nb_bits_for_length - 1 - i)) & 1)
    for i in range(length * 7):
        char_index = ord(text[i // 7])
        char_offset = i % 7
        if char_index < len(text):
            char = ord(text[char_index])
            image_array[i + nb_bits_for_length] = ((image_array[i + nb_bits_for_length] & 0b11111110) |
                                                   ((char >> (6 - char_offset)) & 1))
        else:
            image_array[i + nb_bits_for_length] = (image_array[i + nb_bits_for_length] & 0b11111110)
    image.putdata([(image_array[i], image_array[i + 1], image_array[i + 2]) for i in range(0, len(image_array), 3)])
    return image


'''
def set_hidden_image(image_original, image_to_hide, nb_bits_for_size, nb_last_bits = 1):
    list_bit = get_list_last_k_bits(image_original, nb_last_bits)
    binary_data = ""
    width, height = image_to_hide.size
    for i in range(nb_bits_for_size // nb_last_bits):
        binary_data += '{0:0{1}b}'.format(width, nb_bits_for_size)
        binary_data += '{0:0{1}b}'.format(height, nb_bits_for_size)
    for pixel in image_to_hide.getdata():
        r, g ,b = pixel
        binary_data += '{0:08b}'.format(b)
        binary_data += '{0:08b}'.format(r)
        binary_data += '{0:08b}'.format(g)
    while len(binary_data) < len(list_bit):
        binary_data += '0'
    for k in range(len(list_bit)):
        list_bit[k] = list_bit[k][:-nb_last_bits] + binary_data[k]
    image_original.putdata([(int(list_bit[i], 2), int(list_bit[i + 1], 2), int(list_bit[i + 2], 2))
                            for i in range(0, len(list_bit), 3)])
    return image_original
'''


# Try a method find on internet
def make_image(data, resolution):
    image = Image.new("RGB", resolution) # makes a new PIL.Image object.
    image.putdata(data) # puts the "data" matrix (pixels) onto the image.
    return image


def remove_n_least_significant_bits(value, n):
    value = value >> n
    return value << n


def get_n_least_significant_bits(value, n):
    value = value << MAX_BIT_VALUE - n
    value = value % MAX_COLOR_VALUE
    return value >> MAX_BIT_VALUE - n


def get_n_most_significant_bits(value, n):
    return value >> MAX_BIT_VALUE - n


def shit_n_bits_to_8(value, n):
    return value << MAX_BIT_VALUE - n


def set_hidden_image(image_original, image_to_hide, nb_bits_for_size):
    width, height = image_to_hide.size
    hide_image = image_original.load()
    hide_in_image = image_to_hide.load()
    data = []
    for y in range(height):
        for x in range(width):
            try:
                r_hide, g_hide, b_hide = hide_image[x, y]
                r_hide = get_n_most_significant_bits(r_hide, nb_bits_for_size)
                g_hide = get_n_most_significant_bits(g_hide, nb_bits_for_size)
                b_hide = get_n_most_significant_bits(b_hide, nb_bits_for_size)
                r_hide_in, g_hide_in, b_hide_in = hide_in_image[x, y]
                r_hide_in = remove_n_least_significant_bits(r_hide_in, nb_bits_for_size)
                g_hide_in = remove_n_least_significant_bits(g_hide_in, nb_bits_for_size)
                b_hide_in = remove_n_least_significant_bits(b_hide_in, nb_bits_for_size)

                data.append((r_hide + r_hide_in,
                             g_hide + g_hide_in,
                                b_hide + b_hide_in))

            except Exception as e:
                print(e)

    return make_image(data, (width, height))