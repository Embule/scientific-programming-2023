import matplotlib.pyplot as plt


# approximate the integral of a quadratic equation using the Riemann sum
def riemann(a, b, c, begin_x, end_x, n):
    approximate = 0
    width = (end_x - begin_x) / n

    # calculate the area under the curve by iterating over the values of x
    while begin_x < end_x:
        x = (begin_x + (begin_x + width)) / 2
        y = a * x**2 + b * x + c
        area = y * width
        approximate += area
        begin_x += width

    return approximate


# function for plotting the whole graph using the Riemann function
def plot_riemann(a, b, c, begin_x, end_x, n):
    x_values = []
    y_values = []
    width = (end_x - begin_x) / n

    # add x and y values to their lists using the equation
    while begin_x < end_x:
        x = (begin_x + (begin_x + width)) / 2
        y = a * x**2 + b * x + c
        y_values.append(y)
        x_values.append(begin_x)
        begin_x += width

    # plot the graph with calculated x and y values
    plt.plot(x_values, y_values, "b-")
    plt.xlabel("x", fontsize=15)
    plt.ylabel("f(x)", fontsize=15)
    plt.show()


plot_riemann(-1, 4, 15, -2, 3, 100)
print(riemann(-1, 4, 15, -2, 3, 10))
