import turtle
import pandas


# Create the screen
screen = turtle.Screen()
screen.title("Name the States - U.S.")
screen.setup(width=730, height=510)

# Add the map as Turtle Shape
us_map = "blank_states_img.gif"
screen.addshape(us_map)
turtle.shape(us_map)

# Get the data
data = pandas.read_csv("50_states.csv")
state_list = data.state.tolist()
user_guesses = []

# Use a loop to continuously guess
while len(user_guesses) < 50:

    # Prompt the user to type a State
    answer_state = screen.textinput(title=f"{len(user_guesses)}/{len(data)} - Guess the state",
                                    prompt="Type a state name.").title()
    # Check if the guess is correct
    if answer_state in state_list:
        state_data = data[data.state == answer_state]
        # Record correct guesses in a list
        user_guesses.append(state_data.state.item())
        # Write the state into the map
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.color("black")
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

screen.exitonclick()