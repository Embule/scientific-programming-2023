# exercise 1
total = 0
for x in range(1, 5):
    print(f"x now has the value {x}")
    total = total + x
    print(f"The sum of all numbers from 1 to 4 = {total}")

print(f"The sum of all numbers from 1 to 4 = {total}")

# exercise 2
total = 0
maximum = 10
for x in range(1, maximum):
    print(f"x now has the value {x}")
    total = total + x
    print(f"The sum of all numbers from 1 to 4 = {total}")

print(f"The sum of all numbers from 1 to 4 = {total}")
print()

# exercise 3
total = 0
maximum = 9
i = 0

while i < maximum:
    print(f"x now has the value {i}")
    i += 1
    total = total + i
    print(f"The sum of all numbers from 1 to 4 = {total}")

print(f"The sum of all numbers from 1 to 4 = {total}")

# exercise 4
total = 0
maximum = 9
i = 0

while total <= 20:
    print(f"x now has the value {i}")
    i += 1
    total = total + i
    print(f"The sum of all numbers from 1 to 4 = {total}")

print(f"The sum of all numbers from 1 to 4 = {total}")

# exercise 5
counter = 0
for number in range(1, 20):
    if number > 15:
        print(f"This number is bigger than 15: {number}")
    if number % 3 == 0:
        counter += 1
        print(f"This number is exactly divisible by 3: {number}")

print(f"From the numbers 1 to 20 there are {counter} number divisable by 3")

# exercise 6
for x in range(1, 6):
    for y in range(1, 4):
        print(f"x = {x}, y = {y}")
    print(f"The value of x is now {x} and we have just finished the loop over y")

# exercise 7
for x in range(1, 6):
    for y in range(1, x):
        print(f"x = {x}, y = {y}")
    print(f"The value of x is now {x} and we have just finished the loop over y")
