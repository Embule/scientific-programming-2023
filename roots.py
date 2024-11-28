import math
import matplotlib.pyplot as plt

x_values = []

# add the values of x to a list in steps of 0.01
x = -6
while x < 4:
    x_values.append(x)
    x += 0.01


# calculate the corresponding y-value for each x and add it to a list
def plot_roots(a, b, c):
    list = []

    for x in x_values:
        y = a * x**2 + b * x + c
        list.append(y)
    return list


# calculate the roots of the equation and add them to list
def roots(a, b, c):
    roots_list = []
    try:
        x1 = (-b - math.sqrt(b**2 - 4 * a * c)) / 2 * a
        x2 = (-b + math.sqrt(b**2 - 4 * a * c)) / 2 * a

        roots_list.append(x1)
        roots_list.append(x2)
        return roots_list
    # if the numbers do not fit the equation return empty list
    except ValueError:
        return roots_list


# call and define the values
y_values = plot_roots(1, 2, -10)
result = roots(1, 2, -10)

# print the roots if the equation has them
if len(result) == 0:
    print("This equation does not have roots.")
else:
    x1 = round(result[0], 2)
    x2 = round(result[1], 2)
    print(f"The roots are {x1} and {x2}")

# plot the whole graph
plt.plot(x_values, y_values, "b-")
plt.axhline(0, color="red", linestyle="--")
plt.xlabel("x", fontsize=15)
plt.ylabel("f(x)", fontsize=15)

# if the graph has root points add their coordinates
if len(result) > 0:
    plt.plot(x1, 0, "ro")
    plt.plot(x2, 0, "ro")
    plt.text(
        x1,
        1,
        f"x1 = {x1}",
        color="black",
        fontsize=10,
    )
    plt.text(
        x2,
        1,
        f"x2 = {x2}",
        color="black",
        fontsize=10,
    )
plt.show()
