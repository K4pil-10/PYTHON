# from os.path import split

print("Welcome to the Tip calculator")
bill = float(input("What was the total bill? \n" ))
tip = float(input("How much tip would you like to give? 10, 12 or 15 \n"))
total_people = float(input("How many people to spilt the bill? \n"))

# calc tip

tip_amount = (tip/100) * bill

total_amount = bill + tip_amount

split_amt = total_amount / total_people

print(f"Each person should pay : ${split_amt:.2f}")

print("Enjoying to learn python")