# Dictionary

#apple-key
#red- value
colors_fruits = {
    "apple": "red",
    "pineapple": "yellow",
    "mango": "green",
    "dragon_fruit": "white",
    "grapes": "black"
}

print(colors_fruits["apple"])
print(colors_fruits["grapes"])

# wipe an existing dictionary
colors_fruits= {
    "apple": "white"
    }
print(colors_fruits)

# Edit item in dictionary
print(colors_fruits) #notice in apple value in first and now

#Push method in dictionary
empty_dictionary = {
    "greet": 'hello world'
    }
print(empty_dictionary)


car_dictionary = {
    1: "Tesla",
    2: "TaTa",
    3: "Lamborghini",
    4: "Ferrari",
    5: "Mustang GTR",
}

#loop in dictionary

for key in car_dictionary:
    print(key) #print value of key from car_dictionary
    print(car_dictionary[key])
