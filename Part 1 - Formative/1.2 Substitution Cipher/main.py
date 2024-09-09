# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def sub_encode(text, codebet):
    """
    Encrypts text using the cipher alphabet and returns the result.
    :param text: Text to be encrypted.
    :param codebet: The cipher alphabet.
    :return: The encrypted text.
    """
    new_string = ""
    for i in range(len(text)):
        if text[i].upper() not in alpha:
            new_string += text[i]
        else:
            if text[i].islower():
                num = alpha.find(text[i].upper())
                new_string += codebet[num].lower()
            else:
                num = alpha.find(text[i])
                new_string += codebet[num]
    return new_string


def sub_decode(text, codebet):
    """
    Decrypts text using the cipher alphabet and returns the result.
    :param text: The encrypted text to be decoded.
    :param codebet: The cipher alphabet.
    :return: The decrypted text.
    """
    new_string = ""
    for i in range(len(text)):
        if text[i].upper() not in alpha:
            new_string += text[i]
        else:
            if text[i].islower():
                num = codebet.find(text[i].upper())
                new_string += alpha[num].lower()
            else:
                num = codebet.find(text[i])
                new_string += alpha[num]
    return new_string


test = "yes"
cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
enc = sub_encode(test, cipher_alphabet)
dec = sub_decode(enc, cipher_alphabet)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
