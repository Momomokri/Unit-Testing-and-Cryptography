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
    temp_str = ""
    new_string = ""
    for i in range(len(text)):
        if text[i].upper() not in alpha:
            continue
        else:
            num = alpha.find(text[i].upper()) * a % 26
            temp_str += alpha[num]
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
            continue
        else:
            num = alpha.find(temp_str[i].upper()) * mod_inverse(a, 26) % 26
            new_string += alpha[num]
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
    num = 0
    for i in range(len(ngram)):
        num += alpha.find(ngram[i]) * (26**i)
    return num
def convert_to_text(num, n):
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



# PART 3

# These are the functions you'll need to write:
def affine_n_encode(text, n, a, b):
    new_str = ""
    index = 0
    num_x = len(text) % n
    if num_x > 0:
        for i in range(n - num_x):
            text += "X"
    num_grams = len(text) // n
    for i in range(n):
        n_gram_num = convert_to_num(text[index:(index + num_grams)])
        n_gram_num = a * n_gram_num + b % (26**n)
        new_str += convert_to_text(n_gram_num, num_grams)
        index += num_grams
    return new_str




def affine_n_decode(text, n, a, b):
    new_str = ""
    index = 0
    num_grams = len(text) // n
    for i in range(n):
        n_gram_num = convert_to_num(text[index:(index + num_grams)])
        n_gram_num = mod_inverse(a, 26**n) * (n_gram_num - b) % (26 ** n)
        new_str += convert_to_text(n_gram_num, num_grams)
        index += num_grams
    return new_str

test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
n = 5
a = 347
b = 1721
enc = affine_n_encode(test, n, a, b)
dec = affine_n_decode(enc, n, a, b)
print(enc, dec)
# If this worked, dec should be the same as test!