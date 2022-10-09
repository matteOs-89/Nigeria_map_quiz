import turtle
import pandas
from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
screen.screensize(300, 300)
screen.title("Guess the Nigeria States")
image = "map_of_nigeria.gif"
screen.addshape(image)
t.shape(image)

def get_mouse_click_color(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_color)

guessed_state = []

missed_state = []

data = pandas.read_csv("nigeria_states.csv")

data_state = data.state.to_list()

while len(guessed_state) < 37:

    guess_answer = screen.textinput(title=f"{len(guessed_state)}/36 + FCT correct",
                                    prompt="Type another guess or Exit to Quit: ").title()

    if guess_answer in guessed_state:
        guessed_state.remove(guess_answer)


    if guess_answer in data_state:
        guessed_state.append(guess_answer)
        state_info = data[data.state == guess_answer]
        dot = Turtle()
        dot.hideturtle()
        dot.penup()
        dot.goto(int(state_info.x), int(state_info.y))
        dot.write(guess_answer)

    if guess_answer == "Exit":
        missed_state = [state for state in data_state if state not in guessed_state]
        new_list = pandas.DataFrame(missed_state)
        new_list.to_csv("nigeria_states_not_guessed")
        break





screen.mainloop()