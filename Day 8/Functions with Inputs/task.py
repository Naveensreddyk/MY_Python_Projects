life_until = 90
weeks_in_year = 52
def life_in_weeks(current_age):
    remaining_years = life_until - current_age
    you_left = remaining_years * weeks_in_year
    print(f"You have left {you_left} weeks.")

life_in_weeks(12)



