from generation import find_user_generation
from numerical import *

def make_analysation(birth_day):
    life_path = calculate_life_path(birth_day)
    lucky_color = find_lucky_color(life_path)
    generation = find_user_generation(birth_day)
    return life_path,lucky_color,generation

def validate_user_birthday(birthday):
    
    for seperator in ['/','-','.']:
        if seperator in birthday:
            birthday_parts = birthday.split(seperator)
            break
    else:
        print("Date format should be seperated by /. Thank you")
        return False
    
    if len(birthday_parts) != 3:
        print("Please enter proper birthday. Thank you")
        return False
    
    month,day,year = birthday_parts
    
    if not (month.isdigit() and day.isdigit() and year.isdigit() and len(year) == 4):
        print("Something Went wrong with your birthday")
        return False
    
    month = int(month)
    day = int(day)
    year = int(year)
    
    if not (1901 <= year <= 2024):
        print("Invalid Year, Please choose year between 1901 to 2024")
        return False
    
    return True
    
            

if __name__ == "__main__":
    
    birthday = input("Please enter your birthday (in the format MM/DD/YYYY): ")
    if not validate_user_birthday(birthday):
        print("")
    else:
        path = make_analysation(birthday)
        print(path)