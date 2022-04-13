print("How many integers would you like to enter?")
integer = int(input( ))
min = 0
max = 0
print("Please enter " + str(integer) + " integers")
for number in range(integer):
    num =  int(input( ))
    if num < min or number == 0:
        min=num
    if num > max or number == 0:
        max=num
print("min: " + str(min) + ".")
print("max: " + str(max) + ".")