from processing import *

WIDTH, HEIGHT = 720, 520
BG_WIDTH = 1664
FPS = 60
ANIM = 4   # Animation Cycle
UPDOWN = 3

class Background():
  
  def __init__(self, _x, _y):
    self.x = _x
    self.y = _y
    self.start_x = _x
    self.img = loadImage("desert.png")
    
  def update(self):
    self.x -= 1
    if self.x <= -BG_WIDTH:
      self.x = BG_WIDTH
  
  def display(self):
    image(self.img, self.x, self.y)

class Plane():
  
  def __init__(self):
    self.images = []
    for i in range(2):
      img = loadImage("planegreen_" + str(i) + ".png")
      self.images.append(img)
    self.img = self.images[0]
    self.x = 75
    self.y = 240
    self.dir = "NONE"
    self.frame = 0
    self.ani = 20
  
  def update(self):
    if self.dir == "NONE":
      self.y += 0
    elif self.dir == "UP":
      if self.y > 20:
        self.y -= UPDOWN
    elif self.dir == "DOWN":
      if self.y < height - 40:
        self.y += UPDOWN
    self.ani += 1
    if self.ani >= ANIM:
      self.ani = 0
      self.frame += 1
      if self.frame > 1:
        self.frame = 0
    self.img = self.images[self.frame]
      
  def display(self):
    image(self.img, self.x, self.y)
    
# Arrays
backs = []
    
def setup():
  global plane
  size(WIDTH, HEIGHT)
  frameRate(FPS)
  print("🍕 Pizza Plane Stage 2 🍕")
  print("Linke Maustaste: Flieger fliegt nach oben.")
  print("Rechte Maustaste: Flieger fliegt nach unten.")
  plane = Plane()
  back1 = Background(0, 0)
  back2 = Background(BG_WIDTH, 0)
  backs.append(back1)
  backs.append(back2)
  
def draw():
  background(231, 229, 226)   # Wüstenhimmel
  for back in backs:
    back.update()
    back.display()
  plane.update()
  plane.display()
  
def mousePressed():
  if mouseButton == LEFT:
    plane.dir = "UP"
  elif mouseButton == RIGHT:
    plane.dir = "DOWN"

def mouseReleased():
  plane.dir = "NONE"

run()