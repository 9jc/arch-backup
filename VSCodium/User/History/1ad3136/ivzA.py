from nltk.corpus import wordnet as wn

y = wn.morphy('runs') # "run"
x = wn.morphy('leaves') # "leaf"

print(x,y)