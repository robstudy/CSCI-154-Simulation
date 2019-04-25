import random

#Project has two deck version
#Version 1: Infinite deck: On every run a card is drawn with equal probability.
#Version 2: Single deck: One deck of cards is used. The deck is reshuffled after every game.

#returns new deck of Version 2
def newDeck():
    return {'Ace': 4, 'Two': 4, 'Three': 4, 'Four': 4, 'Five': 4, 'Six':4, 'Seven':4, 'Eight':4,
         'Nine': 4, 'Ten': 4, 'J': 4, 'Q':4, 'K': 4}

deck = newDeck()

#Check if Deck is Empty
def isEmpty():
    """
    Check if Deck is Empty
    """
    for key, value in deck.items():
        if value > 0:
            return False
    return True


#draw cards from deck
def drawCardVersion2():
    """
    Draw Cards from a finite deck
    """
    card, numcards = random.choice(list(deck.items()))
    if numcards > 0:
        deck[card] -= 1
        return card
    elif not isEmpty():
        return drawCardVersion2()
    else:
        return 'Empty Deck'

# DEALER AND HELPER FUNCTIONS #
def shuffle():
    """
    Maximizes/restores the deck between games in finite mode.
    """

    global deck
    deck = newDeck()

def deal():
    """
    Shuffles then draws two cards from the deck, returns in a list.
    """

    shuffle()
    return [draw_card(),draw_card()]
