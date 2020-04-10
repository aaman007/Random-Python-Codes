from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.tokenize import sent_tokenize,word_tokenize

# Creating object for both Stemmers
porter = PorterStemmer()
lancaster = LancasterStemmer()

def stemSentence(sentence):
	words = word_tokenize(sentence)
	stem_words = []
	
	for word in words:
		stem_words.append(porter.stem(word))
		stem_words.append(" ")
	return "".join(stem_words)


# Processing Words

# Porter Stemmer Part
print("Stemming using PorterStemmer")
print("tigers : " + porter.stem("tigers"))
print("trouble : " + porter.stem("trouble"))
print("troubling : " + porter.stem("troubling"))
print("troubled : " + porter.stem("troubled"))
print("")

# Lancaster Stemmer Part
print("Stemming using LancasterStemmer")
print("tigers : " + lancaster.stem("tigers"))
print("trouble : " + lancaster.stem("trouble"))
print("troubling : " + lancaster.stem("troubling"))
print("troubled : " + lancaster.stem("troubled"))
print("")

# Word List
word_list = ["friend","friends","friendship","stabil","destabilize","misunderstanding","railroad","moonlight","football"]

print("{0:20}{1:20}{2:20}".format("Word","PorterStemmer","LancasterStemmer"))

for word in word_list:
	print("{0:20}{1:20}{2:20}".format(word,porter.stem(word),lancaster.stem(word)))
print("")


# Stemming Sentences
print(stemSentence("The tigers are roaring they likes to eat meat they are running it is raining."))
print(stemSentence("This is amazing."))


