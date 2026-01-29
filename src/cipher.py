# This file contains the deterministic logic

import random 
import string





ALPHABET = string.ascii_lowercase
def random_key():

  letters = list(ALPHABET)
  random.shuffle(letters)
  return dict(zip(ALPHABET,letters))
