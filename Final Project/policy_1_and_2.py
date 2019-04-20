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

def policy_1():
	hand=deal()
	for i in range(len(hand)):
		if hand[i]==1:
			hand[i]=11
#	print(hand,end="	")
	return policy_1_r(hand)

def policy_1_r(hand):
	if sum(hand) < 17:
		new_card=draw_card()
		if new_card is not None:
			if new_card==1:
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
#	print(hand,end="	")
	return policy_2_r(hand)

def policy_2_r(hand):
	if sum(hand) >= 17:
		is_soft,index=check_softness(hand)
		if is_soft is not True:
			return hand

	if sum(hand) == 21:
		return hand

	new_card=draw_card()
	if new_card==1:
		new_card=11
	hand,success=harden_until(new_card,hand)
	if success is not True:
		hand.clear()
		return hand
	else:
		return policy_2_r(hand)

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

def deal():
	shuffle()
	return [draw_card(),draw_card()]


for i in range(25):
#	a=policy_1()
	a=policy_2()
	print(a,"	",sum(a))

for i in range(10):
	print(i+1,"s:	",deck[i])


