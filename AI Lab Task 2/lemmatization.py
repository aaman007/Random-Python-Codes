import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize,word_tokenize

lemmatizer = WordNetLemmatizer()


# Getting root of verbs in a sentence

sentence = "He was running and eating at same time. He has bad habit of swimming after playing long hours in the Sun."
punctuations = "?!.,;:"
words = word_tokenize(sentence)

for word in words:
	if word in punctuations:
		words.remove(word)

# Getting root of every parts of speech(pos) which is verb

print("{0:20}{1:20}".format("Word","Lemma"))
for word in words:
	print("{0:20}{1:20}".format(word,lemmatizer.lemmatize(word,pos="v")))
print("")

# Getting root words for adjectives
word_list = ["good","better","best","great","greater","greatest","big","bigger","biggest","bad","worse","worst"]

print("{0:20}{1:20}".format("Word","Lemma"))
for word in word_list:
	print("{0:20}{1:20}".format(word,lemmatizer.lemmatize(word,pos="a")))
