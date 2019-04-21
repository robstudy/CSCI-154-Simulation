#!/usr/bin/env python3

"""
    CSCI 154, Final Project:
    Blackjack Monte Carlo Simulation

    GROUP 2:
    Jheovanny Camacho, 109697217, jheoc@mail.fresnostate.edu
    Robert Garza,
    Robert Hovenesian,
"""

# needed for random number generator
import random

# global variables
deck = [4, 4, 4, 4, 4, 4, 4, 4, 4, 16]  # card deck, list index is face value, list value is card count (1 per suite)
finite = True  # if true, then finite deck, else it is an infinite deck


# DEALER AND HELPER FUNCTIONS #
def shuffle():
    """
    Maximizes/restores the deck between games in finite mode.
    """

    global deck
    deck = [4, 4, 4, 4, 4, 4, 4, 4, 4, 16]


def is_empty():
    """
    Checks if there are still cards to draw in finite mode.
    """

    # by default, it is considered empty
    val = True

    # checking every suite if any cards left (> 0)
    for x in deck:
        # if there are, set val to false
        if x > 0:
            val = False

    return val


def draw_card():
    """
    Draws a card, and if we're in finite mode it also removes the card from the deck.
    """

    global finite

    # randomly generate a number between 1-13 (includes ace, jack, queen, and king)
    num = random.randint(1, 13)
    # if over 10 (jack, queen, king), the face value is still 10
    num = 10 if num > 10 else num

    # for finite decks
    if finite:
        if deck[num - 1] > 0:
            deck[num - 1] = deck[num - 1] - 1
            return num if num is not 1 else 11
        elif not is_empty():
            return draw_card()
    else:
        return num if num is not 1 else 11


def deal():
    """
    Shuffles then draws two cards from the deck, returns in a list.
    """

    shuffle()
    return [draw_card(), draw_card()]


def check_softness(hand):
    """
    Sees if we have any ace in our hand that can be treated as a 1 or 11 without going over.
    Checks if the given hand is soft (ace is set to 11) or is hard (ace is set to 1).
    """

    # index flag
    index = -1

    # for each card in hand, if one has a value of 11, set index to that card
    for i in range(len(hand) - 1, 0 - 1, -1):
        if hand[i] == 11:
            index = i

    # if index changed then it's indeed soft, but if still -1 then it's hard/false
    is_soft = True if index is not -1 else False

    # return the softness value and the soft card
    return is_soft, index


def harden(hand, index):
    """
    Hardens the hand, turning the ace from an 11 to a 1.
    Uses index to see which card from the hand is the ace.
    """

    hand[index] = 1
    return hand


def harden_until(new_card, hand):
    """
    Takes in a value we want to add to the hand, and hardens the hand until the new card can be accepted, or you bust.
    These functions can be reused for any policy that cares about soft/hard hands.
    """

    # when adding a new card, if the new hand value is over 21
    if new_card + sum(hand) > 21:

        # check to see if it's still soft
        is_soft, index = check_softness(hand)

        # if it is, harden it
        if is_soft:
            return harden_until(new_card, harden(hand, index))

        # if the new card is 11, harden it
        elif new_card == 11:
            return harden_until(1, hand)

        # if it isn't soft then it's already hard, we can't do anything, we've lost dude
        else:
            hand.clear()
            return hand, False

    # otherwise, we add a new card and return the (successful) new hand
    else:
        hand.append(new_card)
        return hand, True


# POLICY FUNCTIONS #
def policy_1():
    """
    POLICY 1:
        If our hand ≥ 17, stick.
        Else, hit.
    """

    # first receive a hand
    hand = deal()

    # for each card in our hand
    for i in range(len(hand)):
        # automatically change to soft hand
        if hand[i] == 1:
            hand[i] = 11

    # follow policy
    return policy_1_r(hand)


