import nltk
import random
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.classify import maxent

#print(movie_reviews.categories())

stop_words = stopwords.words('english')
stop2 = ['.',',','&','(','?','!',')']

def extract(words):
    res = dict([(word,True) for word in words])
    #print(res)
    return res

documents = []
for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        documents.append([movie_reviews.words(fileid),category])
documents.append([{'plot',':','good','movie'},'pos'])
documents.append([{'plot',':','not','good','movie'},'neg'])
#print(len(documents))
#print(documents[0])

#documents[1200]
random.shuffle(documents)

#print(movie_reviews.words())

words = []
for word in movie_reviews.words():
    if word not in stop_words:
        words.append(word.lower())

words_FD = nltk.FreqDist(words)

#print(words_FD.most_common(10))
#print(len(words))

#print(words_FD['good'])

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

encoding = maxent.TypedMaxentFeatureEncoding.train(train_set, count_cutoff=3, alwayson_features=True)
clf = maxent.MaxentClassifier.train(train_set, bernoulli=False, encoding=encoding, trace=0)
clf.classify_many(test_set)

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
        

