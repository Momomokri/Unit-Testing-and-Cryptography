# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def sub_encode(text, codebet):
    new_string = ""
    for i in range(len(text)):
        num = alpha.find(text[i])
        new_string += codebet[num]
    return new_string


def sub_decode(text, codebet):
    new_string = ""
    for i in range(len(text)):
        num = codebet.find(text[i])
        new_string += alpha[num]
    return new_string


test = "HELLOWORLD"
cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
enc = sub_encode(test, cipher_alphabet)
dec = sub_decode(enc, cipher_alphabet)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
