height = int(input("Enter your height: "))

if height >= 179:
    print("You can ride")
    age = int(input("Enter your age: "))
    if age < 12:
        print("You have to pay $5")
    elif age <= 18:
        print("You have to pay $7")
    else :
        print("You have to pay $10")
else:
    print("You can't ride")