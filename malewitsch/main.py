# Map Art: Hommage an Kasimir Malewitsch
# Author: Jörg Kantel
from processing import *
from random import randint

WIDTH, HEIGHT = 600, 400
lmargin = 40   # unterer Rand und Rand links
umargin = 100  # oberer Rand und Rand rechts
nIter   = 30   # Anzahl der Shapes
a       = 100  # Transparenz


def drawRect():
    x = randint(lmargin, width - umargin)
    y = randint(lmargin, height - umargin)
    w = randint(lmargin, umargin)
    h = randint(lmargin, umargin)
    rect(x, y, w, h)

def drawCircle():
    x = randint(lmargin, width - umargin)
    y = randint(lmargin, height - umargin)
    r = randint(15, 50)
    ellipse(x, y, r, r)

def setup():
    size(WIDTH, HEIGHT)
    background(230, 226, 204)
    malewitsch1 = [color(42, 40, 45),
               color(160, 51, 46),
               color(54, 50, 80),
               color(50, 80, 105),
               color(180, 144, 55),
               color(215, 158, 40),
               color(140, 82, 48)]
    for _ in range(nIter):
        rand = randint(0, 100)
        if rand < 30:
            stroke(0)
            strokeWeight(1)
            fill(malewitsch1[randint(0, 1)])
            if randint(0, 100) > 50:
                drawRect()
            else:
                drawCircle()
        elif rand < 85:
            fill(malewitsch1[randint(2, 5)])
            drawRect()
        else:
            stroke(malewitsch1[6])
            strokeWeight(7)
            noFill()
            drawCircle()
            stroke(0)
            strokeWeight(1)
    print("I did it, Babe!")
    
run()