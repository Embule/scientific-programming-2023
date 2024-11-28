# exercise 1
def half(number):
    return number / 2


x = 4
y = 3
a = half(x)
b = half(y)

print(a, b)


# exercise 2
def mean(x, y):
    return (x + y) / 2


x = mean(4, 6)
print(x)


# exercise 3
def max(a, b):
    if a > b:
        return a
    return b


x = 4
y = 18
z1 = max(x, y)
z2 = max(y, x)

print(z1, z2)


# exercise 4
def maxx(a, b, c):
    number = max(a, b)

    return max(number, c)


x = 1
y = 2
z = 3

print(maxx(y, x, z))


# exercise 5
def my_sum(list):
    sum = 0
    for number in list:
        sum += number
    return sum


my_list = [1, 2, 3, 4]
s = my_sum(my_list)
print(s)


# exercise 6
def arrange(start, stop, step):
    list = []

    while start < stop:
        list.append(start)
        start += step
    return list


x_values = arrange(-1, 3, 0.5)
print(x_values)
