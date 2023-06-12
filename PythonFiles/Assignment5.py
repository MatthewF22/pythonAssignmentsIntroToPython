# Create several turtles and have them jump around randomly
# Record each position on the screen with a text description of the location
#
# Matthew Franklin, 9/26/2019
import turtle
import random


def myRand(sz):
    """ Returns a random integer in the range -sz to sz """
    return random.randrange(-sz, sz)


def getLocation(t):
    """ Returns a string with the location of turtle t """
    loc = "I'm at" + str(t.position())
    return loc


def main():
    # define turtles
    wn = turtle.Screen()
    mrT = turtle.Turtle()
    msPacMan = turtle.Turtle()
    msPacMan.color("blue")
    babyHuey = turtle.Turtle()
    babyHuey.color("orange")

    # define screen bounds
    width = 225
    height = 250

    # draw turtles and their locations
    for _ in range(3):
        # Move 1st turtle
        mrT.goto(myRand(width), myRand(height))
        mrT.stamp()
        mrT.write(getLocation(mrT))

        # Move 2nd turtle
        # Put your code here for msPacMan
        msPacMan.goto(myRand(width), myRand(height))
        msPacMan.stamp()
        msPacMan.write(getLocation(msPacMan))

        # Move 3rd turtle
        # Put your code here for babyHuey
        babyHuey.goto(myRand(width), myRand(height))
        babyHuey.stamp()
        babyHuey.write(getLocation(babyHuey))
    wn.exitonclick()


# Start the program
main()