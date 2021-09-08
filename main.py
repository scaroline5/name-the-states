from turtle import Screen
import turtle
import pandas


# Create the screen
screen = Screen()
screen.title("Name the States - U.S.")
screen.setup(width=730, height=510)

# Add the map as Turtle Shape
us_map = "blank_states_img.gif"
screen.addshape(us_map)
turtle.shape(us_map)

# Get the data
data = pandas.read_csv("50_states.csv")

# Set the Score
correct_answers = 0
total_states = len(data)

# Prompt the user to type a State
answer_state = screen.textinput(title=f"{correct_answers}/{total_states} - Guess the state", prompt="Type a state name.").lower()


