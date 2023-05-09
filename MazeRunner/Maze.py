# import section
import turtle as t 
import random as r
import time 
#Game Configuration 
wn=t.Screen()
wallLength=15
numberOfWalls=25
pathWidth=15
barrier=15
interval = 1000
fontSetup=("Times New Roman",30,"normal")
timer = 5
flag = True
paused = False 
#Initialize Objects or Turtles
mazeDrawer = t.Turtle()
mazeDrawer.pensize(5)
mazeDrawer.pencolor("blue")
mazeDrawer.speed(0)
timekeeper = t.Turtle()
timekeeper.pu()
timekeeper.hideturtle()
timekeeper.goto(-100,-300)
timekeeper.pd()
timekeeper.speed(0)
mazeRunner = t.Turtle()
mazeRunner.color("red")
mazeRunner.pu()
mazeRunner.goto(-pathWidth*3,pathWidth*3)
mazeRunner.pd()
mazeEnemy= t.Turtle()
mazeEnemy.color("black")
mazeEnemy.pu()
mazeEnemy.goto(-pathWidth*3-20,pathWidth*3-20)
mazeEnemy.pd()
mazeEnemy.speed("slowest")
#Functions
def drawDoor(pos):
    mazeDrawer.fd(pos)
    mazeDrawer.pu()
    mazeDrawer.fd(pathWidth*2 )
    mazeDrawer.pd()
def drawBarrier(pos):
    mazeDrawer.fd(pos)
    mazeDrawer.left(90)
    mazeDrawer.fd(pathWidth*2)
    mazeDrawer.bk(pathWidth*2)
    mazeDrawer.right(90)    
def drawMaze():
    wallLength=15
    for w in range(numberOfWalls):
        wallLength+=pathWidth
        if w>4:
          mazeDrawer.left(90)
          
          #where do we draw the walls and the barries inside of a wall length
          doorSpot = r.randint(pathWidth*2,(wallLength-2*pathWidth))
          barrierSpot = r.randint(pathWidth*2,(wallLength-2*pathWidth))
          
          #check to make sure a door and barrier do not render on top each other
          while abs(doorSpot-barrierSpot) < pathWidth:
              doorSpot=r.randint(pathWidth*2,(wallLength-2*pathWidth))
          #draw the wall 
          if(doorSpot<barrierSpot):
              drawDoor(doorSpot)
              drawBarrier(barrierSpot-doorSpot-pathWidth*2)
              #draw rest of wall
              mazeDrawer.fd(wallLength-barrierSpot)
          else:
              drawBarrier(barrierSpot)
              drawDoor(doorSpot-barrierSpot)
              mazeDrawer.fd(wallLength-doorSpot-pathWidth*2)
    for i in range(4):
      wallLength+=pathWidth
      mazeDrawer.left(90)
      mazeDrawer.fd(wallLength)
def moveUp():
  mazeRunner.setheading(90)
def moveDown():
  mazeRunner.setheading(270)
def moveLeft():
  mazeRunner.setheading(180)
def moveRight():
  mazeRunner.setheading(0)
def go():
    collisionDistance=5
    #Pac man movement, so no going through walls
    mazeRunner.fd(1)
    #determine if it hits a wall
    canvas = wn.getcanvas()
    x,y=mazeRunner.pos()
    margin=1
    items = canvas.find_overlapping(x+margin,-y+margin,x-margin,-y+margin)
    if (abs(mazeRunner.xcor() - mazeDrawer.xcor()) < collisionDistance):
      if (abs(mazeRunner.ycor() - mazeDrawer.ycor()) < collisionDistance):
          print("Game Over!")
          mazeEnemy.fillcolor("red")
          mazeRunner.fillcolor("red") 
          mazeEnemy.hideturtle()
          mazeRunner.hideturtle()
          timekeeper.hideturtle()   


    if(len(items)>0):       #stack of what is overalapping 
        canvasColor = canvas.itemcget(items[0], "fill")
        if canvasColor=="blue":  # we know we have hit a wall
            mazeRunner.color("gray")
            wn.onkeypress(None,"Return")    #disbling the movement 
            mazerunnerreturn()
            return
    wn.ontimer(go,15)
def pausee():
  print("p has been pressed")
  print(paused)
  paused = True
  if paused == True:
    interval = 0
  else:
    pass 
def updatetimer():
    #global is to let this fucntion know to go look at a  golbal var
    global timer
    timekeeper.clear()
    if timer >= 60:
        timekeeper.write("Game Over!",font=fontSetup)
    else:
        timer+=1
        timekeeper.write(f"Timer: {timer}",font=fontSetup)
    #object.write("message",options)
    #we need to recuslively run this fucntion 
    #timerkeeper gets the screen's ontimer and resets the comand and inteval
    timekeeper.getscreen().ontimer(updatetimer,interval)
def mazerunnerreturn():
  global timer
  mazeRunner.clear()
  mazeRunner.pu()
  mazeRunner.goto(-pathWidth*3,pathWidth*3)
  mazeRunner.pd()
  wn.onkeypress(go,"Return")
def runturt():
  wn.update()
  print("RAN")
  mazeEnemy.clear()
  x=mazeRunner.xcor()
  y=mazeRunner.ycor()
  mazeEnemy.goto(x,y)


          
#Events
#wn.ontimer(updatetimer,interval)
wn.onkeypress(moveUp,"w")
wn.onkeypress(moveDown,"s")
wn.onkeypress(moveLeft,"a")
wn.onkeypress(moveRight,"d")
wn.onkeypress(go,"Return")   #Enter and Return are different 
wn.onkeypress(pausee,"p")   #Enter and Return are different 

wn.listen()
#Main Loop or Game Loop or Running Code
drawMaze()
# startt.onclick()

wn.ontimer(updatetimer,interval)
#wn.ontimer(runturt,1)
while True:
  wn.update()
  mazeEnemy.clear()
  x=mazeRunner.xcor()
  y=mazeRunner.ycor()
  mazeEnemy.goto(x-timer+50,y-timer+50)
  if timer-60 == 0:
    print("You got the turtle!")
    print("Game Over!")
    mazeEnemy.fillcolor("red")
    mazeRunner.fillcolor("red") 
    mazeEnemy.hideturtle()
    mazeRunner.hideturtle()
    timekeeper.hideturtle()   
  
    
    # mazerunnerreturn()
  
  
  
wn.mainloop()