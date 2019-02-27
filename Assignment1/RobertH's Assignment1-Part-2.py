# Assignment 1
# Part 3
# Robert Garza, Jheovanny Camacho, Robert Hovanesian
# 03-05-2019

from random import shuffle

class Scrambler:
	def __init__(self):
		self.words=list()
		condition=True
		while condition:
			newLine=str(input("Type a line to scramble: "))
			newWords=newLine.split()
			if not newWords:
				condition=False
			else:
				correctedWords=list()
				newWords.reverse()
				i=0
				limit=len(newWords)
				while(i<limit):
					if newWords[i][-1]=="!" or newWords[i][-1]=="," or newWords[i][-1]=="." or newWords[i][-1]=="?":
						correctedWords.append(newWords[i][-1])
						newWords[i]=newWords[i][0:-1]
						i-=1
					else:
						correctedWords.append(newWords[i])
					i+=1
						
				self.words.extend(correctedWords)

		self.words.reverse()
		print(self.words)

	def scramble_it(self):
		returnList=""
		for w in self.words:
			if w!="!" and w!="," and w!="." and w!="?":
				returnList+=" "
			newWord=list(w[1:-1])
			shuffle(newWord)
			newWord.insert(0,w[0])
			if len(w)>1:
				newWord.append(w[-1])
			returnList+=''.join(newWord)
		if(len(returnList)>1 and returnList[0]==" "):
			returnList=returnList[1:]
		return returnList


scramble1 = Scrambler()
print(scramble1.scramble_it())
