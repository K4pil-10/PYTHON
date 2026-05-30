from unittest import result

def name(f_name, l_name):
    print(f_name.title(),l_name.title())
name(f_name="kapil", l_name="chhetri")

def country_capital(nepal, india):
    city1=nepal.title()
    city2= india.title()
    return f"{city1} {city2}"
result= country_capital(nepal="KATHMANdu", india="New DelhI")
print(result)


#combine function

def country(name):
    return name + name

def country_2(name):
    return name.title()

output= country_2(country("NePaL")) #Nepalnepal
print(output)