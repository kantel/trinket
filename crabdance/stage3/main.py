# Dancing Crab
# Jörg Kantel 2023
# Inspiriert von Heiko Fehr: »Let's Code Python«, Bonn (Rheinwerk-Verlag) 2019, Seiten 247ff.
# Krabbe: Nitin Chowdary (CC0), https://opengameart.org/content/crab
# Luftblasen: HorrorPen (CC-BY 3.0), https://opengameart.org/content/bubbles8-colors
# Bildhintergrund: Kenney.nl Fish Pack (CC0), https://www.kenney.nl/assets/fish-pack

from processing import *
from random import randint

WIDTH, HEIGHT = 640, 416
NUM_BUBBLES = 50
NUM_ENEMIES = 5

class Background():
  
  def __init__(self, _img):
    self.img = loadImage(_img)
    
  def display(self):
    image(self.img, 0, 0)

class Crab():
  
  def __init__(self):
    self.img1 = loadImage("crab1.png")
    self.img2 = loadImage("crab2.png")
    self.img = self.img1
    self.w = 64
    self.h = 64
    self.r = 32
    self.x = width//2 - self.w//2
    self.y = height//2 + 100
    self.dir = "None"
    self.speed = 5
    self.animation_count = 0
    self.score = 0
    
  def update(self):
    if self.dir == "None":
      self.x += 0
    elif self.dir == "RIGHT":
      if self.x <= width - self.w - 5:
        self.x += self.speed
    elif self.dir == "LEFT":
      if self.x >= 2:
        self.x -= self.speed
    self.animation_count += 1
    if self.animation_count >= 10:
      self.animation_count = 0
    if self.animation_count <= 5:
      self.img = self.img1
    else:
      self.img = self.img2

  def display(self):
    image(self.img, self.x, self.y)
    
class Bubble():
  
  def __init__(self):
    self.reset()
    self.speed = 2
    
  def reset(self):
    dia = str(randint(0, 2))
    self.img = loadImage("bubbleblue" + dia + ".png")
    self.r = self.img.width//2
    self.x = randint(0, width)
    self.y = randint(-2*height, -50)
    
  def is_circle_collision(self, other):
    distance = dist(self.x, self.y, other.x, other.y)
    if distance < self.r + other.r:
      return True
    return False
  
  def update(self):
    self.y += self.speed
    if self.y > height + 50:
      self.reset()
    
  def display(self):
    image(self.img, self.x, self.y)

class EnemyBubble(Bubble):
  
  def __init__(self):
    super().__init__()
    self.reset()
    self.r = 15
    self.speed = 3
    
  def reset(self):
    self.img = loadImage("bubblere1.png")
    self.x = randint(0, width)
    self.y = randint(-2*height, -50)
    

bubbles = []
enemybubbles = []
    
def setup():
  global bg, crab
  size(WIDTH, HEIGHT)
  print("🐠 Crab Dancing with Bubbles - Stage 3 🐡")
  bg = Background("background.png")
  for _ in range(NUM_BUBBLES):
    bubble = Bubble()
    bubbles.append(bubble)
  for _ in range(NUM_ENEMIES):
    enemybubble = EnemyBubble()
    enemybubbles.append(enemybubble)
  crab = Crab()
  
def draw():
  background(49, 197, 244) # Hellblau
  bg.display()
  crab.update()
  crab.display()
  for bubble in bubbles:
    bubble.update()
    if bubble.is_circle_collision(crab):
      bubble.reset()
      crab.score += 1
    bubble.display()
  for enemybubble in enemybubbles:
    enemybubble.update()
    if enemybubble.is_circle_collision(crab):
      print("GAME OVER")
      crab.x = 2000
      crab.y = 2000
    enemybubble.display()
  
def mousePressed():
  if mouseButton == LEFT:
    crab.dir = "LEFT"
  elif mouseButton == RIGHT:
    crab.dir = "RIGHT"

def mouseReleased():
  crab.dir = "NONE"

run()