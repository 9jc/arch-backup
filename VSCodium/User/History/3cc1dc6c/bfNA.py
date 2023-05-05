from nltk.corpus import wordnet as wn

synonyms = []

for syn in wn.synsets("love"):
    for i in syn.lemmas():
        synonyms.append(l.name())

print(set(synonyms))
