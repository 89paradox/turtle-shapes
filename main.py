import turtle
turtle = turtle.Turtle()
turtle.speed(100)
class shapes:
	def square(size=5):
		for i in range(4):
			turtle.forward(size * 10)
			turtle.right(90)
	def circle(size):
		for i in range(720 * size):
			turtle.forward(0.5)
			turtle.right(0.5 / size)
shapes.circle(1)
shapes.circle(2)