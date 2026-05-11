# Types of Random
# 1. random.randint() // print whole number
# 2. random.random() // 0-1
# 3. random.uniform() // float
# 4. random.tringular()

import random
print("between 0 to 1 ")
dec_random = random.random()
print(dec_random)

print("between acc to domain and range (a,b) a--> starting and b--> ending")
num_random = random.randint(1,100)
print(num_random)

print("floating point")

num_float = round(random.uniform(1,10),2)
print(num_float)