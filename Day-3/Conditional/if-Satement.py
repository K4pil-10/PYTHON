height = int(input("Enter your height in cm: "))
bill = 0
if height >= 179:
    print("You can ride")
    age = int(input("Enter your age: "))
    if age < 12:
        bill = 5
        print("You have to pay $5")
    elif age <= 18:
        bill = 7
        print("You have to pay $7")
    else :
        bill = 10
        print("You have to pay $10")
    want_photo = input("wan photo then type y for  Yes and n for No: ")
    if want_photo == "y":
        bill += 3
    print(f"The total bill is {bill}")
else:
    print("You can't ride")