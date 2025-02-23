from turtle import Turtle
INITIAL_POSITION = [(0,0),(-20, 0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in INITIAL_POSITION:
            self.add_segment(position)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self,position):
        snake_body = Turtle(shape="square")
        snake_body.color("green")
        snake_body.penup()
        snake_body.goto(position)
        self.segments.append(snake_body)

    def move_forward(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_cord = self.segments[seg_num - 1].xcor()
            y_cord = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_cord, y_cord)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)