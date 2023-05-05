from nltk.corpus import wordnet as wn

y = wn.syno ('runs') # "run"
x = wn.synsets('leaves') # "leaf"

print(x,y)