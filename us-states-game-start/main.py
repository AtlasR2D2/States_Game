import turtle
import states_fn
from place_state import Place_State
from states_fn import us_states_dict
import time
import pandas as pd

FONT_GameOver = ("Courier", 16, "normal")
ALIGNMENT_GameOver = "Center"

def add_background_image(screen_x):
    screen_x.addshape(map_image)  # Set the Background Picture to Map
    turtle.shape(map_image)

states_dict = us_states_dict

screen = turtle.Screen()
screen.title("U.S. States Game")

screen.tracer(0)

map_image = "blank_states_img.gif"
add_background_image(screen)

correct_guesses = []    # Used to store correct guesses

game_over = False
victory_flag = False
while not game_over:
    screen.update()
    answer_state = screen.textinput(title="Guess a State", prompt="Name another state: ").title()
    if answer_state.lower() == "exit":
        game_over = True
        victory_flag = False
    elif answer_state in correct_guesses:
        pass
    else:
        if answer_state in states_dict:
            correct_guesses.append(answer_state)
            place_state = Place_State(state_name=answer_state)
        else:
            game_over = True
            victory_flag = False

    if len(correct_guesses) == len(states_dict): # Check if user has guessed all states correctly
        game_over = True
        victory_flag = True

screen.tracer()

missing_states = []
if not victory_flag:
    final_score = len(correct_guesses)
    final_score_string = f"You got {final_score} out of {len(states_dict)} correct."
    screen.clear()
    turtle.hideturtle()
    turtle.write(
        arg=f"Game Over.\n{final_score_string}\nThe missing states will be exported as a csv.\nClick on screen to exit.",
        align=ALIGNMENT_GameOver, font=FONT_GameOver)
    for state in states_dict:
        if state not in correct_guesses:
            missing_states.append(state)
    # Export missing states as a csv for some homework
    pd.DataFrame(missing_states,columns=["state"]).to_csv("missing_states.csv")
else:
    final_score = len(correct_guesses)
    final_score_string = f"You got {final_score} out of {len(states_dict)} correct."
    screen.clear()
    turtle.hideturtle()
    turtle.write(arg=f"You Win!\n{final_score_string}\nClick on screen to exit.", align=ALIGNMENT_GameOver,
                 font=FONT_GameOver)

screen.exitonclick()
