import turtle
import time
from random import randint

#declaring window variable
window = turtle.Screen()
window.setup(width=1000, height=800, startx=None, starty=None)
window.tracer(0, 0)

#declares variable for drawing turtle
back_turtle = turtle.Turtle()

text_turtle = turtle.Turtle()
text_turtle.ht()

lap_turtle = turtle.Turtle()
lap_turtle.speed(0)
lap_turtle.ht()
lap_turtle.color('white')
lap_turtle.up()
lap_turtle.goto(0, 80)
lap_turtle.pendown()

inputWrite = turtle.Turtle()
inputWrite.ht()
inputWrite.penup()
inputWrite.goto(0, -100)
inputWrite.pendown()

carTurtle = turtle.Turtle()
carTurtle.penup()
carTurtle.goto(-380, 0)
carTurtle.setheading(-90)
carTurtle.color('red')

timer_turtle = turtle.Turtle()
timer_turtle.ht()
timer_turtle.speed(0)
timer_turtle.penup()
timer_turtle.goto(-380,- 350)
timer_turtle.pendown()
timer_turtle.color('white')

game_over = turtle.Turtle()
game_over.speed(0)
game_over.ht()
game_over.color("white")
game_over.penup()
game_over.goto(0, 0)
game_over.pendown()

start_turtle = turtle.Turtle()
start_turtle.ht()
start_turtle.penup()
start_turtle.goto(0, 0)
start_turtle.pendown()
start_turtle.color("white")

# list of words for the game
wordlist = ["chicken", "dog", "fox", "cow", "moose", "fish", "linus", "bunny", "frog"]

usr_word = ''

laps = 0

timer = 10000

#funtions for letter input
def onA():
  inputWrite.clear()
  global usr_word
  usr_word += 'a'
  inputWrite.write(usr_word, False, align="center", font=("Arial", 30, "normal"))

def onB():
  inputWrite.clear()
  global usr_word
  usr_word += 'b'
  inputWrite.write(usr_word, False, align="center", font=("Arial", 30, "normal"))

def onC():
  inputWrite.clear()
  global usr_word
  usr_word += 'c'
  inputWrite.write(usr_word, False, align="center", font=("Arial", 30, "normal"))

def onD():
  inputWrite.clear()
  global usr_word
  usr_word += 'd'
  inputWrite.write(usr_word, False, align="center", font=("Arial", 30, "normal"))

def onE():
  inputWrite.clear()
  global usr_word
  usr_word += 'e'
  inputWrite.write(usr_word, False, align="center", font=("Arial", 30, "normal"))

def onF():
  inputWrite.clear()
  global usr_word
  usr_word += 'f'
  inputWrite.write(usr_word, False, align="center", font=("Arial", 30, "normal"))

def onG():
  inputWrite.clear()
  global usr_word
  usr_word += 'g'
  inputWrite.write(usr_word, False, align="center", font=("Arial", 30, "normal"))

def onH():
  inputWrite.clear()
  global usr_word
  usr_word += 'h'
  inputWrite.write(usr_word, False, align="center", font=("Arial", 30, "normal"))

def onI():
  inputWrite.clear()
  global usr_word
  usr_word += 'i'
  inputWrite.write(usr_word, False, align="center", font=("Arial", 30, "normal"))

def onJ():
  inputWrite.clear()
  global usr_word
  usr_word += 'j'
  inputWrite.write(usr_word, False, align="center", font=("Arial", 30, "normal"))

def onK():
  inputWrite.clear()
  global usr_word
  usr_word += 'k'
  inputWrite.write(usr_word, False, align="center", font=("Arial", 30, "normal"))

def onL():
  inputWrite.clear()
  global usr_word
  usr_word += 'l'
  inputWrite.write(usr_word, False, align="center", font=("Arial", 30, "normal"))

def onM():
  inputWrite.clear()
  global usr_word
  usr_word += 'm'
  inputWrite.write(usr_word, False, align="center", font=("Arial", 30, "normal"))

def onN():
  inputWrite.clear()
  global usr_word
  usr_word += 'n'
  inputWrite.write(usr_word, False, align="center", font=("Arial", 30, "normal"))

def onO():
  inputWrite.clear()
  global usr_word
  usr_word += 'o'
  inputWrite.write(usr_word, False, align="center", font=("Arial", 30, "normal"))

def onP():
  inputWrite.clear()
  global usr_word
  usr_word += 'p'
  inputWrite.write(usr_word, False, align="center", font=("Arial", 30, "normal"))

def onQ():
  inputWrite.clear()
  global usr_word
  usr_word += 'q'
  inputWrite.write(usr_word, False, align="center", font=("Arial", 30, "normal"))

def onR():
  inputWrite.clear()
  global usr_word
  usr_word += 'r'
  inputWrite.write(usr_word, False, align="center", font=("Arial", 30, "normal"))

def onS():
  inputWrite.clear()
  global usr_word
  usr_word += 's'
  inputWrite.write(usr_word, False, align="center", font=("Arial", 30, "normal"))

def onT():
  inputWrite.clear()
  global usr_word
  usr_word += 't'
  inputWrite.write(usr_word, False, align="center", font=("Arial", 30, "normal"))

def onU():
  inputWrite.clear()
  global usr_word
  usr_word += 'u'
  inputWrite.write(usr_word, False, align="center", font=("Arial", 30, "normal"))

def onV():
  inputWrite.clear()
  global usr_word
  usr_word += 'v'
  inputWrite.write(usr_word, False, align="center", font=("Arial", 30, "normal"))

def onW():
  inputWrite.clear()
  global usr_word
  usr_word += 'w'
  inputWrite.write(usr_word, False, align="center", font=("Arial", 30, "normal"))

