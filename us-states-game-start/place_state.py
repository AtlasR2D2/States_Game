import turtle
from states_fn import us_states_dict

FONT = ("Courier", 8, "normal")
ALIGNMENT = "Center"

states_dict = us_states_dict

class Place_State(turtle.Turtle):
    def __init__(self, state_name):
        super().__init__()
        self.state_name = state_name
        self.coordinates = states_dict[self.state_name]
        self.hideturtle()
        self.penup()
        self.goto(self.coordinates)
        self.write(arg=self.state_name, align=ALIGNMENT, font=FONT)
