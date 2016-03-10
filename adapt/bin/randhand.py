#!/usr/bin/env python


# Python program to shuffle a deck of card using the module random and draw 5 cards

# import modules
import itertools, random
import sys

# make a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

# shuffle the cards
random.shuffle(deck)

suit = 'AKQJT98765432'

def xlate(n):
    return suit[n-1]

suitabbrev = {}
suitabbrev['Club'] = 'c'
suitabbrev['Diamond'] = 'd'
suitabbrev['Heart'] = 'h'
suitabbrev['Spade'] = 's'

hand = deck[1:14]

def valof(s):
    vals = {'A' : 0,
            'K' : 1,
            'Q' : 2,
            'J' : 3,
            'T' : 4,
            '9' : 5,
            '8' : 6,
            '7' : 7,
            '6' : 8,
            '5' : 9,
            '4' : 10,
            '3' : 11,
            '2' : 12}
    return vals[s]

hval = { 'A' : 4,
         'K' : 3,
         'Q' : 2,
         'J' : 1,
         'T' : 0,
         '9' : 0,
         '8' : 0,
         '7' : 0,
         '6' : 0,
         '5' : 0,
         '4' : 0,
         '3' : 0,
         '2' : 0}



def handvalue(hand):
    hv = 0
    for i in range(len(hand)):
        hv += hval[hand[i]]

    return hv
#print hand

xhand = []
for s in ['Club', 'Diamond', 'Heart', 'Spade']:
    thissuit = []
    for i in range(13):
        if hand[i][1] == s:
            thissuit.append(xlate(hand[i][0]))
    
    print '%s: ' % suitabbrev[s],
    if len(thissuit) == 0:
        sys.stdout.write('void')
    else:
        for thing in sorted(thissuit,key=valof):
            sys.stdout.write(thing)
    print
    xhand += thissuit


if False: # handvalue(xhand) < 10:
    print '-----------pass----------------'
else:    
    print
    print "q: opening"
    print

    print "a: ??"



