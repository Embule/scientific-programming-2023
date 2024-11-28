# excercise 1
list = ["banana", 10.9, 2, "fruit", 42]
print(list[0], list[4], list[-1])

# excercise 2
list[1] = "Hello"
print(list)

# excercise 3
list = [
    "1kg apples",
    "100g sugar",
    "1 tsp cinnamon",
    "1 lemon",
    "300g flour",
    "1 tsp baking powder",
]
for item in list:
    print(item)

# excercise 4
number = 1
list = []
while number < 31:
    list.append(number)
    number += 1
print(list)

# excercise 5
list = [9, 10, 11, 12]
sum = 0

for number in list:
    sum += number

print(sum)

# excercise 6
numbers = [8, 2, 3, 15, 7, 19]

numbers2 = []
for number in numbers:
    if number > 5 and number < 16:
        numbers2.append(number)

print(numbers2)

# excercise 7
numbers = [8, 2, 3, 15, 7, 19]
count = 0
numbers2 = []

for number in numbers:
    if number > 5 and number < 16:
        numbers2.append(number)
    else:
        count += 1

print(numbers2)
print(count)

# excercise 8
n = 123
list = []
range = range(0, n)

for number in range:
    if number % 3 == 0 and number % 5 == 0:
        list.append(number)
print(list)

dates = [
    "September 21st",
    "September 23rd",
    "September 24th",
    "September 26th",
    "September 29th",
    "October 1st",
    "October 2nd",
    "October 4th",
]
names = ["Mark", "Betty", "Dirk", "Betty", "Mark", "Mark", "Dirk", "Betty"]

last_date = None
for i in range(len(dates)):
    dates[i]
    names[i]

    if names[i] == "Dirk":
        last_date = dates[i]

print("last date", last_date)
