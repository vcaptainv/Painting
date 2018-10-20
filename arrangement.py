#Yusheng Hu
#arrangement.py
#11/09/2015

import lsystem
import turtle_interpreter
import turtle

def goto(x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    
def triangle(x, y, size):
	#draw a triangle out
	goto(x, y)
	for i in range(3):
		turtle.forward(size)
		turtle.right(120)
		
def block( x, y, width, height):
    goto( x, y )
    for i in range(2):
    	turtle.forward(width)
    	turtle.left(90)
    	turtle.forward(height)
    	turtle.left(90)
    	
def house(x, y, scale):
	# draw a house out
	turtle.color('brown4')
	turtle.fill(True)
	block(x, y, scale, scale)
	turtle.fill(False)
	turtle.left(90)
	turtle.color('orange')
	turtle.fill(True)
	triangle(x, y+scale, scale)
	turtle.fill(False)
	turtle.color("black")
	turtle.setheading(0)


	
def grassland():
	#Likewise, I draw a big rectangle on the bottom of the page and color it green
	turtle.color('peru')
	turtle.fill(True)
	block(-400, -500, 1000, 400)
	turtle.fill(False)
	turtle.color("black")

def sky():
	#I draw a big rectangle on the top of the page and color it blue
	turtle.color(0.0, 1.0, 1.0)
	turtle.fill(True)
	block(-500, -100, 1000, 1000)
	turtle.fill(False)
	turtle.color("black")

def main():
	# assign the lsystem string to a new parameter
	sun = lsystem.Lsystem('sun.txt')
	tree1 = lsystem.Lsystem('systemCL.txt')
	tree2 = lsystem.Lsystem('systemDL.txt')
	tree3 = lsystem.Lsystem('tree2.txt')
	tree4 = lsystem.Lsystem('systemFL.txt')
	tree5 = lsystem.Lsystem('systemGL.txt')
	#then apply iteration to the string
	tstr1 = sun.buildString(5)
	tstr2 = tree1.buildString(3)
	tstr3 = tree2.buildString(3)
	tstr4 = tree3.buildString(3)
	tstr5 = tree4.buildString(3)
	tstr6 = tree5.buildString(5)
	
	turtle.tracer(False)
	
	sky()
	grassland()
	turtle.setheading(90)
	house(250, -180, 200)
	
	terp = turtle_interpreter.TurtleInterpreter()
	# draw the shapes out 
	terp.color('red')
	terp.goto(-250, 250)
	terp.drawString(tstr1, 30, 30)
		
	turtle.setheading(90)
	terp.color((0.5, 0.4, 0.3 ))
	terp.goto(-50, -300)
	terp.drawString(tstr2, 10, 30)
	
	turtle.setheading(90)
	terp.color((0, 0, 0))
	terp.goto(150, -250)
	terp.drawString(tstr3, 10, 30)
	
	turtle.setheading(90)
	terp.color((0, 0, 0))
	terp.goto(-280, -320)
	terp.drawString(tstr4, 10, 30)
	
	turtle.setheading(90)
	terp.color((0.7,0.2,0.3))
	terp.goto(-200, -250)
	terp.drawString(tstr5, 10, 30)
	
	turtle.setheading(90)
	terp.color((0.5, 0.5, 0.5))
	terp.goto(300, -300)
	terp.drawString(tstr6, 5, 30)
	
	
	
	
	
	terp.hold()
	turtle.update()
if __name__ == "__main__":
  main()

