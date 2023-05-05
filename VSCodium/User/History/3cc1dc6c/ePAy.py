from nltk.corpus import wordnet as wn
import nltk

nltk.download('omw-1.4')

synonyms = []

for syn in wn.synsets("love"):
    for i in syn.lemmas():
        synonyms.append(l.name())

print(set(synonyms))
