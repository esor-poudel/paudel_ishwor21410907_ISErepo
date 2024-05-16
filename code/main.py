from generation import find_user_generation
from numerical import *

def make_analysation(birth_day):
    life_path = calculate_life_path(birth_day)
    lucky_color = find_lucky_color(life_path)
    generation = find_user_generation(birth_day)
    return life_path,lucky_color,generation

if __name__ == "__main__":
    
    date = input("Enter date of birth")
    path = make_analysation(date)
    print(path)