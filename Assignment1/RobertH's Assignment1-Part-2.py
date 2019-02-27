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
				self.words.extend(newWords)#and append all of its elements to the end of the class's words.
		#print(self.words)#Prints the list, for debugging purposes.

	def scramble_it(self):
		returnString=""#This will contain the string that will be returned.
		for w in self.words:#For all the words that we have
			returnString+=" "
			endIndex=-1#The index of the character we consider to be the index after the middle of the word.
			for i in range(len(w)-1,0,-1):#For loop, starting from the end of the word going until the beginning.
				if w[i]=="!" or w[i]=="," or w[i]=="." or w[i]=="?" or w[i]=="'" or w[i]=='"':#If we find one of these characters
					endIndex=i-1#update the end index. So "That's" should consider the second 't' the start of the end, the t's won't be shuffled.
			newWord=list(w[1:endIndex])#Grab the middle of the current word. If the word is two character or less, this and the next line will just shuffle an empty list.
			shuffle(newWord)#Shuffle just the middle
			newWord.insert(0,w[0])#Add the first character of the word back to it at the front.
			if len(w)>1:#If the word is more than one character, that is to say if it has a last character that is different from the first.
				newWord.append(w[endIndex:])#add the last character back to it at the end.
			returnString+=''.join(newWord)#Convert the newWord from a list to a string, and concatenate it with the returnString.
		returnString=returnString[1:]#Slice off the leading space.
		return returnString#return the string.



scramble1 = Scrambler()
print(scramble1.scramble_it())
