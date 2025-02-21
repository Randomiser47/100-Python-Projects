import turtle
import pandas
from state_move import State_m
score = turtle
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv('50_states.csv')
state_name = states_data.state
states_to_learn = []
guessed_states = []
answerd_state = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(state_name)} Guess the state", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state not in state_name.values:
        print("Invalid state! Try again.") 
        continue 

    #If valid, proceed to get the coordinates
    answerd_state.append(answer_state)
    x_place = int(states_data[states_data["state"] == answer_state].x.iloc[0])
    y_place = int(states_data[states_data["state"] == answer_state].y.iloc[0])

    guessed_states.append(answer_state)

    state_label = State_m(answer_state, x_place, y_place)
            
         
for state in states_data.state:
    if state not in answerd_state:
        states_to_learn.append(state)
pandas.DataFrame(states_to_learn).to_csv("learn_states.txt")