def policy_1_r(hand):
    """
    Recursive function for Policy 1.
    """

    # if our hand is less than 17, we hit
    # otherwise, we do nothing, effectively sticking
    if sum(hand) < 17:
        new_card = draw_card()

        # as long as the deck isn't empty
        if new_card is not None:
            # new aces are automatically soft (does not turn hard later)
            if new_card == 1:
                new_card = 11

            # add the card to our hand
            hand.append(new_card)

            # follow policy again
            hand = policy_1_r(hand)

    # if our hand is greater than 21, we've bust (lost)
    if sum(hand) > 21:
        hand.clear()

    # return current hand
    return hand


def policy_2():
    """
    POLICY 2:
        If our hand ≥ 17, and hard, stick.
        Else, hit (unless our hand = 21).
    """

    # first receive a hand
    hand = deal()

    # for each card in our hand
    for i in range(len(hand)):
        # automatically change to soft hand
        if hand[i] == 1:
            hand[i] = 11

    # follow policy
    return policy_2_r(hand)


def policy_2_r(hand):
    """
    Recursive function for Policy 2.
    """

    # if our hand is 21 (Blackjack) we win/draw, return hand
    if sum(hand) == 21:
        return hand

    # if 17 or above
    if sum(hand) >= 17:

        # check softness of our hand
        is_soft, index = check_softness(hand)
        # if hard, return current hand (stick)
        if is_soft is not True:
            return hand

    # hit, if deck isn't empty and if card is ace, set to soft
    new_card = draw_card()
    if new_card is not None:
        if new_card == 1:
            new_card = 11

        # receive hardened hand
        hand, success = harden_until(new_card, hand)

        # if hardened hand is over 21, success is False, we've bust (lost)
        if success is not True:
            hand.clear()
            return hand

        # return current hand
        else:
            return policy_2_r(hand)


def policy_3():
    """
    POLICY 3:
        If our hand ≥ 17, and hard, stick.
        If our hand ≥ 17, and soft, stick 50% of the time.
        Else, hit (unless our hand = 21).
    """

    # first receive a hand
    hand = deal()

    # for each card in our hand
    for i in range(len(hand)):
        # automatically change to soft hand
        if hand[i] == 1:
            hand[i] = 11

    # follow policy
    return policy_3_r(hand)


def policy_3_r(hand):
    """
    Recursive function for Policy 3.
    """

    # if our hand is 21 (Blackjack) we win/draw, return hand
    if sum(hand) == 21:
        return hand

    # if 17 or above
    if sum(hand) >= 17:

        # check softness of our hand
        is_soft, index = check_softness(hand)
        # if hard, return current hand (stick)
        if is_soft is not True:
            return hand

        # ! HERE'S THE DIFFERENCE FROM POLICY 2 !
        # if we have a soft hand while above 17, we essentially flip a coin (50% chance)
        # if true then stick, otherwise we hit
        elif is_soft is True:
            if random.choice([True, False]) is True:
                return hand

    # hit, if deck isn't empty and if card is ace, set to soft
    new_card = draw_card()
    if new_card is not None:
        if new_card == 1:
            new_card = 11

        # receive hardened hand
        hand, success = harden_until(new_card, hand)

        # if hardened hand is over 21, success is False, we've bust (lost)
        if success is not True:
            hand.clear()
            return hand

        # return current hand
        else:
            return policy_3_r(hand)


def policy_4():
    """
    POLICY 4:
        Always stick.
    """

    # first receive a hand
    hand = deal()

    # for each card in our hand
    for i in range(len(hand)):
        # automatically change to soft hand
        if hand[i] == 1:
            hand[i] = 11

    if sum(hand) > 21:
        hand[0] = 1

    # return current hand
    return hand


def policy_5():  # based on policy 2
    """
    POLICY 5:
        If Dealer's exposed card is ace or above 7, follow Policy 2.
        Else, if Player's card is 12 or above and hard, stick.
        Else, hit.
    """

    # first receive a hand
    hand = deal()

    # for each card in our hand
    for i in range(len(hand)):
        # automatically change to soft hand
        if hand[i] == 1:
            hand[i] = 11

    # check dealer's exposed card, the player decides the policy based on that
    # if dealer got an ace or a card larger than 7, follow policy 2
    dealers_card = draw_card()
    if (dealers_card == 1) or (dealers_card > 7):
        return policy_2_r(hand), dealers_card
    # otherwise continue policy 5
    else:
        return policy_5_r(hand), dealers_card


