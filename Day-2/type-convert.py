# str --> bool, float, int
print("Converting string to Bool, float and integers")

strings = bool("Kapil")
print(type(strings))
strings = int("60")+ int("7")
print(strings)
strings = float("1.111") + float("22.2")
print(strings)

# float --> bool, str, int
print("Converting float to Bool, string and integers")

floats = bool(1.1111)
print(type(floats))

floats = int(1.1111)
print(type(floats))

floats = str(1.1111)
print(type(floats))

print("Converting booleans to str, float and integers")

booleans = str(True)
print(type(booleans))

booleans = int(True)
print(type(booleans))

booleans = float(True)
print(type(booleans))
