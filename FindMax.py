#How to compare more than 2 variable

#Assign or get variables
x = 10
y = 9
z = 100

#Assign max to first variable
current_max = x

#Compare 1 at a time
if current_max < y:
    current_max = y
if current_max < z:
    current_max = z

#Find which variable was the max
if current_max == x:
    print("Max is x")
elif current_max == y:
    print("Max is y")
else:
    print("Max is z")

print(current_max)





