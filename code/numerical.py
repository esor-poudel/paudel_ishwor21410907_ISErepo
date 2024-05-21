

def calculate_life_path(birth_day):
    day,month,year = map(int, birth_day.split('/'))
    
    day_count = single_digit_number(day)
    month_count = single_digit_number(month)
    year_count = single_digit_number(year)
    # print(day,month,year)
    # print(day_count,month_count,year_count)
    count = day_count + month_count + year_count
    return single_digit_number(count)

def find_lucky_color(life_path_number):
    colors = {
        1: "Red",
        2: "Orange",
        3: "Yellow",
        4: "Green",
        5: "Sky Blue",
        6: "Indigo",
        7: "Violet",
        8: "Magenta",
        9: "Gold",
        11: "Silver",
        22: "White",
        33: "Crimson"
    }
    return colors.get(life_path_number)



def check_if_mater_number(num):
    if num in [11,22,33]:
        return True
    return False

def single_digit_number(num):
    if check_if_mater_number(num):
        return num
    while num > 9:
        num = sum(int(digit) for digit in str(num))
    return num        
