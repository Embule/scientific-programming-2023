# exercise 1
x = 12
if x < 50:
    print("foo")
else:
    print("bar")

# exercise 2
x = 9
y = 10
if x < y:
    y = y + 5
else:
    y = 0
print(y)

# exercise 3
speed = 115
limit = 100

if speed >= limit + 25:
    print("Your fine is 232€")
elif speed >= limit + 20:
    print("Your fine is 174€")
elif speed >= limit + 10:
    print("Your fine is 64€")
elif speed >= limit + 5:
    print("Your fine is 30€")
else:
    print("You be driving fine!")

# exercise 4
user_input = input("What is your age? ")
age = int(user_input)
is_student = input("Are you a student? (y/n)")

if age < 12:
    print("Free entrance!")
elif age < 18 or age >= 65 or is_student == "y":
    print("You receive a discount at the museum.")
else:
    print("No discount.")
