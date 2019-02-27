#!/usr/bin/env python3
# Assignment 1
# Part 3
# Robert Garza, Jheovanny Camacho, Robert Hovanesian
# 03-05-2019
from random import shuffle

class Scrambler:
	def __init__(self):
		self.words=list()#The list that will contain all the sentences.
		while True:#Looping while there is input, exit condition is below.
			newLine=str(input("Type a line to scramble: "))#Ask for input
			if not newLine:#If there is no lines of input left, then break.
				break
			else:
				newWords=newLine.split()#Otherwise split up each line into a list of words,
				newWords.reverse()#in reverse order.
				correctedWords=list()#This will contain the words we will push into the final result.
				i=0
				while(i<len(newWords)):#Iterating over all the words in the list.
					if newWords[i][-1]=="!" or newWords[i][-1]=="," or newWords[i][-1]=="." or newWords[i][-1]=="?":#If the current word ends in a punctuating character
						correctedWords.append(newWords[i][-1])#we add it to the tail of the list, which is really the head in reverse order
						newWords[i]=newWords[i][:-1]#we slice off the punctuating character from the word
						i-=1#we decrement i by one because we want to redo this iteration of the loop, with the same word shortened.
					else:#If there were no special characters at the end
						correctedWords.append(newWords[i])#Just add it to the tail of the list.
					i+=1#Increment the loop.

				correctedWords.reverse()#Reverse the list of corrected words
				self.words.extend(correctedWords)#and append all of its elements to the end of the class's words.
		#print(self.words)#Prints the list, for debugging purposes.

	def scramble_it(self):
		returnString=""#This will contain the string that will be returned.
		for w in self.words:#For all the words that we have
			if w!="!" and w!="," and w!="." and w!="?":#If the word isn't a single punctuating character
				returnString+=" "#Add a space before it. We will remove the extra leading space caused by this at the end.
			newWord=list(w[1:-1])#Grab the middle of the current word. If the word is two character or less, this and the next line will just shuffle an empty list.
			shuffle(newWord)#Shuffle just the middle
			newWord.insert(0,w[0])#Add the first character of the word back to it at the front.
			if len(w)>1:#If the word is more than one character, that is to say if it has a last character that is different from the first.
				newWord.append(w[-1])#add the last character back to it at the end.
			returnString+=''.join(newWord)#Convert the newWord from a list to a string, and concatenate it with the returnString.
		if(len(returnString)>1 and returnString[0]==" "):#If there is at least one word and it contains a leading space
			returnString=returnString[1:]#slice off the leading space.
		return returnString#return the space.



scramble1 = Scrambler()
print(scramble1.scramble_it())
