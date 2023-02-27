from processing import *
from random import randint

WIDTH, HEIGHT = 640, 416
N_FISHES = 15

class Background():
  
  def __init__(self, _img):
    self.img = loadImage(_img)
    
  def display(self):
    image(self.img, 0, 0)

class Fish():
  
  def __init__(self, _idx, _x, _y, _dir, _speed):
    self.imgr0 = loadImage("fish" + str(_idx) + "r_0.png")
    self.imgl0 = loadImage("fish" + str(_idx) + "l_0.png")
    self.imgr1 = loadImage("fish" + str(_idx) + "r_1.png")
    self.imgl1 = loadImage("fish" + str(_idx) + "l_1.png")
    self.x = _x
    self.y = _y
    self.dir = _dir
    if self.dir == "rt":
      self.img = self.imgr0
    elif self.dir == "lt":
      self.img = self.imgl0
    self.speed = _speed*randint(1, 3)
    self.switch = 5
    self.timer = self.switch
    
  def update(self):
    self.x += self.speed
    if self.timer <= 0:
      self.timer = self.switch
      if self.img == self.imgr0:
        self.img = self.imgr1
      elif self.img == self.imgr1:
        self.img = self.imgr0
      elif self.img == self.imgl0:
        self.img = self.imgl1
      elif self.img == self.imgl1:
        self.img = self.imgl0
    if self.x > width + randint(40, 200):
      self.img = self.imgl0
      self.y = randint(20, 300)
      self.speed = randint(-3, -1)
    if self.x < randint(-200, -40):
      self.img = self.imgr0
      self.y = randint(20, 300)
      self.speed = randint(1, 3)
    self.timer -= 1
 
  def display(self):
    image(self.img, self.x, self.y)

fishes = []

def setup():
  global bg
  size(WIDTH, HEIGHT)
  print("🐠 Jörgs kleines, bonbonbuntes Aquarium 🐡")
  bg = Background("background.png")
  for _ in range(N_FISHES):
    direction = randint(0, 1)
    if direction == 0:
      dr = "rt"
      speed = 1
    else:
      dr = "lt"
      speed = -1
    x = randint(-100, width + 200)
    y = randint(20, 300)
    fish = Fish(randint(1, 7), x, y, dr, speed)
    fishes.append(fish)

def draw():
  background(49, 197, 244) # Hellblau
  bg.display()
  for fish in fishes:
    fish.update()
    fish.display()

run()