def policy_5_r(hand):
    """
    Recursive function for Policy 5.
    """

    # if our hand is 21 (Blackjack) we win/draw, return hand
    if sum(hand) == 21:
        return hand

    # if 12 or above
    if sum(hand) >= 12:

        # check softness of our hand
        is_soft, index = check_softness(hand)
        # if hard, return current hand (stick)
        if is_soft is not True:
            return hand

    # hit, if deck isn't empty and if card is ace, set to soft
    new_card = draw_card()
    if new_card is not None:
        if new_card == 1:
            new_card = 11

        # receive hardened hand
        hand, success = harden_until(new_card, hand)

        # if hardened hand is over 21, success is False, we've bust (lost)
        if success is not True:
            hand.clear()
            return hand

        # return current hand
        else:
            return policy_5_r(hand)


def policy_6():  # based on policy 3
    """
    POLICY 6:
        If Dealer's exposed card is ace or above 7, follow Policy 3.
        Else, if Player's card 12 or above and hard, stick.
        Else, if Player's card 12 or above and soft, stick 50% chance of the time.
        Else, hit.
    """

    # first receive a hand
    hand = deal()

    # for each card in our hand
    for i in range(len(hand)):
        # automatically change to soft hand
        if hand[i] == 1:
            hand[i] = 11

    # check dealer's exposed card, the player decides the policy based on that
    # if dealer got an ace or a card larger than 7, follow policy 3
    dealers_card = draw_card()
    if (dealers_card == 1) or (dealers_card > 7):
        return policy_3_r(hand), dealers_card
    # otherwise continue policy 6
    else:
        return policy_6_r(hand), dealers_card


def policy_6_r(hand):
    """
    Recursive function for Policy 6.
    """

    # if our hand is 21 (Blackjack) we win/draw, return hand
    if sum(hand) == 21:
        return hand

    # if 12 or above
    if sum(hand) >= 12:

        # check softness of our hand
        is_soft, index = check_softness(hand)
        # if hard, return current hand (stick)
        if is_soft is not True:
            return hand
        # ! HERE'S THE DIFFERENCE FROM POLICY 5 !
        # if we have a soft hand while above 12, we essentially flip a coin (50% chance)
        # if true then stick, otherwise we hit
        elif is_soft is True:
            if random.choice([True, False]) is True:
                return hand

    # hit, if deck isn't empty and if card is ace, set to soft
    new_card = draw_card()
    if new_card is not None:
        if new_card == 1:
            new_card = 11

        # receive hardened hand
        hand, success = harden_until(new_card, hand)

        # if hardened hand is over 21, success is False, we've bust (lost)
        if success is not True:
            hand.clear()
            return hand

        # return current hand
        else:
            return policy_6_r(hand)


# checks each policy, uncommented one is the one being checked (in this case, policy 6)
for i in range(25):
    # player's turn

    # hand, dealers_card = policy_1(), draw_card()
    # hand, dealers_card = policy_2(), draw_card()
    # hand, dealers_card = policy_3(), draw_card()
    # hand, dealers_card = policy_4(), draw_card()
    # hand, dealers_card = policy_5()
    hand, dealers_card = policy_6()

    # dealer goes after the player and follows policy 1
    dealers_hand = policy_1_r([dealers_card, draw_card()])

    # outputs the results, contains:
    # player's hand and sum,
    # dealer's hand and sum,
    # message on if the player wins or loses
    print(hand, "	", sum(hand), "		", dealers_hand, "	", sum(dealers_hand), "		",
          "Player Wins!" if sum(hand) > sum(dealers_hand) else "Player loses. . .")

# this just shows how many of each card type is left in the deck, if finite
if finite:
    for i in range(10):
        print(i + 1, "s:	", deck[i])
