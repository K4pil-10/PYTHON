def life_in_weeks(age):
    yera_left= 100-age
    total_weeks_left= yera_left *7
    print(f"total weeks to left {total_weeks_left}")
life_in_weeks(age=int(input("enter your age: ")))