# Multiple return

def country_city(country,city):
    if country =="" or city == "":
        return "You didn't put any value!"
    live = country.title()
    lives= city.title()
    return f"You live in {live} , {lives}"
output= country_city(country=input("In which country do you live? \n"), city=input("In which city do yo live?"))
print(output)