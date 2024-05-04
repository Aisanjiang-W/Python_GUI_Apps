from turtle import Turtle

start_position = [(0, 0), (-20, 0), (-40, 0)]
moving_distance = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.crate_snake()
        self.head = self.segments[0]

    def crate_snake(self):
        for position in start_position:
            self.add_segment(position)

    def add_segment(self, position):
        new_segments = Turtle(shape="square")
        new_segments.color("White")
        new_segments.penup()
        new_segments.goto(position)
        self.segments.append(new_segments)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.crate_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment_position in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_position - 1].xcor()
            new_y = self.segments[segment_position - 1].ycor()
            self.segments[segment_position].goto(new_x, new_y)
        self.head.forward(moving_distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
