from nltk.corpus import WordNet as wn

synonyms = []

for syn in wn.synsets("love"):
    for i in .lemmas():
        synonyms.append(l.name())

print(set(synonyms))
