from nltk.tokenize import word_tokenize

def gtTokenizedFileData(file):
    return word_tokenize(open(file,"r").read())
	
def process(data):
    return [word.lower() for word in data];

words = input("Meaningless Text:\n")
words = process(word_tokenize(words))
	
blocked_Words = gtTokenizedFileData("blocked_Words.txt")
print("You get These meaningful words:")
	
for word in words:
    if word not in blocked_Words:
        print(word)
