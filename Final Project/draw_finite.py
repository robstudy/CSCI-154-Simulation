#!/usr/bin/env python3
import random

#deck=[0,0,0,0,0,0,0,0,0,0]
deck=[4,4,4,4,4,4,4,4,4,16]

def isEmpty():
    val=True
    for x in deck:
        if x > 0:
            val=False
    return val

def drawCard():
    num=random.randint(1,13)
    num=10 if num > 10 else num
    if deck[num-1] > 0:
        deck[num-1]=deck[num-1]-1
        return num
    elif not isEmpty():
        return drawCard()

for i in range(100):
    print(drawCard())

for i in deck:
    print("d",i)
