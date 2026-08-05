from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import nltk
lemmatizer = WordNetLemmatizer()

result = lemmatizer.lemmatize("mice")
print(result)

result = lemmatizer.lemmatize("going" , pos=wordnet.VERB)
print(result)


# part of speech tagging

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

nltk.download("averaged_perceptron_tagger_eng")
sentence = "Donald Trump has a devoted following".split()

words_and_tags = nltk.pos_tag(sentence)
print(words_and_tags)

for word , tag in words_and_tags:
    lemma = lemmatizer.lemmatize(word , pos=get_wordnet_pos(tag))
    print(lemma , end=" ")

sentence = "the cat was following the bird as it flew by".split()

words_and_tags = nltk.pos_tag(sentence)
print(words_and_tags)

for word , tag in words_and_tags:
    lemma = lemmatizer.lemmatize(word , pos=get_wordnet_pos(tag))
    print(lemma,end=" ")

print()
sentence = "ahmed is tired and will probably be commiting suicide soon".split()
words_nd_tags = nltk.pos_tag(sentence)
for word , tag in words_nd_tags:
    lemma = lemmatizer.lemmatize(word , pos=get_wordnet_pos(tag))
    print(lemma , end=" ")

