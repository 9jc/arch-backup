import os
import time
from nltk.corpus import wordnet as wn

os.system("clear||cls")
# print("Program to match english word meanings\n") #Title

# a_colum = open("a.txt","r")
b_colum = open("b.txt","r")

with open("a.txt", 'r') as f:
    for i, x in enumerate(f):
        if 1 <= i <= 15:
            print(x)
            time.sleep(3)
        elif i > 15:
            break





