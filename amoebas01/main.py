from processing import *
from random import randint, uniform

WIDTH, HEIGHT = 600, 600
MIN_DIA = 50
MIN_DIA2 = MIN_DIA//2
MAX_DIA = 150
MAX_DIA2  = MAX_DIA//2

class Amoeba():
  
  def __init__(self, _x, _y, _diameter):
    self.x = _x
    self.y = _y
    self.d = _diameter
    self.nucleus = {
      "fill": ["#FF0000", "#FF9900", "#FF00FF",
               "#00FF00", "#0099FF"][int(randint(0, 4))],
      "x": self.d*uniform(-0.15, 0.15),
      "y": self.d*uniform(-0.15, 0.15),
      "d": self.d/uniform(2.5, 4)
    }
    
  def display(self):
    # Cell Nucleus
    fill(self.nucleus["fill"])
    noStroke()
    ellipse(self.x + self.nucleus["x"], self.y + self.nucleus["y"],
            self.nucleus["d"], self.nucleus["d"])
    # Cell Membrane
    fill(0x880099AA)
    stroke("#FFFFFF")
    strokeWeight(3)
    ellipse(self.x, self.y, self.d, self.d)

amoebas = []

def setup():
  size(WIDTH, HEIGHT)
  for _ in range(15):
    amoeba = Amoeba(randint(MAX_DIA2, width - MAX_DIA2),
                    randint(MAX_DIA2, height - MAX_DIA2),
                    randint(MIN_DIA, MAX_DIA))
    amoebas.append(amoeba)
  
def draw():
  background("#004477")
  for amoeba in amoebas:
    amoeba.display()

print("I did it, Babe!")    
run()
