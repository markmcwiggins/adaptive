#!/usr/bin/python

top = ['q','j','10','9','8','7','6','5','4','3','2']
suits = ['clubs','spades','hearts','diamonds']

suit = 0
topn = 0
for i in range(9,53):
    print 'ln -s %d.png %s%s.png' % (i,top[topn],suits[suit])
    suit += 1
    if suit > 3:
        suit = 0
        topn += 1

