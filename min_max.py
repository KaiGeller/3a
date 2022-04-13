integer = int(input("How many integers would you like to enter: "))
print(integer)
min = 0
max = 0
for number in range(integer):
    num =  int(input("Please enter " + str(integer) + " integers: "))
    if num < min or number == 0:
        min=num
    if num > max or number == 0:
        max=num
print("min: " + str(min) + ".")
print("max: " + str(max) + ".")