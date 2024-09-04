# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def caesar_encode(text, n):
    new_string = ""
    for i in range(len(text)):
        num = alpha.find(text[i]) + n
        new_string += alpha[num % 26]
    return new_string


def caesar_decode(text, n):
    new_string = ""
    for i in range(len(text)):
        num = alpha.find(text[i]) - n
        new_string += alpha[num % 26]
    return new_string


test = "HELLOWORLD"
shift = 5
enc = caesar_encode(test, shift)
dec = caesar_decode(enc, shift)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
