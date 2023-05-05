from nltk.corpus import wordnet as wn

y = wn.synsets('runs') # "run"
x = wn.synsets('leaves') # "leaf"

print(x,y)