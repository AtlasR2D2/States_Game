import pandas as pd

def construct_us_states_dictionary():
    us_states = pd.read_csv("50_states.csv")
    us_states_state = us_states["state"].tolist()
    us_states["coordinates"] = us_states[["x", "y"]].apply(tuple, axis=1)
    us_states_coordinates = us_states["coordinates"].tolist()
    return dict(zip(us_states_state, us_states_coordinates))

us_states_dict = construct_us_states_dictionary()