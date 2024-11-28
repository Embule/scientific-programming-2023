# use abbreviation 'plt' for  plot library
import matplotlib.pyplot as plt

x_values = []
y_values = []

# add the values between 0 and 4 of x to a list in steps of 0.01
x = 0
while x < 3.99:
    x_values.append(x)
    x += 0.01

# calculate the corresponding y-value for each x and add it to a list
for x in x_values:
    y = 12.38 * x**4 - 84.38 * x**3 + 165.19 * x**2 - 103.05 * x
    y_values.append(y)

# find the smallest value of y and the corresponding value of x
smallest_y = y_values[0]
corresponding_x = x_values[0]
for i in range(len(y_values)):
    y_value = y_values[i]
    x_value = x_values[i]

    if y_value < smallest_y:
        corresponding_x = x_value
        smallest_y = y_value

# print the coordinates for the smallest value of y
print(f"(xmin, ymin) = ({round(corresponding_x,2)}, {round(smallest_y,2)})")

# plot the whole graph with the point of smallest value of y
plt.plot(x_values, y_values, "b-")
plt.plot(corresponding_x, smallest_y, "ro")
plt.xlabel("x", fontsize=15)
plt.ylabel("f(x)", fontsize=15)
plt.text(
    corresponding_x - 2,
    smallest_y,
    f"(xmin, ymin) = ({round(corresponding_x,2)}, {round(smallest_y,2)})",
    color="black",
    fontsize=10,
)
plt.show()
