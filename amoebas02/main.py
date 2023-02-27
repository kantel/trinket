from processing import *
from random import randint, uniform

WIDTH, HEIGHT = 640, 480
MIN_DIA = 30
MIN_DIA2 = MIN_DIA//2
MAX_DIA = 120
MAX_DIA2  = MAX_DIA//2
FPS = 120

class Amoeba():
  
  def __init__(self, _x, _y, _diameter):
    self.x = _x
    self.y = _y
    self.d = _diameter
    self.nucleus = {
      "fill": [color(54, 50, 80), color(160, 51, 46), color(180, 144, 55),
               color(140, 82, 48), color(215, 158, 40)][int(randint(0, 4))],
      "x": self.d*uniform(-0.15, 0.15),
      "y": self.d*uniform(-0.15, 0.15),
      "d": self.d/uniform(2.5, 4)
    }
  
  def circle_point(self, t, r):
    x = cos(t)*r
    y = sin(t)*r
    return([x, y])
    
  def display(self):
    # Cell Nucleus
    fill(self.nucleus["fill"])
    noStroke()
    ellipse(self.x + self.nucleus["x"], self.y + self.nucleus["y"],
            self.nucleus["d"], self.nucleus["d"])
    # Cell Membrane
    # fill(0x880099AA)
    fill(230, 226, 204, 80)
    # stroke("#FFFFFF")
    stroke(255, 255, 255)
    strokeWeight(3)
    r = self.d/2.0
    # print("r = ", r/8)
    cpl = r*.55
    cpx, cpy = self.circle_point(frameCount*.15, r/4)
    xp, xm = self.x + cpx, self.x - cpx
    yp, ym = self.y + cpy, self.y - cpy
    beginShape()
    vertex(self.x, self.y - r)   # top vertex
    bezierVertex(xp + cpl, yp - r, xm + r, ym - cpl,
                 self.x + r, self.y)   # right vertex
    bezierVertex(xp + r, yp + cpl, xm + cpl, ym + r,
                 self.x, self.y + r)   # bottom vertex
    bezierVertex(xp - cpl, yp + r, xm - r, ym + cpl,
                 self.x - r, self.y)   # left vertex
    bezierVertex(xp - r, yp - cpl, xm - cpl, ym - r,
                 self.x, self.y - r)   # top vertex
    endShape()

amoebas = []

def setup():
  size(WIDTH, HEIGHT)
  for _ in range(10):
    amoeba = Amoeba(randint(MAX_DIA2, width - MAX_DIA2),
                    randint(MAX_DIA2, height - MAX_DIA2),
                    randint(MIN_DIA, MAX_DIA))
    amoebas.append(amoeba)
  frameRate(FPS)
  
def draw():
  background(50, 80, 105)
  for amoeba in amoebas:
    amoeba.display()

print("I did it, Babe!")    
run()
