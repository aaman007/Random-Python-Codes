from nltk.corpus import movie_reviews 
from nltk.tokenize import word_tokenize
from random import shuffle 
from nltk import FreqDist
from nltk.corpus import stopwords
import string
from nltk import NaiveBayesClassifier
from nltk import classify 
import nltk

'''
print (len(movie_reviews.fileids())) # Output: 2000
 
# Review categories
print (movie_reviews.categories()) # Output: [u'neg', u'pos']
 
# Total positive reviews
print (len(movie_reviews.fileids('pos'))) # Output: 1000
 
# Total negative reviews
print (len(movie_reviews.fileids('neg'))) # Output: 1000
 
positive_review_file = movie_reviews.fileids('pos')[0] 
print (positive_review_file) # Output: pos/cv000_29590.txt
'''

documents = []
 
for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        #documents.append((list(movie_reviews.words(fileid)), category))
        documents.append((movie_reviews.words(fileid), category))
 
# print (len(documents)) # Output: 2000
 
# print first tuple
# print (documents[0])
 
# shuffle the document list
shuffle(documents)

all_words = [word.lower() for word in movie_reviews.words()]
 
# print first 10 words
# print(all_words[:10])
 
all_words_frequency = FreqDist(all_words)
 
# print (all_words_frequency)
 
# print 10 most frequently occurring words
# print (all_words_frequency.most_common(10))
 
stopwords_english = stopwords.words('english')
# print (stopwords_english)
 
# create a new list of words by removing stopwords from all_words
all_words_without_stopwords = [word for word in all_words if word not in stopwords_english]
 
# print the first 10 words
# print (all_words_without_stopwords[:10])
 
# print (string.punctuation)
 
# create a new list of words by removing punctuation from all_words
all_words_without_punctuation = [word for word in all_words if word not in string.punctuation]
 
# print the first 10 words
# print (all_words_without_punctuation[:10])

# Let's name the new list as all_words_clean 
# because we clean stopwords and punctuations from the word list
 
all_words_clean = []
for word in all_words:
    if word not in stopwords_english and word not in string.punctuation:
        all_words_clean.append(word)
 
# print (all_words_clean[:10])

all_words_frequency = FreqDist(all_words_clean)
 
# print (all_words_frequency)
 
# print 10 most frequently occurring words
# print (all_words_frequency.most_common(10))

# print (len(all_words_frequency)) # Output: 39586
 
# get 2000 frequently occuring words
most_common_words = all_words_frequency.most_common(5000)
# print (most_common_words[:10])
 
# print (most_common_words[1990:])
 
# the most common words list's elements are in the form of tuple
# get only the first element of each tuple of the word list
word_features = [item[0] for item in most_common_words]
# print (word_features[:10])

def document_features(document):
    # "set" function will remove repeated/duplicate tokens in the given list
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features
 
# get the first negative movie review file
movie_review_file = movie_reviews.fileids('neg')[0] 
# print (movie_review_file)
 
#print (document_features(movie_reviews.words(movie_review_file)))

feature_set = [(document_features(doc), category) for (doc, category) in documents]
# print (feature_set[0])

# print (len(feature_set)) # Output: 2000
 
test_set = feature_set[:1000]
train_set = feature_set[1000:]
 
# print (len(train_set)) # Output: 1600
# print (len(test_set)) # Output: 400
 
clf = NaiveBayesClassifier.train(train_set) 
accuracy = nltk.classify.accuracy(clf,test_set)
print(accuracy)
 
while(True):
	print("Enter the review or Exit to close the application")
	custom_review = input()
	
	if custom_review == "Exit":
		break;
 
	custom_review_tokens = word_tokenize(custom_review)
	custom_review_set = document_features(custom_review_tokens)
 
	print(clf.classify(custom_review_set))

	prob_result = clf.prob_classify(custom_review_set)
	print(prob_result)
	print(prob_result.max())
	print(prob_result.prob("neg"))
	print(prob_result.prob("pos"))
