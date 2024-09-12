# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_"

def vig_encode(text, keyword):
  """
  Encodes text using vigenere cipher rules.
  :param text: The text to be encoded.
  :param keyword: The keyword to be used for the vigenere cipher.
  :return: The encoded text.
  """
  new_string = ""
  for i in range(len(text)):
    if text[i].upper() not in alpha:
      continue
    else:
      if text[i].islower():
        num = alpha.find(text[i].upper()) + alpha.find(keyword[i % len(keyword)])
        new_string += alpha[num % len(alpha)].lower()
      else:
        num = alpha.find(text[i]) + alpha.find(keyword[i % len(keyword)])
        new_string += alpha[num % len(alpha)]

  return new_string


def vig_decode(text, keyword):
  """
  Decodes text using vigenere cipher rules.
  :param text: The text to be decoded.
  :param keyword: The keyword to be used for the vigenere cipher.
  :return: The decoded text.
  """
  new_string = ""
  for i in range(len(text)):
    if text[i].upper() not in alpha:
      continue
    else:
      if text[i].islower():
        num = alpha.find(text[i].upper()) - alpha.find(keyword[i % len(keyword)])
        new_string += alpha[num % len(alpha)].lower()
      else:
        num = alpha.find(text[i]) - alpha.find(keyword[i % len(keyword)])
        new_string += alpha[num % len(alpha)]
  return new_string


test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
vig_key = "TEST"
enc = vig_encode(test, vig_key)
dec = vig_decode(enc, vig_key)
print(enc)
print(dec)
# If this worked, dec should be the same as test!