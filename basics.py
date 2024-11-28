# print string
print("I'm learning python!")

# print string from a variable
programming_language = "JavaScript"
print(f"I'm not learning {programming_language}")

# print multiplication
x = 6
y = 7
print(x * y)

# print floating point number instead of integer, removed // operator
x = 9
y = 4
z = x / y
print(f"x divided by y is {z}")

# compute and print how many oranger are left over
oranges = 9
baskets = 4
oranges_per_basket = oranges // baskets
oranges_left = oranges % baskets
print(f"When I divide {oranges} oranges over {baskets} baskets...")
print(f"I have {oranges_per_basket} oranges per basket...")
print(f"and I will have {oranges_left} oranges left, to keep for myself!")

# print correct result
x = int("32")
y = 10
z = x + y
print(f"x plus y is {z}")

# print correct result
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = x + y
print(f"The first number plus the second number is {z}")
