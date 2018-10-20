#Yusheng Hu
#shapes.py
#11/10/2015

import lsystem
import turtle_interpreter
import turtle

def main(x, x0, y0):
	#x stands for itteration x0 y0 stands for position 
	shape = lsystem.Lsystem('shape.txt')
	tstr = shape.buildString(x)
	terp = turtle_interpreter.TurtleInterpreter()
	terp.goto(x0, y0)
	terp.drawString(tstr, 30, 360/x)
	
def draw():
	#use a loop to draw the graph out
	for i in range (3, 7):
		main(i, -100+100*(i-3), 0)
		turtle.setheading(0)
	terp = turtle_interpreter.TurtleInterpreter()
	terp.hold()	
if __name__ == "__main__":
  draw()	
