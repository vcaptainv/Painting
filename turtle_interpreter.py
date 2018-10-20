#Yusheng Hu
#turtle interpreter
#VERSION 2
import turtle
import random

class TurtleInterpreter:
	def __init__(self, dx = 800, dy = 800):
		turtle.setup(width=dx, height=dy)
		turtle.tracer(False)
 
	def drawString(self, dstring, distance, angle):
		#create two lists which can include information of turtle position and turtle color
		stack =[]
		color=[]
		# for each character in the dstirng
		for c in str(dstring):
	
			if c == 'F':
			# python would go forward	
				turtle.forward(distance)
			
			elif c == '+':
			#turtle would turn left	
				turtle.left(angle)
			elif c == '-':
			#turtle would turn right	
				turtle.right(angle)
			elif c == '[':
			#turtle would record the position and heading angle
				stack.append(turtle.position())
				stack.append(turtle.heading())
			elif c == ']':
			#turtle would return to the position and heading angle recorded before	
				turtle.up()
				turtle.setheading(stack.pop())
				turtle.setposition(stack.pop())
				turtle.down()
			elif c == 'L':
			#turtle would draw a green leave 	
				h = turtle.heading()
				p = turtle.position()
				turtle.color('limegreen')
				turtle.fill(True)
				turtle.circle(distance/3, 180)
				turtle.fill(False)
				turtle.color('black')
				turtle.up()
				turtle.goto(p)
				turtle.down()
				turtle.setheading(h)
			elif c == 'o':
			# turtle would draw a berry	
				turtle.color(random.random(), random.random(), random.random())
				turtle.fill(True)
				turtle.circle(distance/5, 360)
				turtle.fill(False)
				turtle.color("black")
			elif c=='<':
			#turtle would record the color value
				color.append(turtle.color()[0])
			elif c=='>':
			#turtle would return to the color value recorded before
				turtle.color(color.pop())
			elif c=='g':
			#turtle would turn to green color
				turtle.color(0.15,0.5,0.2)
			elif c=='y':
			#turtle would turn to yellow color
				turtle.color(0.8,0.8,0.3)
			elif c=='r':
			#turtle would turn to red color
				turtle.color(0.7,0.2,0.3)
			elif c == 'b':
			#turtle would change color to brown
				turtle.color('saddlebrown')
			elif c == '%':
			#turtle would change color to chocolate
				turtle.color('chocolate')
			elif c == '!':
			#turtle would change color to black
				turtle.color('black')
			elif c == 'w':
			#turtle would change the width to 2(make the line seems thicker)
				turtle.width(2)
			elif c == 'c':
			#turtle would return to default value of width
				turtle.width(1)	
		turtle.update()
		
	def hold(self):

		# have the turtle listen for events
		turtle.listen()

		# hide the turtle and update the screen
		turtle.ht()
		turtle.update()

		# have the turtle listen for 'q'
		turtle.onkey( turtle.bye, 'q' )
		# have the turtle listen for a click
		turtle.onscreenclick( lambda x,y: turtle.bye() )

		# start the main loop until an event happens, then exit
		turtle.mainloop()
		exit()
		
	def place(self, xpos,ypos,angle=None):
		turtle.up()
		turtle.goto(xpos,ypos)
		if angle !=None:
			turtle.setheading(angle)
		turtle.down()
		
	def orient(self,angle):
		turtle.setheading(angle)
		
	def goto(self,xpos,ypos):
		turtle.up()
		turtle.goto(xpos,ypos)
		turtle.down()
	
	def color(self,c):
		turtle.color(c)
		
	def width(self,w):
		turtle.width(w)