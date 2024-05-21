def find_user_generation(birth_day):
    day,month,year = map(int, birth_day.split('/'))
    generations = {
        "Silent Generation": (1901, 1945),
        "Baby Boomer": (1946, 1964),
        "Generation X": (1965, 1979),
        "Millennial": (1980, 1994),
        "Generation Z": (1995, 2009),
        "Generation Alpha": (2010, 2024)
    }
    for generation, (start_year, end_year) in generations.items():
        if start_year <= year <= end_year:
            return generation
    return "Unknown Generation"