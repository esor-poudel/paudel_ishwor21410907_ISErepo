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


def calculate_life_path(birth_day):
    day,month,year = map(int, birth_day.split('/'))
    
    day_count = single_digit_number(day)
    month_count = single_digit_number(month)
    year_count = single_digit_number(year)
    # print(day,month,year)
    # print(day_count,month_count,year_count)
    count = day_count + month_count + year_count
    return single_digit_number(count)

def find_lucky_color():
    pass

def find_master_number():
    pass

