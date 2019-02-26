# Assignment 1
# Part 2
# Robert Garza, Jheovanny Camacho, Robert Hovanesian
# 03-05-2019

from random import shuffle


class Scrambler:
    def __init__(self, paragraph):
        self.paragraph = paragraph

    def scramble_it(self):
        # initialize paragraph list
        new_paragraph_list = []
        words = self.paragraph

        # for every word (element) in the paragraph
        for word in words:

            # middle is the characters between first and last characters
            middle = list(word[1:-1])
            # shuffle function from random module will shuffle middle
            shuffle(middle)
            # new string consisting of shuffled middle
            shuffled_innards = ''.join(middle)

            # new word consists of original first, shuffled middle, and original last element
            new_word = word[0] + shuffled_innards + word[-1]
            # add each new word to the paragraph list, forming a new sentence
            new_paragraph_list.append(new_word)

        # convert paragraph list to a string, separating words with a space
        new_paragraph_string = ' '.join(new_paragraph_list)

        return new_paragraph_string


user_paragraph = input('Please enter one sentence at a time: ').split()

scramble = Scrambler(user_paragraph)
print(scramble.scramble_it())

