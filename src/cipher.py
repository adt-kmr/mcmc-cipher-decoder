# This file contains the deterministic logic

import random 
import string





ALPHABET = string.ascii_lowercase
def random_key():

  letters = list(ALPHABET)
  random.shuffle(letters)
  return dict(zip(ALPHABET,letters))







key = random_key()

key['a'], key['z']







def encrypt(plaintext,key):
  return ''.join(key.get(c,c) for c in plaintext.lower())


def decrypt(ciphertext,key):
  inverse_key = { v: k for k, v in key.items()}

  return ''.join(inverse_key.get(c, c) for c in ciphertext.lower())

