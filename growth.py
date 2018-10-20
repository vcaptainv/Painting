#Yusheng Hu
#growth.py
#11/10/2015

import lsystem
import turtle_interpreter
import turtle

def main():
	#first create a empty list which would record all the strings that python would draw
	tasklist =[]
	tasklist.append('l1.txt')
	tasklist.append('l2.txt')
	turtle.tracer(False)
	# use double loop to draw the graph out
	for j in range (2):
		for i in range (2, 5):
			task = lsystem.Lsystem(tasklist[j])
			tstr = task.buildString(i)
			terp = turtle_interpreter.TurtleInterpreter()
			x0 = -300 + (i-2)*200
			y0 = 200 - j*400
			terp.goto(x0, y0)
			terp.drawString(tstr, 15, 120)
					
	terp.hold()
	turtle.update()	
if __name__ == "__main__":
  main()