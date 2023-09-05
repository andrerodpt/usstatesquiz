import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. Stages Game")
bg_image = 'blank_states_img.gif'
screen.addshape(bg_image)
screen.setup(width=721, height=491)
turtle.shape(bg_image)

## Get the data
states = pd.read_csv('50_states.csv')


def write_state_text(state, x, y):
    tim = turtle.Turtle()
    tim.penup()
    tim.hideturtle()
    tim.goto(x, y)
    tim.write(state, align='center', font=('Arial', 8, "normal"))

correct_guesses = []
while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 Guess the State", prompt="What's another state's name?").title()
    if answer_state == 'Exit':
        break

    result_df = states[states.state == answer_state]

    if not result_df.empty and answer_state not in correct_guesses:
        correct_guesses.append(answer_state)
        x_cor = result_df['x'].values[0]
        y_cor = result_df['y'].values[0]
        write_state_text(answer_state, x_cor, y_cor)

states_to_learn_df = states[~states['state'].isin(correct_guesses)]
states_to_learn_df.to_csv('states_to_learn.csv', index=False)
