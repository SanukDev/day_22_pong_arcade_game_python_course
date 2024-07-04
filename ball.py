from turtle import Turtle



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_po = 10
        self.y_po = 10

    def move_ball(self):
        x_position = self.xcor()
        y_position = self.ycor()
        self.goto(x_position + self.x_po, y_position + self.y_po)

    def bounce_y(self):
        self.y_po *= - 1

    def bounce_x(self):
        self.x_po *= - 1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
