import turtle
from turtle import Screen

# Create the screen
screen = Screen()
screen.title("Name the States - U.S.")
screen.setup(width=730, height=510)

# Add the map as Turtle Shape
us_map = "blank_states_img.gif"
screen.addshape(us_map)
turtle.shape(us_map)


