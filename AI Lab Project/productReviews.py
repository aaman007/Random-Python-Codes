import nltk
import random
from nltk.corpus import product_reviews
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = stopwords.words('english')
stop2 = ['.',',','&','(','?','!',')']

def extract(words):
    res = dict([(word.lower(),True) for word in words])
    #print(res)
    return res

documents = []
for category in product_reviews.categories():
    for fileid in product_reviews.fileids(category):
        documents.append([product_reviews.words(fileid),category])
documents.append([{'plot',':','good','movie'},'pos'])
documents.append([{'plot',':','not','good','movie'},'neg'])

random.shuffle(documents)

words = []
for word in product_reviews.words():
    if word not in stop_words:
        words.append(word.lower())

words_FD = nltk.FreqDist(words)

word_features = list(words_FD.keys())[:7000]
feature_sets = []
for (review,category) in documents:
    words = set([word for word in review if word not in stop_words and word not in stop2])
    # print("hello")
    features = {}

    for w in word_features:
        features[w] = w in words
    feature_sets.append([features,category])
#print(feature_sets[0])

train_set = feature_sets[:5000]
test_set = feature_sets[5000:]

clf = nltk.NaiveBayesClassifier.train(train_set)
nltk.classify.accuracy(clf,test_set)

#clf.show_most_informative_features(10)

while(True):
    print("Enter a sentence or Exit\n")
    review = input()
    if review == "Exit":
        break
    else:
        print("Prediction : ")
        prob = clf.prob_classify(extract(review.split()))
        pred = prob.max()

        print("Predicted Sentiment : " , pred)
        print("Probabilty : " , round(prob.prob(pred),2))
        print()
        

