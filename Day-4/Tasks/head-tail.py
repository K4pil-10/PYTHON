import random

# choose = input("Choose head or tail. Type h for head and t for tail: ").lower()

ans = random.randint(0,1)

if ans == 0  :
    print("Heads")
else :
    print("Tail")