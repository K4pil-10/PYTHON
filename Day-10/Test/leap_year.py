def is_leap_year(year):
    num= year
    if num % 4 == 0:
        if num % 100 == 0:
            if num % 400 == 0:
                return f"{num}  is a leap year"
            else:
                return f"{num} isn't leap year"
        else:
            return f"{num} is a leap year"
    else:
        return f"{num} isn't leap year"
output=is_leap_year(year=int(input("Enter days: ")))
print(output)