def onX():
  inputWrite.clear()
  global usr_word
  usr_word += 'x'
  inputWrite.write(usr_word, False, align="center", font=("Arial", 30, "normal"))

def onY():
  inputWrite.clear()
  global usr_word
  usr_word += 'y'
  inputWrite.write(usr_word, False, align="center", font=("Arial", 30, "normal"))

def onZ():
  inputWrite.clear()
  global usr_word
  usr_word += 'z'
  inputWrite.write(usr_word, False, align="center", font=("Arial", 30, "normal"))

def onEsc():
    turtle.bye()

def onBack():
  inputWrite.clear()
  global usr_word
  usr_word = usr_word[:-1]
  inputWrite.write(usr_word, False, align="center", font=("Arial", 30, "normal"))

#listening for keyboard input

def keyActivate():
  window.listen()

  window.onkey(onA, "a")
  window.onkey(onB, "b")
  window.onkey(onC, 'c')
  window.onkey(onD, 'd')
  window.onkey(onE, 'e')
  window.onkey(onF, 'f')
  window.onkey(onG, 'g')
  window.onkey(onH, 'h')
  window.onkey(onI, 'i')
  window.onkey(onJ, 'j')
  window.onkey(onK, 'k')
  window.onkey(onL, 'l')
  window.onkey(onM, 'm')
  window.onkey(onN, 'n')
  window.onkey(onO, 'o')
  window.onkey(onP, 'p')
  window.onkey(onQ, 'q')
  window.onkey(onR, 'r')
  window.onkey(onS, 's')
  window.onkey(onT, 't')
  window.onkey(onU, 'u')
  window.onkey(onV, 'v')
  window.onkey(onW, 'w')
  window.onkey(onX, 'x')
  window.onkey(onY, 'y')
  window.onkey(onZ, 'z')
  window.onkey(onBack, 'BackSpace')

def keyDeactivate():
  window.onkey(None, "a")
  window.onkey(None, "b")
  window.onkey(None, 'c')
  window.onkey(None, 'd')
  window.onkey(None, 'e')
  window.onkey(None, 'f')
  window.onkey(None, 'g')
  window.onkey(None, 'h')
  window.onkey(None, 'i')
  window.onkey(None, 'j')
  window.onkey(None, 'k')
  window.onkey(None, 'l')
  window.onkey(None, 'm')
  window.onkey(None, 'n')
  window.onkey(None, 'o')
  window.onkey(None, 'p')
  window.onkey(None, 'q')
  window.onkey(None, 'r')
  window.onkey(None, 's')
  window.onkey(None, 't')
  window.onkey(None, 'u')
  window.onkey(None, 'v')
  window.onkey(None, 'w')
  window.onkey(None, 'x')
  window.onkey(None, 'y')
  window.onkey(None, 'z')
  window.onkey(None, 'BackSpace')

keyActivate()

window.onkey(onEsc, 'Escape')

def background():
  window.tracer(0, 0)
  #used to draw curves of track
  def curves():
    for i in range(90):
      back_turtle.speed(0)
      back_turtle.forward(5)
      back_turtle.left(1)
  window.bgcolor("forestgreen")
  back_turtle.pensize(100)
  back_turtle.speed(0)
  back_turtle.penup()
  back_turtle.goto(-380, 0)
  back_turtle.pendown()
  back_turtle.right(90)
  curves()
  back_turtle.forward(200)
  curves()
  curves()
  back_turtle.forward(200)
  curves()
  start_turtle.write("Press Space to Start", False, align='center', font=("Arial", 50, 'normal'))
  window.update()
  lap_turtle.write("Laps: ", False, align='center', font=("Arial", 50, "normal"))

#turtle function to draw words
def writeWord(word):
  text_turtle.clear()
  text_turtle.ht()
  text_turtle.color("white")
  text_turtle.write(word, False, align="center", font=("Arial", 60, "normal"))

background()

window.tracer(8, 0)
wordindex = randint(0, 8)
word = wordlist[wordindex]
writeWord(word)

def detection():
  def timerFunc():
    global timer
    timer_turtle.clear()
    timer -= 1
    timer_turtle.write(str(timer)[1:3], False, align="center", font=("Arial", 50, "normal"))
    window.update()
  timerFunc()
  global word
  global usr_word
  global laps
  window.update()
  if usr_word == word:
    carTurtle.color('blue')
    inputWrite.clear()
    usr_word = ''
    def turn():
      for i in range(90):
        carTurtle.speed(0)
        carTurtle.forward(5)
        carTurtle.left(1)
    turn()
    carTurtle.speed(10)
    carTurtle.forward(200)
    turn()
    turn()
    carTurtle.speed(10)
    carTurtle.forward(200)
    turn()
    laps += 1
    window.update()
    
    lap_turtle.clear()
    lap_turtle.write("Laps: " + str(laps), False, align='center', font=("Arial", 50, "normal"))

    wordindex = randint(0, 8)
    word = wordlist[wordindex]
    writeWord(word)

  if usr_word != word:
    if len(usr_word) >= len(word):
      carTurtle.color('red')
      inputWrite.clear()
      usr_word = ''
      wordindex = randint(0, 8)
      word = wordlist[wordindex]
      writeWord(word)

def loop():
  start_turtle.clear()
  while True:
    detection()
    if str(timer)[1:3] == '00':
      game_over.write('Game Over', False, align='center', font=('Arial', 60, 'normal'))
      inputWrite.clear()
      carTurtle.ht()
      text_turtle.clear()
      window.update()
      break

window.onkey(loop, 'space')
turtle.mainloop()