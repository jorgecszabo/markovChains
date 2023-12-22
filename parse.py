# This script parses raw text files to be usable with the code in the notebook. It prints
# one word per line to standard output.
# Usage: python parse.py filetoparse.txt > parsedoutput.txt
import sys
import re
import unicodedata

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

regex = re.compile('[^a-zA-Z\'-]')

with open(sys.argv[1],'r') as file:
    for line in file:
        for word in line.split():
            if word[-1] == '.' or word[-1] == '?' or word[-1] == '!' or word[-1] == ':':
                print('.')
            word = strip_accents(word) # elimino acentos
            word = regex.sub('', word) # ahora le quito caracteres que no sean letras del abecedario, como puntos y comas
            word = word.lower() # lo paso a minúsculas
            print(word)
