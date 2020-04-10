import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import RegexpTokenizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
from sklearn.feature_extraction.text import TfidfVectorizer

data = pd.read_csv('train.tsv',sep='\t')
#print(data.head())
#print(data.info())
#print(data.Sentiment.value_counts())

Sentiment_count = data.groupby('Sentiment').count()
#plt.bar(Sentiment_count.index.values, Sentiment_count['Phrase'])

#tokenizer to remove unwanted elements from out data like symbols and numbers
token = RegexpTokenizer(r'[a-zA-Z0-9]+')
cv = CountVectorizer(lowercase=True,stop_words='english',ngram_range = (1,1),tokenizer = token.tokenize)
text_counts= cv.fit_transform(data['Phrase'])

X_train, X_test, y_train, y_test = train_test_split(text_counts, data['Sentiment'], test_size=0.3, random_state=1)

# Model Generation Using Multinomial Naive Bayes
clf = MultinomialNB().fit(X_train, y_train)
predicted= clf.predict(X_test)
#print(X_test)
print("MultinomialNB Accuracy:",metrics.accuracy_score(y_test, predicted))

'''
tf=TfidfVectorizer()
text_tf= tf.fit_transform(data['Phrase'])
X_train, X_test, y_train, y_test = train_test_split(text_tf, data['Sentiment'], test_size=0.3, random_state=123)

# Model Generation Using Multinomial Naive Bayes
clf = MultinomialNB().fit(X_train, y_train)
predicted= clf.predict(X_test)
print("MultinomialNB Accuracy:",metrics.accuracy_score(y_test, predicted)) 
'''

while(True):
    print("Enter a sentence or Exit\n")
    review = input()
    if review == "Exit":
        break
    else:
        print("Prediction : ")
        print("Predicted Sentiment : " , clf.predict(review))
        print()
