from processing import *
from random import randint

WIDTH, HEIGHT = 720, 520
BG_WIDTH = 1664
FPS = 60
ANIM = 4   # Animation Cycle
UPDOWN = 3
MAX_FIRECOUNT = 15
NO_ENEMIES = 10

## Oberklasse für alles, was sich bewegt

class Sprite():

  def __init__(self):
    pass

  def display(self):
    image(self.img, self.x, self.y)
  
  def collide_rect(self, other):
    distance_x = (self.x + self.w/2) - (other.x + other.w/2)
    distance_y = (self.y + self.h/2) - (other.y + other.h/2)
    half_w = self.w/2 + other.w/2
    half_h = self.h/2 + other.h/2
    if (abs(distance_x) < half_w):
      if (abs(distance_y) < half_h):
        return True
    return False

class Background(Sprite):
  
  def __init__(self, _x, _y):
    Sprite.__init__(self)
    self.x = _x
    self.y = _y
    self.start_x = _x
    self.img = loadImage("desert.png")
    
  def update(self):
    self.x -= 1
    if self.x <= -BG_WIDTH:
      self.x = BG_WIDTH
  

class Missile(Sprite):
  
  def __init__(self, _x, _y):
    Sprite.__init__(self)
    self.img = loadImage("missile.png")
    self.x = _x
    self.y = _y
    self.w = 19
    self.h = 7
    self.speed = 10
  
  def update(self):
    self.x += self.speed
    for enemy in enemies:
      if self.collide_rect(enemy):
        missiles.remove(self)
        # Enemy Explosion
        e_x, e_y = enemy.x, enemy.y - 5
        enemy.reset()
        hit = Explosion(e_x, e_y)
        hits.append(hit)
    if self.x >= width + 20:
      missiles.remove(self)

class Explosion(Sprite):
  
  def __init__(self, _x, _y):
    Sprite.__init__(self)
    self.img = loadImage("explosion.png")
    self.x = _x
    self.y = _y
    self.w = 38
    self.h = 38
    self.timer = 10
    
  def update(self):
    self.timer -= 1
    if self.timer <= 0:
      hits.remove(self)
  
class Plane(Sprite):
  
  def __init__(self):
    Sprite.__init__(self)
    self.images = []
    for i in range(2):
      img = loadImage("planegreen_" + str(i) + ".png")
      self.images.append(img)
    self.img = self.images[0]
    self.x = 75
    self.y = 240
    self.w = 44
    self.h = 30
    self.dir = "NONE"
    self.frame = 0
    self.ani = 20
    self.firecount = 0
  
  def update(self):
    if self.dir == "NONE":
      self.y += 0
    elif self.dir == "UP":
      if self.y > 20:
        self.y -= UPDOWN
    elif self.dir == "DOWN":
      if self.y < height - 20:
        self.y += UPDOWN
    self.ani += 1
    if self.ani >= ANIM:
      self.ani = 0
      self.frame += 1
      if self.frame > 1:
        self.frame = 0
    self.firecount -= 1
    self.img = self.images[self.frame]
      
  def fire(self):
    if self.firecount < 0:
      missile = Missile(self.x + 20, self.y + 20)
      missiles.append(missile)
      self.firecount = MAX_FIRECOUNT

class Enemy(Sprite):
  
  def __init__(self, _x, _y):
    Sprite.__init__(self)
    self.img = loadImage("pizza.png")
    self.x = _x
    self.y = _y
    self.w = 36
    self.h = 36
    self.speed = randint(3, 6)
    
  def reset(self):
    self.x = width + randint(30, 100)
    self.y = randint(30, height - 30)
    self.speed = randint(3, 6)
    
  def update(self):
    self.x -= self.speed
    if self.x < -30:
      self.reset()
    
# Listen
backs = []
missiles = []
hits = []
enemies = []
    
def setup():
  global plane
  size(WIDTH, HEIGHT)
  frameRate(FPS)
  print("🍕 Pizza Plane Stage 3 🍕")
  print("Linke Maustaste: Flieger fliegt nach oben.")
  print("Rechte Maustaste: Flieger fliegt nach unten.")
  print("Mittlere Maustaste: Feuern!")
  # Hintergrund
  back1 = Background(0, 0)
  back2 = Background(BG_WIDTH, 0)
  backs.append(back1)
  backs.append(back2)
  # Den Flieger initialisieren
  plane = Plane()
  # Die Gegner (Pizzas)
  for _ in range(NO_ENEMIES):
    pizza = Enemy(width + randint(30, 100), randint(30, height - 30))
    enemies.append(pizza)
  
def draw():
  background(231, 229, 226)   # Wüstenhimmel
  for back in backs:
    back.update()
    back.display()
  plane.update()
  plane.display()
  for missile in missiles:
    missile.update()
    missile.display()
  for enemy in enemies:
    enemy.update()
    enemy.display()
  for hit in hits:
    hit.update()
    hit.display()
  
def mousePressed():
  if mouseButton == LEFT:
    plane.dir = "UP"
  elif mouseButton == RIGHT:
    plane.dir = "DOWN"
  elif mouseButton == CENTER:
    plane.fire()

def mouseReleased():
  plane.dir = "NONE"

run()    
