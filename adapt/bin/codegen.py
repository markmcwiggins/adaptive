#!/usr/bin/python

import sys

datfyle = sys.argv[1]
html = sys.argv[2]

f = open(datfyle)
fh = open(html,'w')

hand = {}
cardstr = {
    'A' : 'ace',
    'K' : 'k',
    'Q' : 'q',
    'J' : 'j',
    'T' : '10',
    '9' : '9',
    '8' : '8',
    '7' : '7',
    '6' : '6',
    '5' : '5',
    '4' : '4',
    '3' : '3',
    '2' : '2' }
    

suitlist = ['c:','d:','h:','s:']
suitnames = { 'c:' : 'clubs',
              'd:' : 'diamonds',
              'h:' : 'hearts',
              's:' : 'spades',
              'n:' : 'no trump'}


qexpand = {'opening' : 'What is your opening bid with this hand?',
           'yourbid?' : 'What is your bid now?',
           'bid:' : 'The bidding so far'}

capital = { 'c' : 'Clubs',
            'd' : 'Diamonds',
            'h' : 'Hearts',
            's' : 'Spades',
            'n' : 'NT'}

def expandans(a):
    if a == '??':
        return a
    n = a[0]
    s = a[1]
    return '%s,%s' % (n,capital[s])
    

def expandbid(b):
    suit = suitnames[b[1] + ':']
    return '%d %s' % (int(b[0]),suit)

previousbids = False
def dobids(bids):
    fh.write('<br><h2>The bidding so far:<br>')
    flipflop = True
    for b in bids:
        if flipflop:
            fh.write("Opener: ")
        else:
            fh.write('Responder: ')
        fh.write(expandbid(b))
        flipflop = not flipflop
        fh.write('<br>\n')
    skip = f.readline()
    fh.write('</h2><H1>What is your bid now?</H1><br>\n')
    skip = f.readline()


n = 0
while True:
    line = f.readline()
    (suit ,cards) = line.rstrip().split()
    if cards == 'void':
        cards = []
    hand[suit] = list(cards)
    n += 1
    if n == 4:
        break

skip = f.readline()  # expected blank line

line = f.readline()
try:
    (q,heading) = line.rstrip().split()
    if qexpand.get(heading):
        question = qexpand[heading]
    else:
        question = heading
except:
    heading = line.rstrip()
    question = heading
    pass

if heading == 'bid:':
    line = f.readline()
    bids = line.strip().split(',')
    print bids
    previousbids = True


skip = f.readline()
line = f.readline()
(a,ans) = line.rstrip().split()
answer = ans
explanation = ''
try:
    exline = f.readline()
    words = exline.rstrip().split(':')
    print words
    explanation = ' '.join(words[1:]).rstrip()
except:
    print 'nope no explanation'
    pass

fh.write('''
{% extends 'bridgehand.html' %}
{% block 'body' %}
''')
#fh.write(question + '<br>\n')
for s in suitlist:
    for c in hand[s]:
        card = '%s%s.png' % (cardstr[c],suitnames[s])
        fh.write('<img src="/static/cards/%s">\n' % card)
    fh.write('<br>\n')

if previousbids:
    dobids(bids)
    question = ''

fh.write('<br><br><h1>%s</h1><br><br>\n<form action="answer_proc/" method="POST">\n' % question)
for amp in range(7):
    xamp = amp + 1
    fh.write('<input type="radio" value="%d" name="amp">%d</input>\n' % (xamp,xamp))
fh.write('<br>\n')
for suit in ['Spades', 'Hearts', 'Diamonds', 'Clubs', 'NT']:
    fh.write('<input type="radio" value="%s" name="suit">%s</input>\n' % (suit,suit))
fh.write('<br>\n')
fh.write('''
 {% csrf_token %}''')
fh.write('''
<input type="hidden" value="%s" name="ra"/>
''' % expandans(answer))
if explanation:
    fh.write('<input type="hidden" value="%s" name="explanation"/>' % explanation)
fh.write('<input type="submit">\n{% endblock %}')
fh.close()


