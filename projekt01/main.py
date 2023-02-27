from processing import *
from random import uniform, randint, choice

WIDTH, HEIGHT = 600, 400
NO_BALLS = 100

class Ball():
  
  def __init__(self, _x, _y):
    self.x = _x
    self.y = _y
    pyxelpal = [color(169, 193, 255), color(126, 32, 114), color(212, 24, 108), 
          color(211, 132, 65), color(233, 195, 91), color(112, 198, 169), 
          color(118, 150, 222), color(163, 163, 163), color(255, 151, 152),
          color(237, 199, 176)]
    self.color = choice(pyxelpal)
    self.dx = uniform(-2.5, 2.5)
    if abs(self.dx) <= 0.2:
      self.dx = uniform(0.5, 2.5)
    self.dy = uniform(-2.5, 2.5)
    if abs(self.dy) <= 0.2:
      self.dy = uniform(0.5, 2.5)
    self.d = randint(12, 20)    # Durchmesser
    
  def update(self):
    self.x += self.dx
    self.y += self.dy
    if self.x >= WIDTH - self.d//2 or self.x <= self.d//2:
      self.dx *= -1
    if self.y >= HEIGHT - self.d//2 or self.y <= self.d//2:
      self.dy *= -1
    
  def show(self):
    noStroke()
    fill(self.color)
    ellipse(self.x, self.y, self.d, self.d)
    
balls = []
    
def setup():
  size(WIDTH, HEIGHT)
  print("Hallo, Jörg!")
  for _ in range(NO_BALLS):
    ball = Ball(randint(20, WIDTH-20), randint(20, HEIGHT-20))
    balls.append(ball)

def draw():
  background(57, 92, 152)   # dark blue
  for ball in balls:
    ball.update()
    ball.show()
    
run()