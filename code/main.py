from generation import find_user_generation
from numerical import *

def make_analysation(birth_day):
    life_path = calculate_life_path(birth_day)
    return life_path

if __name__ == "__main__":
    date = "13/11/1987"
    path = make_analysation(date)
    print(path)