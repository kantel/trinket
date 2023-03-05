import turtle, math

WIDTH, HEIGHT = 440, 440
WALL   = 63
DOOR   = 62
CHEST  = 22
PLAYER = 10
TILESIZE = 16

maze_map_0 = [[63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63],
            [63,10,-1,63,63,63,63,63,63,63,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,63,63,63,63,63],
            [63,-1,-1,63,63,63,63,63,63,63,-1,-1,63,63,63,63,63,63,-1,-1,63,63,63,63,63],
            [63,-1,-1,-1,-1,-1,-1,-1,63,63,-1,-1,63,63,63,63,63,63,-1,-1,63,63,63,63,63],
            [63,-1,-1,-1,-1,-1,-1,-1,63,63,-1,-1,63,63,63,-1,-1,-1,-1,-1,-1,-1,-1,63,63],
            [63,63,63,63,63,63,-1,-1,63,63,-1,-1,63,63,63,-1,-1,-1,-1,-1,-1,-1,-1,63,63],
            [63,63,63,63,63,63,-1,-1,63,63,-1,-1,63,63,63,63,63,63,-1,-1,63,63,63,63,63],
            [63,63,63,63,63,63,-1,-1,63,63,-1,-1,-1,-1,63,63,63,63,-1,-1,63,63,63,63,63],
            [63,-1,-1,63,63,63,-1,-1,-1,-1,-1,-1,-1,-1,63,63,63,63,22,-1,63,63,63,63,63],
            [63,-1,-1,63,63,63,-1,-1,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63],
            [63,-1,-1,-1,-1,-1,-1,-1,-1,-1,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63],
            [63,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,63,63,63,63,63,63,63,63],
            [63,63,63,63,63,63,63,63,63,63,63,63,-1,-1,-1,-1,-1,63,63,63,63,63,-1,22,63],
            [63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,-1,-1,63,63,63,63,63,-1,-1,63],
            [63,-1,-1,63,63,63,63,63,63,63,63,63,63,63,63,-1,-1,-1,-1,-1,-1,-1,-1,-1,63],
            [63,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,63],
            [63,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,63,63,63,63,63,63,63,63,63,63,63,63,63],
            [63,63,63,63,63,63,63,63,63,63,-1,-1,63,63,63,63,63,63,63,63,63,63,63,63,63],
            [63,63,63,63,63,63,63,63,63,63,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,63],
            [63,22,-1,-1,63,63,63,63,63,63,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,63],
            [63,-1,-1,-1,63,63,63,63,63,63,63,63,63,63,63,63,63,63,-1,-1,63,63,63,63,63],
            [63,-1,-1,-1,-1,-1,63,63,63,63,63,63,63,63,63,63,63,63,-1,-1,63,63,63,63,63],
            [63,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,63,63,63,63,-1,-1,-1,-1,-1,-1,-1,-1,63],
            [63,63,63,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,62],
            [63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63]]

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("#2b3e50")

# Bildschirm-Refresh ausschalten
screen.tracer(0)

# Die Turtle-Bilder registrieren
images = ["wall1.png", "wizard.png", "chest.png", "key.png"]
for image in images:
  screen.addshape(image)

class Player(turtle.Turtle):
  
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.penup()
    self.right(270)
    self.shape("wizard.png")
    self.speed(0)
    self.gold = 0
    
  # Player Movement
  def go_up(self):
    next_x, next_y = self.xcor(), self.ycor() + TILESIZE
    if (next_x, next_y) not in walls:
      self.goto(next_x, next_y)
    
  def go_down(self):
    next_x, next_y = self.xcor(), self.ycor() - TILESIZE
    if (next_x, next_y) not in walls:
      self.goto(next_x, next_y)
    
  def go_left(self):
    next_x, next_y = self.xcor() - TILESIZE, self.ycor()
    if (next_x, next_y) not in walls:
      self.goto(next_x, next_y)
    
  def go_right(self):
    next_x, next_y = self.xcor() + TILESIZE, self.ycor()
    if (next_x, next_y) not in walls:
      self.goto(next_x, next_y)
      
  # Kollisionserkennung (Pythagoras)
  def is_collision(self, other):
    a = self.xcor() - other.xcor()
    b = self.ycor() - other.ycor()
    distance = math.sqrt((a**2) + (b**2))
    if distance < 5:
      return True
    else:
      return False

class Wall(turtle.Turtle):
  
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.penup()
    self.shape("wall1.png")
    self.speed(0)

class Chest(turtle.Turtle):
  
  def __init__(self, _x, _y):
    turtle.Turtle.__init__(self)
    self.penup()
    self.right(270)
    self.shape("chest.png")
    self.speed(0)
    self.gold = 100
    self.goto(_x, _y)
  
  def destroy(self):
    self.goto(2000, 2000)
    self.hideturtle()
  
levels = []
levels.append(maze_map_0)

def setup_maze(level):
  for y in range(len(level)):
    for x in range(len(level[y])):
      # Get the mumber of every item in the mace
      item_number = level[y][x]
      # Berechne die Bildschirmkoordinaten
      screen_x = -192 + (x*TILESIZE)
      screen_y =  192 - (y*TILESIZE)
      
      # Prüfe, ob Item ein Wall ist
      if item_number == WALL:
        wall.goto(screen_x, screen_y)
        wall.stamp()
        walls.append((screen_x, screen_y))
        
      # Prüfe, ob Item der Spieler ist
      if item_number == PLAYER:
        player.goto(screen_x, screen_y)
        
      # Prüfe, ob Item eine Schatztrue ist
      if item_number == CHEST:
        chests.append(Chest(screen_x, screen_y))

wall = Wall()
walls = []
chests = []
player = Player()

# Level Setup
setup_maze(levels[0])

# Das Spiel beenden
def exit_game():
  global keep_going
  print("Bye, bye, Baby")
  keep_going = False

# Auf Tastaturereignisse lauschen
screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_right, "Right")

screen.onkey(exit_game, "q")   # Das Spiel beenden

# Spiel starten
print("🧙 Simple Maze Game Stage 1 🧙")
keep_going = True
while keep_going:
  # Hat der Spieler eine Schatzkiste gefunden?
  for chest in chests:
    if player.is_collision(chest):
      player.gold += chest.gold
      print("Player Gold: {}".format(player.gold))
      # Verberge die Schatzkiste
      chest.destroy()
      # Lösche die Schatzkiste aus der Liste
      chests.remove(chest)
  # Ist der Spieler dem Labyrint entkommen?
  if player.xcor() > 192:
    print("**Gewonen!**")
    exit_game()
  
  screen.update()   # den gesamten Bildschirm neu zeichnen