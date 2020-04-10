from nltk.tokenize import word_tokenize

def getTokenizedFile(file):
	return word_tokenize(open(file,"r").read())
	
def process(data):
	return [word.lower() for word in data];

while(True):
	s = input("Enter your sentence or enter Exit:\n")
	s = process(word_tokenize(s))
	
	stopWords = getTokenizedFile("stopWords.txt")
	print("Meaningful words are :")
	
	cnt = 1
	for word in s:
		if word in stopWords:
			continue
		else:
			print(str(cnt)+". "+word)
			cnt = cnt+1
	print()
