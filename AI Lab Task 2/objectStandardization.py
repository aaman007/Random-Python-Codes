from nltk.tokenize import word_tokenize

def lowerCaseMaker(words):
	return [word.lower() for word in words]
def getTokenizedFile(data):
	return lowerCaseMaker(word_tokenize(data))
	
def getData(file):
	return open(file,"r").readlines()
	
def process(words):
	words = [word[:-1] for word in words]
	return[word.lower() for word in words]

mapped_data = {"hlw":"hello"}
def constructMappedData(keys,values):
	for i in range(0,len(keys)):
		mapped_data[keys[i]] = values[i]
	
keys = process(getData("shortform.txt"))
values = process(getData("shortform_meaning.txt"))
constructMappedData(keys,values)

while(True):
	s = input("Enter your sentence or type Exit::\n")
	if s == "Exit":
		break;
	words = getTokenizedFile(s)
	temp = []
	for word in words:
		if word in mapped_data:
			temp.append(mapped_data[word])
		else:
			temp.append(word)
	print("Standard Form: ")	
	print(" ".join(temp))
	print("")
	
