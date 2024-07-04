from turtle import Screen, Turtle

class Padlle(Turtle):

    def __init__(self, x_position, y_position):
        self.x = x_position
        self.y = y_position
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(x_position, y_position)
        self.speed(0)
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up_padlle(self):
        loc = self.ycor()
        self.goto(self.x, loc + 30)

    def down_padlle(self):
        loc = self.ycor()
        self.goto(self.x, loc - 30)

    def contro_padlle(self,up, down):
        screen = Screen()
        screen.listen()
        screen.onkey(key=up, fun=self.up_padlle)
        screen.onkey(key=down, fun=self.down_padlle)