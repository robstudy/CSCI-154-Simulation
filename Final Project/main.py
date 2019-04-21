#!/usr/bin/env python3
import random

#deck=[0,0,0,0,0,0,0,0,0,0]
deck=[4,4,4,4,4,4,4,4,4,16]
finite=True

def shuffle():
	global deck
	deck=[4,4,4,4,4,4,4,4,4,16]

def is_empty():
	val=True
	for x in deck:
		if x > 0:
			val=False
	return val

def draw_card():
	global finite
	num=random.randint(1,13)
	num=10 if num > 10 else num
	if finite:
		if deck[num-1] > 0:
			deck[num-1]=deck[num-1]-1
			return num
		elif not is_empty():
			return draw_card()
	else:
		return num

def deal():
	shuffle()
	return [draw_card(),draw_card()]

def policy_1():
	hand=deal()
	for i in range(len(hand)):
		if hand[i]==1:
			hand[i]=11
	return policy_1_r(hand)

def policy_1_r(hand):
	if sum(hand) < 17:
		new_card=draw_card()
		if new_card is not None:
			if(new_card==1):
				new_card=11
			hand.append(new_card)
			hand=policy_1_r(hand)
	if sum(hand) > 21:
		hand.clear()
	return hand

def policy_2():
	hand=deal()
	for i in range(len(hand)):
		if hand[i]==1:
			hand[i]=11
	return policy_2_r(hand)

def policy_2_r(hand):
	if sum(hand) == 21:
		return hand

	if sum(hand) >= 17:
		is_soft,index=check_softness(hand)
		if is_soft is not True:
			return hand

	new_card=draw_card()
	if new_card is not None:
		if new_card==1:
			new_card=11
		hand,success=harden_until(new_card,hand)
		if success is not True:
			hand.clear()
			return hand
		else:
			return policy_2_r(hand)

def policy_3():
	hand=deal()
	for i in range(len(hand)):
		if hand[i]==1:
			hand[i]=11
	return policy_3_r(hand)

def policy_3_r(hand):
	if sum(hand) == 21:
		return hand

	if sum(hand) >= 17:
		is_soft,index=check_softness(hand)
		if is_soft is not True:
			return hand
		elif is_soft is True:
			if random.choice([True, False]) is True:
				return hand

	new_card=draw_card()
	if new_card is not None:
		if new_card==1:
			new_card=11
		hand,success=harden_until(new_card,hand)
		if success is not True:
			hand.clear()
			return hand
		else:
			return policy_3_r(hand)

def policy_4():
	hand=deal()
	for i in range(len(hand)):
		if hand[i]==1:
			hand[i]=11
	if sum(hand) > 21:
		hand[0]=1
	return hand

def policy_5():#Based on policy 2
	hand=deal()
	for i in range(len(hand)):
		if hand[i]==1:
			hand[i]=11
	dealers_card=draw_card()
	if (dealers_card == 1) or (dealers_card > 7):
		return policy_2_r(hand),dealers_card
	else:
		return policy_5_r(hand),dealers_card

def policy_5_r(hand):
	if sum(hand) == 21:
		return hand

	if sum(hand) >= 12:
		is_soft,index=check_softness(hand)
		if is_soft is not True:
			return hand

	new_card=draw_card()
	if new_card is not None:
		if new_card==1:
			new_card=11
		hand,success=harden_until(new_card,hand)
		if success is not True:
			hand.clear()
			return hand
		else:
			return policy_5_r(hand)

def policy_6():#Based on policy 3
	hand=deal()
	for i in range(len(hand)):
		if hand[i]==1:
			hand[i]=11
	dealers_card=draw_card()
	if (dealers_card == 1) or (dealers_card > 7):
		return policy_3_r(hand),dealers_card
	else:
		return policy_6_r(hand),dealers_card

def policy_6_r(hand):
	if sum(hand) == 21:
		return hand

	if sum(hand) >= 12:
		is_soft,index=check_softness(hand)
		if is_soft is not True:
			return hand
		elif is_soft is True:
			if random.choice([True, False]) is True:
				return hand

	new_card=draw_card()
	if new_card is not None:
		if new_card==1:
			new_card=11
		hand,success=harden_until(new_card,hand)
		if success is not True:
			hand.clear()
			return hand
		else:
			return policy_6_r(hand)

def check_softness(hand):
	index=-1
	for i in range(len(hand)-1,0-1,-1):
		if hand[i]==11:
			index=i
	is_soft=True if index is not -1 else False
	return is_soft,index

def harden(hand,index):
	hand[index]=1
	return hand

def harden_until(new_card,hand):
	if new_card + sum(hand) > 21:
		is_soft,index=check_softness(hand)
		if is_soft:
			return harden_until(new_card,harden(hand,index))
		elif new_card == 11:
			return harden_until(1,hand)
		else:
			hand.clear()
			return hand,False
	else:
		hand.append(new_card)
		return hand,True



for i in range(25):
#	hand,dealers_card=policy_1(),draw_card()
#	hand,dealers_card=policy_2(),draw_card()
#	hand,dealers_card=policy_3(),draw_card()
#	hand,dealers_card=policy_4(),draw_card()
#	hand,dealers_card=policy_5()
	hand,dealers_card=policy_6()

	dealers_hand=[dealers_card,draw_card()]
	dealers_hand=policy_1_r([dealers_card,draw_card()])

	print(hand,"	",sum(hand),"		",dealers_hand,"	",sum(dealers_hand),"		","Player Wins!" if sum(hand) > sum(dealers_hand) else "Player loses. . .")


if finite:
	for i in range(10):
		print(i+1,"s:	",deck[i])#This just shows how many of each card type is left in the deck, if finitee.
