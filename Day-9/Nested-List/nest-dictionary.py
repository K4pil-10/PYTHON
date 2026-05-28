# Dictionary
capitals = {
    "Nepal": "Kathmandu",
    "India": "New Delhi",
    "Germany": "Berlin",
    "Japan": "Tokyo"
}

# Nested List Dictionary

#list inside dictionary
travel_cities = {
    "Nepal": ["Kathmandu", "Butwal", "Pokhara"],
    "India": ["Kolkata", "New Delhi", "Cennai"]
}
print(travel_cities["Nepal"][1])

#list inside list   
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

# dictionary inside dictionary
visit = {
    "Nepal":{
        "cities_visited": ["Kathmandu", "Butwal", "Pokhara"],
        "num_times_visit":3,
    },
    "India": {
        "cities_visited": ["Kolkata", "New Delhi", "Cennai"],
        "num_times_visit":3,

    }
}

print(visit["India"]["cities_visited"][2])
print(visit["India"]["num_times_visit"])