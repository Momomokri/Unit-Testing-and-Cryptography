import math

# Read the instructions to see what to do!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# PART 1
# These functions are provided for you!
def mod_inverse_helper(a, b):
    q, r = a//b, a%b
    if r == 1:
        return (1, -1 * q)
    u, v = mod_inverse_helper(b, r)
    return (v, -1 * q * v + u)


def mod_inverse(a, m):
    assert math.gcd(a, m) == 1, "You're trying to invert " + str(a) + " in mod " + str(m) + " and that doesn't work!"
    return mod_inverse_helper(m, a)[1] % m


# These are the functions you'll need to write:
def affine_encode(text, a, b):
    """
    Encodes a string using Affine Cipher.
    :param text: The text to encode.
    :param a: The value to multiply by (slope)
    :param b: The value to shift by (intercept)
    :return: The encoded text.
    """
    temp_str = ""
    new_string = ""
    for i in range(len(text)):
        if text[i].upper() not in alpha:
            temp_str += text[i]
        elif text[i].isupper():
            num = alpha.find(text[i].upper()) * a % 26
            temp_str += alpha[num]
        else:
            num = alpha.find(text[i].upper()) * a % 26
            temp_str += alpha[num].lower()
    for i in range(len(text)):
        if temp_str[i].upper() not in alpha:
            new_string += temp_str[i]
        else:
            if temp_str[i].islower():
                num = alpha.find(temp_str[i].upper()) + b
                new_string += alpha[num % 26].lower()
            else:
                num = alpha.find(temp_str[i]) + b
                new_string += alpha[num % 26]
    return new_string


def affine_decode(text, a, b):
    """
    Decodes a string using Affine Cipher.
    :param text: The text to decode.
    :param a: The value to use in mod inverse (slope)
    :param b: The value to shift back by (intercept)
    :return: The decoded text.
    """
    temp_str = ""
    new_string = ""
    for i in range(len(text)):
        if text[i].upper() not in alpha:
            temp_str += text[i]
        else:
            if text[i].islower():
                num = alpha.find(text[i].upper()) - b
                temp_str += alpha[num % 26].lower()
            else:
                num = alpha.find(text[i]) - b
                temp_str += alpha[num % 26]
    for i in range(len(text)):
        if temp_str[i].upper() not in alpha:
            new_string += temp_str[i]
        elif temp_str[i].isupper():
            num = alpha.find(temp_str[i].upper()) * mod_inverse(a, 26) % 26
            new_string += alpha[num]
        else:
            num = alpha.find(temp_str[i].upper()) * mod_inverse(a, 26) % 26
            new_string += alpha[num].lower()
    return new_string


test = "HELLOWORLD"
a = 3
b = 9
enc = affine_encode(test, a, b)
dec = affine_decode(enc, a, b)
print(enc)
print(dec)
# If this worked, dec should be the same as test!


# PART 2
# These  are the functions you'll need to write:
def convert_to_num(ngram):
    """
    Converts a text into a number.
    :param ngram: The text to convert.
    :return: A number based on the input text.
    """
    num = 0
    for i in range(len(ngram)):
        if ngram[i] not in alpha:
            continue
        else:
            num += alpha.find(ngram[i]) * (26**i)
    return num


def convert_to_text(num, n):
    """
    Converts a number to a text.
    :param num: The number to convert.
    :param n: The length of the text to be converted to.
    :return: The converted text.
    """
    new_str = ""
    quo = num
    for i in range(n):
        new_str += alpha[quo % 26]
        quo //= 26
    return new_str


test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
l = len(test)
num = convert_to_num(test)
answer = convert_to_text(num, l)
print(num)
print(answer)
# If this worked, answer should be the same as test!


# These are the functions you'll need to write:
def affine_n_encode(text, n, a, b):
    """
    Encodes a string using Affine Cipher and Ngram ciphering.
    :param text: The text to encode.
    :param n: The amount of strings to create from text.
    :param a: The value to multiply by (slope)
    :param b: The value to shift by (intercept)
    :return: The encoded text.
    """
    new_str = ""
    for i in range(len(text)):
        if text[i].upper() in alpha:
            new_str += text[i]
    text = new_str
    text = text.upper()
    while len(text) % n != 0:
        text += "X"
    new_str = ""
    for i in range(0, len(text), n):
        n_gram = text[i:(i + n)]
        x = convert_to_num(n_gram)
        number = (a * x + b) % (26 ** n)
        new_str += convert_to_text(number, n)
    return new_str


def affine_n_decode(text, n, a, b):
    """
    Decodes a string using Affine Cipher and Ngram ciphering.
    :param text: The text to decode.
    :param n: The amount of strings to create from text.
    :param a: The value to use in mod inverse (slope)
    :param b: The value to shift back by (intercept)
    :return: The decoded text.
    """
    new_str = ""
    for i in range(len(text)):
        if text[i].upper() in alpha:
            new_str += text[i]
    text = new_str
    text = text.upper()
    new_str = ""
    for i in range(0, len(text), n):
        n_gram = text[i:(i + n)]
        x = convert_to_num(n_gram)
        number = (mod_inverse(a, 26**n) * (x - b)) % (26 ** n)
        new_str += convert_to_text(number, n)
    return new_str


test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
n = 5
a = 347
b = 1721
enc = affine_n_encode(test, n, a, b)
dec = affine_n_decode(enc, n, a, b)
print(enc, dec)
# If this worked, dec should be the same as test!
