# Draws several lines radiating out from the origin.
# Matthew Franklin 11 - 28 - 2022
import turtle
import random


class StampTurtle(turtle.Turtle):
    # Constructor - just copy and use for now
    def __init__(self):
        super().__init__()

    def forward(self, dist):
        super().forward(dist)
        self.stamp()

    def backward(self, dist):
        super().backward(dist)
        self.color(random.choice(["red","blue","green","purple","orange"]))
        #I was printing out the color change because I had problems with it changing at first, so that assured I was doing it right/wrong
        #print(self.color)
        self.stamp()

class MattsTurtle(turtle.Turtle):
    # Constructor - just copy and use for now
    def __init__(self):
        super().__init__()

#For the forward portion I had it choose a random pensize to use
    def forward(self, dist):
        super().forward(dist)
        self.pensize(random.randrange(7,12))
        self.stamp()

#for the backward portion, I changed the shape of the turtle when it stamps to make it an actual turtle
    def backward(self, dist):
        super().backward(dist)
        self.shape("turtle")
        self.stamp()

def main():
    # named constants
    screen_size = 500
    screen_startx = 60  # x coordinate of the left edge of the graphics window
    # Set up the window and its attributes
    wn = turtle.Screen()
    wn.setup(screen_size, screen_size, screen_startx, 0)
    turtle_list = []
    num_turtles = 2
    num_stamp_turtles = 3
    #I used a variable to have a for loop in range of how many MattsTurtle I wanted
    num_matt_turtles = 3
    # Create a list of different colored turtles, each pointing
    #   in a different direction
    for _ in range(num_turtles):
        t = turtle.Turtle()
        t.right(random.randrange(350))
        t.color(random.choice(['red', 'green', 'blue', 'yellow']))
        # t.speed(7)
        turtle_list.append(t)

    # Create a list of different colored stamp_turtles, each pointing
    #   in a different direction

    for _ in range(num_stamp_turtles):
        t = StampTurtle()
        t.right(random.randrange(350))
        t.color('black')
        #t.speed(7)
        turtle_list.append(t)

    #the for loop in order to append my new turtle class into the turtle list
    for _ in range(num_matt_turtles):
        t = MattsTurtle()
        t.left(random.randrange(350))
        #I changed the color to a random solid color in order to easily spot the difference once it printed out
        t.color(random.choice(["red","blue","green"]))
        turtle_list.append(t)

    # Move each turtle outward from the origin ten times
    for t in turtle_list:
        for _ in range(10):
            t.backward(random.randrange(10, 30))
    wn.exitonclick()


# Run the main function. This should be the last statement in the file.
main()