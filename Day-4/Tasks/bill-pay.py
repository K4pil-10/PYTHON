import random

friends = ["Kapil", "Ishan", "Subash", "Bikram", "Sunil"]
# print(friends[random.randint(0,4)])
bill_payer = random.randint(0,4) # can use random.choice()
if bill_payer == 0 :
    print("Kapil should pay bill")
elif bill_payer == 1 :
    print("Ishan should pay bill")
elif bill_payer == 2 :
    print("Subash should pay bill")
elif bill_payer== 3 :
    print("Bikram should pay bill")
else:
    print("Sunil hould pay bill")

